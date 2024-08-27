import argparse
import sys
from collections import Counter

ID, FORM, LEMMA, UPOS, XPOS, FEATS, HEAD, DEPREL, DEPS, MISC = range(10)

vote_results = {1: 'evenvote', 2: 'two2one', 3:'allsame'}

def vote_upos(upos):
    # upos is a lsit of upos tags
    c = Counter(upos)
    k, v = c.most_common(1)[0] # count them, and take the most common
    if v > 1: # if most common appears more than once, take it...
        return k, v
    else:
        return upos[0], v # ...otherwise take the first one (files are in order of priority)
    
def vote_whole_feats(feats):
    # try if you have two to one voting using complete feature strings
    c = Counter(feats)
    k, v = c.most_common(1)[0]
    if v > 1:
        return k
    else:
        return None # if not return None
    
def vote_feats(feats):
    # feats is a list of feature analyses from different parsers (pruned to only contain the ones with the same upos tag)
    # len(feats) is at least 3

    # try to vote using whole strings, returns None if fails
    voted = vote_whole_feats(feats)
    if voted != None:
        return voted # done!

    # if not, do category-wise voting
    # the categories are taken from the first analysis (given in order of priority)
    # if the first one is "_", we can just return it (no categories to do the voting)
    if feats[0] == "_":
        return feats[0]
    
    print("Voting individual features!")
    # collect all categories and their values (key: category, value: list of values)
    d = {} 
    for feat in feats:
        if feat == "_":
            continue
        for feature in feat.split("|"):
            cat, val = feature.split("=")
            if cat not in d:
                d[cat] = []
            d[cat].append(val)

    # here collect the voted features, go through the categories of the first analysis, vote the value for it using d dictionary
    voted_features = [] 
    for feature in feats[0].split("|"):
        c, v = feature.split("=")
        counter = Counter(d[c])
        key, value = counter.most_common(1)[0]
        if value > 1: # outvoted
            voted_features.append(c+"="+key)
        else: # no consensus, take the value from the first analysis (in order of priority)
            voted_features.append(feature)


    return "|".join(voted_features)




def main(args):
    print(args.predicted_files)

    files = [open(fname, 'rt', encoding='utf-8') for fname in args.predicted_files]

    with open(args.output, 'wt', encoding='utf-8') as f:
        for lines in zip(*files):
            # lines is a list of lines, one from each file
            lines = [line.strip() for line in lines]
            if not lines[0] or lines[0].startswith("#"): # if empty line or comment, print and continue
                print(lines[0], file=f)
                continue
            cols = [line.split("\t") for line in lines]
            if "-" in cols[0][ID]: # multiword token without analysis, we can print it and continue
                print(lines[0], file=f)
                continue

            upos = [c[UPOS] for c in cols] # gather all upos's
            feats = [c[FEATS] for c in cols] # gather all features

            voted_upos, num_votes = vote_upos(upos)
            print(f"Voted {voted_upos} from {upos} with popularity {num_votes}")

            # prune features
            # if upos was outvoted, remove its features
            #pruned_features = []
            #for i, pos in enumerate(upos):
                #if pos == voted_upos:
            #        pruned_features.append(feats[i])

            #assert len(pruned_features) > 0
            #if len(pruned_features) < 3: # we have less than three left after upos pruning, cannot vote!
            #    voted_feats = pruned_features[0] # take the first one from pruned features, these are in order of priority
            #else:
            voted_feats = vote_feats(feats)
            print(f"Voted {voted_feats} from {feats}")
            
            
            cols[0][UPOS] = voted_upos
            cols[0][FEATS] = voted_feats
            upos.append(vote_results[num_votes])
            cols[0][UPOS+1:UPOS+1] = upos  # Insert the whole upos list after the voted upos
            print("\t".join(cols[0]), file=f)


    # Done!


 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Majority vote keeping all uposes')
    parser.add_argument('predicted_files', nargs='+', help='Files to use')
    parser.add_argument('--output', type=str, required=True, help='Output file')
    args = parser.parse_args()
    
    main(args)