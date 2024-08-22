import argparse
import sys

ID, FORM, LEMMA, UPOS, XPOS, FEATS, HEAD, DEPREL, DEPS, MISC = range(10)

def read_tokens(fname):
    # function to read tokens from a file
    # tokens is a list of all tokens, where a token is a list (typically length == 1, but can be more in case of multiword tokens)
    tokens = []
    with open(fname, 'rt', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            cols = line.split("\t")
            
            if "-" in cols[ID]: # this is a multiword token
                token = [cols]
                start, end = int(cols[ID].split("-")[0]), int(cols[ID].split("-")[1]) # how many tokens to read
                for i in range(start, end+1):
                    new_line = f.readline() # read next line
                    new_line = new_line.strip()
                    new_cols = new_line.split("\t")
                    token.append(new_cols)
                tokens.append(token) # multiword token ready, append to tokens
                continue
            tokens.append([cols]) # normal token, append to tokens

    return tokens

def get_oracle(gold, predictions):
    placeholder = predictions[0] # take the first prediction as a placeholder to get columns, rewrite fields later
    if len(placeholder) > 1 or len(gold) > 1:
        oracle = get_oracle(gold[-1:], [p[-1:] for p in predictions]) # if one of these is a multiword token, process the last token
        placeholder[-1] = oracle[0] # rewrite the last token with the oracle
        return placeholder
    gold_upos = gold[0][UPOS]
    gold_feats = gold[0][FEATS]
    predicted_upos = [p[0][UPOS] for p in predictions]
    predicted_feats = [p[0][FEATS] for p in predictions]
    if gold_upos in predicted_upos: # if gold among predicted, rewrite placeholder
        placeholder[0][UPOS] = gold_upos
    if gold_feats in predicted_feats: # if gold among predicted, rewrite placeholder
        placeholder[0][FEATS] = gold_feats
        return placeholder # done, return

    # process categories separately
    if gold_feats == "_" or placeholder[0][FEATS] == "_":
        return placeholder # if gold has no features or default has no categories, we cannot do anything, return as is
    #pruned_features = []
    #for upos, feats in zip(predicted_upos, predicted_feats):
    #    if upos == placeholder[0][UPOS]: # if upos matches the selected one, keep the features
    #        if feats == "_":
    #            continue
    #        pruned_features.append(feats)
    #if len(pruned_features) == 0:
    #    return placeholder
    all_values = {} # here we collect which values we have seen for each category
    for feature in predicted_feats:
        if feature == "_":
            continue
        for f in feature.split("|"):
            c, v = f.split("=")
            if c not in all_values:
                all_values[c] = []
            all_values[c].append(v)
    
    gold_features = {feature.split("=")[0]:feature.split("=")[1] for feature in gold_feats.split("|")} # gold features as a dictionary

    selected_features = placeholder[0][FEATS].split("|")
    for i, category in enumerate(selected_features): # go through the selected categories 
        cat, val = category.split("=")
        if cat in gold_features and gold_features[cat] in all_values[cat]: # if gold has this category, AND if we have seen the gold value in our predicted values: rewrite
            selected_features[i] = cat + "=" + gold_features[cat] # rewrite placeholder with gold value
    placeholder[0][FEATS] = "|".join(selected_features) # rewrite the whole FEATS field
    
    return placeholder # return placeholder, predictions rewritten

def norm(form):
    return form.replace(" ", "")

def main(args):
    print("Using prediction files:", args.predicted_files)

    gold_tokens = read_tokens(args.gold) # gold tokens is a list of tokens, where a token is a list (typically length == 1, but can be more in case of multiword tokens)
    predicted_tokens = [read_tokens(f) for f in args.predicted_files] # same for predicted tokens
    print("Predicted tokens:", [len(tokens) for tokens in predicted_tokens]) # length of each predicted file must be the same
    print("Gold tokens:", len(gold_tokens)) # length of gold tokens can differ

    oracle_tokens = [] # here collect the oracle predictions for each token
    gold_idx = 0 # where are we going in gold tokens
    current_form = "" # this is because in some cases we need to combine predicted tokens (keep reading until we match the gold token)
    for predictions in zip(*predicted_tokens): # go through the predicted tokens ony by one
        form = current_form + predictions[0][0][FORM]
        gold_form = gold_tokens[gold_idx][0][FORM]
        if norm(form) == norm(gold_form): # norm removes spacing, if predicted and gold form match, we take the oracle prediction
            oracle = get_oracle(gold_tokens[gold_idx], predictions)
            oracle_tokens.append(oracle)
            print(f"Oracle: {oracle[0][FEATS]} out of {[p[0][FEATS] for p in predictions]}")
            gold_idx += 1
            current_form = ""
            continue
        else:
            print(f"missmatch! gold: {gold_form}, predicted: {form}")

            if len(form) < len(gold_form): # if predicted form is shorter than gold form, we need to keep reading predicted tokens
                oracle_tokens.append(predictions[0]) # tokenization error, there is nothing we can do to this one because we do not have mathing gold token
                current_form = form # keep the form for the next iteration, so that we combine predicted tokens until we hit the matching gold token
                continue

            if len(form) > len(gold_form): # if predicted form is longer than gold form, we need to keep reading gold tokens
                while len(norm(gold_form)) < len(norm(form)): # while predicted is longer, keep reading
                    gold_idx += 1
                    gold_form = gold_form + gold_tokens[gold_idx][0][FORM]
                print(gold_form)
                assert norm(form) == norm(gold_form)
                oracle = get_oracle(gold_tokens[gold_idx], predictions) # now take the oracle using the final gold token analysis
                oracle_tokens.append(oracle)
                gold_idx += 1
                current_form = ""
            
    with open(args.output, 'wt', encoding='utf-8') as output_file:
        for i, token in enumerate(oracle_tokens):
            if i != 0 and token[0][ID].split("-")[0]=="1":
                print(file=output_file)
            for t in token: # in case of multiword tokens, there might be more than one
                print("\t".join(t), file=output_file)
        print(file=output_file)
 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Oracle')
    parser.add_argument('predicted_files', nargs='+', help='Files to use')
    parser.add_argument('--gold', type=str, required=True, help='Gold file')   
    parser.add_argument('--output', type=str, default='oracle_output.txt', help='Output file')
    args = parser.parse_args()
    
    main(args)