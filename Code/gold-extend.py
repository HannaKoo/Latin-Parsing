# Requires Python >= 3.10!

# Write gold upos next to the upos vote results.
# In this crude version we decided it is enough to skip mwt's.
# (First remove all mwt's, comments, etc. from all input files somewhere else (TM), so the tokenization and lines will match, but then how to modify this to read four files but vote with only three?)
# Or
# Read from the gold standard until we find the same word. Then pick UPOS from there.
# ----------------------------------------------------------------------------------

import argparse
import sys
from collections import Counter

ID, FORM, LEMMA, UPOS, XPOS, FEATS, HEAD, DEPREL, DEPS, MISC = range(10)

vote_results = {1: 'evenvote', 2: 'two2one', 3:'allsame'}

def vote_upos(upos):
    # upos is a list of upos tags
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

    # print("Voting individual features!")
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
    print(args.gold)

    files = [open(fname, 'rt', encoding='utf-8') for fname in args.predicted_files]
    lines_to_skip = 0

    # Requires Python 3.10 (parenthesized context managers):
    with (open(args.output, 'w', encoding='utf-8') as f,
          open(args.gold, 'r', encoding='utf-8') as gold):
        for lines in zip(*files):
            # lines is a list of lines, one from each file
            if lines_to_skip > 0:
                lines_to_skip -= 1
                continue
            lines = [line.strip() for line in lines]
            if not lines[0] or lines[0].startswith("#"): # if empty line or comment, print and continue
                print(lines[0], file=f)
                continue
            cols = [line.split("\t") for line in lines]
            if "-" in cols[0][ID]: # multiword token without analysis, we can print it and continue
                print(lines[0], file=f)
                # skip rest of the mwt:
                start, end = int(cols[0][ID].split("-")[0]), int(cols[0][ID].split("-")[1])
                lines_to_skip = end - start + 1
                continue
            if " " in cols[0][FORM]: # tokenization has multiple words together, print and skip.
                print(lines[0], file=f)
                continue


            upos = [c[UPOS] for c in cols] # gather all upos's
            feats = [c[FEATS] for c in cols] # gather all features

            voted_upos, num_votes = vote_upos(upos)
            # print(f"Voted {voted_upos} from {upos} with popularity {num_votes}")

            voted_feats = vote_feats(feats)
            # print(f"Voted {voted_feats} from {feats}")
            
            place = gold.tell()  # Remember where we start searching in case we have to abort and return
            maxloop = 100  # We are skipping sentence breaks and mwts, so 100 is probably overkill.
            for i in range(maxloop):
            # while True: # Search for the next gold standard line with same FORM as cols[0]
                # Abort search after maxloop reached. (What will happen if we run into end-of-file first?)
                goldline = gold.readline()
                goldline = goldline.strip()
                # print(goldline)
                if not goldline or goldline.startswith("#"):
                    continue
                goldcols = goldline.split("\t")
                if goldcols[FORM] == cols[0][FORM]:
                    break
                    # BUG: Will loop forever when Trankit has tokenized 'quo posito' 
                    # and gold standard has 'quo' and 'posito'. FIXED: by skipping lines 
                    # with a " " in FORM.
            else: # no match found
                print("Aborting, cols[0][FORM] =", cols[0][FORM])
                gold.seek(place)
                goldcols[UPOS] = "N/A"

            cols[0][UPOS] = voted_upos
            cols[0][FEATS] = voted_feats

            if voted_upos == goldcols[UPOS]:
                iscorrect = "yesright"
            else:
                iscorrect = "thatswrong"

            upos = ",".join(upos)
            # upos.append(vote_results[num_votes])
            cols[0][UPOS+1:UPOS+1] = [upos, vote_results[num_votes], iscorrect, goldcols[UPOS]]
            # Insert the whole upos list after the voted upos, and voting result
            
            print("\t".join(cols[0]), file=f)


    # Done!




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Majority vote keeping all uposes')
    parser.add_argument('predicted_files', nargs='+', help='Files to use')
    parser.add_argument('--gold', type=str, required=True, help='Gold file')   
    parser.add_argument('--output', type=str, required=True, help='Output file')
    args = parser.parse_args()
    
    main(args)
