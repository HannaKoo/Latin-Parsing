# Based on conllu-split-feats.py 2024-05-12

# Collect and combine corresponding columns from different conllu-files for comparison.
# - Input files must have same tokenization and other line breaks 
#   - (FIXME: mwt's differ! What to do? Follow (only) ID's!)
#   - (Also some have "# text =" and some don't. Skip # lines.)
#   - Or prepare files beforehand: feedback.py!
# Then split FEATS-column on '|'. Then split feats on '=' and make a dict.

# Write a new conllu file with voted UPOS (and FEATS?).
# Take LEMMA from Stanza.

# Difference:
# - Earlier we wanted to split feats, but now we might just copy them
# verbatim to the result conllu?
# - We might want to vote on FEATS features, when everyone agrees on POS.

import pathlib
import csv
import re
from collections import Counter
from pprint import pprint

# Selected models:
# ITTB: TrMegaITTB-StMegaPreITTB-CustomITTB
# LLCT: TrMegaLLCT-StMegaPreLLCT-CustomLLCT
# Perseus: TrMegaPerseus-StClassPrePerseus-CustomPerseus
# PROIEL: TrMegaPRO-StClassPrePRO-CustomPRO
# UDante: TrMegaUdante-StMegaPreUDante-CustomUDante

todo = {  # (Not used)
        'ITTB': [['Trankit', 'Mega'], ['Stanza', 'Mega', 'pretokenized']], 
        'LLCT': [['Trankit', 'Mega'], ['Stanza', 'Mega', 'pretokenized']],
        
        }

# There's no loop, only one allowed:
# bank = 'ittb'
# bank = 'llct'
bank = 'perseus'
# bank = 'proiel' 
# bank = 'udante'

wdir = pathlib.Path("Results/conllu_files/test_output")
rdir = pathlib.Path("Results/conllu_files/vote_" + bank)

# Filename eg: MM_Stanza-Classical_proiel_pretokenized-Trankit.conllu
# origin_filename_pattern = "MM_(.*?)_(.*?)_.*"
#                              ^^^   ^^^ = file id / origin, eg. Stanza-Mega_ittb
model_filename_pattern = "MM_(.*?)[-_].*"
header = ['ID','FORM','LEMMA','UPOS','XPOS','FEATS','HEAD','DEPREL','DEPS','MISC']

def read_conllus(rdir, filename_pattern):
    # Read conllu files in rdir into a dict based data structure
    # {'Custom_proiel': [{'ID': '1', 'FORM': 'adtendite', ...}, {...}], 'Stanza-Classical_proiel': [{'ID': '1', 'FORM': 'adtendite', ...}, {...}], ...}
    # {origin: [{header: value}]}
    #           ^^^^^^^^^^^^^^^ = row
    # Where row corresponds to the lines in the input and output files
    
    files = list(rdir.iterdir())  # This reads all files in rdir.
    # Plan-B: test filename in the loop using RE. <-- FIXME: Do Plan-B
    # if todo in file:  # FIXME
    # Plan-C: For now, we are reading all files in rdir.
    data = {}  # (dict of lists of dicts)
    header = ['ID','FORM','LEMMA','UPOS','XPOS','FEATS','HEAD','DEPREL','DEPS','MISC']
    p = re.compile(filename_pattern)
    for file in files:
        m = p.match(file.stem)
        origin = m.group(1) # + '_' + m.group(2)
        print("Reading  ", file)
        print("as", origin, "\n")
        with open(file, 'r', newline='', encoding="utf8") as f:
            reader = csv.DictReader(f, fieldnames=header, delimiter='\t')
            data[origin] = []
            for row in reader:
                data[origin].append(row)
    return data

def split_feats(data):
    featkeys = set()
    for origin in data:
        for row in data[origin]:  # row = line number of the input, and output, files
            if row['FEATS']:
                featslist = (row['FEATS'].split('|'))
                row['FEATS'] = {}
                if featslist[0] == '_':
                    row['FEATS']['_'] = None
                else:
                    for feat in featslist:
                        key, value = feat.split('=')
                        featkeys.add(key)
                        row['FEATS'][key] = value
    return data, featkeys

def join_feats(feat_dict):
    # Turn a feats dict back into a string,
    
    if feat_dict == {'_': None}:
        return '_'
    
    feat_list = []
    for feat in feat_dict:
        feat_list.append(feat + '=' + feat_dict[feat])
    return '|'.join(feat_list)

def popularity_vote(data, line_nr):
    # Count most popular UPOS and its count on data line line_nr,
    # returns tuple (most popular UPOS, it's count).
    # if there are no UPOS, return (None, None).
    # TODO: Which origins is the winner from?
    # UPOSes = []
    UPOSes = {}
    for model in data:

        UPOSes[model] = data[model][line_nr]['UPOS']
        # {Stanza: NOUN, Trankit:NOUN, udtagger:VERB}
    votedPOS, popularity = Counter(UPOSes.values()).most_common(1)[0]
    # print(data[model][line_nr]['FORM'], votedPOS, popularity)
    todelete = []
    for i in UPOSes:
        if UPOSes[i] != votedPOS:
            todelete.append(i)
    for i in todelete:
        del UPOSes[i]
    return votedPOS, popularity, UPOSes

# From the old popularity_vote():
# Where does it need the None check?
    #     UPOS = data[origin][line_nr]['UPOS']
    #     if UPOS != None:  # TODO: Try .get(key, with default)
    #         UPOSes.append(UPOS)
    #     if UPOSes == []:
    #         return None, None
    # return Counter(UPOSes).most_common(1)[0]  # , best_origin(s)

def feats_vote(data, line_nr):
    # Voting for the case when all UPOS agree.
    # For now compare all FEATS at once.
    FEATSes = []
    for model in data:
        FEATSes.append(join_feats(data[model][line_nr]['FEATS']))
    voted_FEATS, FEATSpopularity = Counter(FEATSes).most_common(1)[0]
    return voted_FEATS, FEATSpopularity


data = read_conllus(rdir, model_filename_pattern)
data, featkeys = split_feats(data)
# TODO: Get rid of featkeys
# Write a function to get feats from data.

# example (from Auctoritate):
# The first non-empty FEATS is on line 10; This should print Abl.
# print(data['stanza-ittb'][10]['FEATS']['Case'])

wdir.mkdir(parents=True, exist_ok=True)

with open(wdir/('feats_' + bank + '.txt'), 'w', encoding='utf8') as f_feats:
    feats = {}
    for origin in data:
        feats[origin] = []
        for row in data[origin]:
            if row['FEATS']:
                f_feats.write(str(row['FEATS']) + '\n')
                # (Separating key and value with '=' looked clearer than this dict-look)

with open(wdir/('featkeys_' + bank + '.txt'), 'w', encoding='utf8') as f_featkeys:
    # Print featkeys sorted, so it does not change with every run and confuse git.
    f_featkeys.write("featkeys: " + str(sorted(featkeys)) + "\n")
    f_featkeys.write("len: " + str(len(featkeys)))

with open(wdir/('data_' + bank + '.txt'), 'w', encoding='utf8') as f_data:
    pprint(data, width=100, stream=f_data, sort_dicts=False)
    # f_data.write(str(data))

# How to read and write dict to human editable file? 
# - json, will it work with the nested structures?
# - But this one doesn't need nested structures!
# a dict of which feats to include:
# include_feats = {'Case': True, 'Gender': True, 'Number': True,
                #  'InflClass': False, 'InflClass[Nominal]': False,
                #  'NumType': None}
include_feats = ['Case', 'Gender', 'Number', 'Degree', 'Aspect', 'Mood', 'Tense', 'Voice', 'VerbForm', 'Person']
include_POS = ['NOUN', 'PROPN', 'ADJ', 'VERB', 'DET', 'PRON', 'ADV', 'NUM']
# TODO: List FEATS from these POS's only?

writeheaders1 = ['ID', 'FORM', 'UPOS', 'pop']
writeheaders2 = [''] * len(writeheaders1)

# Put feats into a list for the first header line,
# (and count the feats to include.)
num_feats = 0
for feat in include_feats:
    # if include_feats[feat]:
    #     num_feats += 1
        writeheaders1.extend( [feat] * len(data) )

# Put origins to the second header line list.
origins = []
for origin in data:
    origins.append(origin)
# writeheaders2.extend( origins * num_feats )
writeheaders2.extend( origins * len(include_feats) )

wfile = wdir/('feats-split_' + bank + '.tsv')
with wfile.open('w', newline='', encoding='utf8') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerow(writeheaders1)
    tsv_writer.writerow(writeheaders2)

    for i, row in enumerate(data['udtagger']): # _' + bank]):
        # It does not matter which ^^origin^^ to choose here, because
        # line breaks, ID and FORM match(?)
        UPOS_popular, UPOS_popularity, best_models = popularity_vote(data, i)
        newrow = [row['ID'], row['FORM'], UPOS_popular, UPOS_popularity] 
        for j in include_feats:
            for origin in data:
                if data[origin][i]['FEATS']:
                    if j in data[origin][i]['FEATS']:
                        newrow.append(data[origin][i]['FEATS'][j])
                    else:
                        newrow.append('')  # insert placeholder for empty column
        tsv_writer.writerow(newrow)

# Write conllu with voting:
# ------------------------
default = 'Trankit'
with open(wdir/('MM_voted-FEATSwhole_' + bank + '.conllu'), 'w', newline='', encoding='utf8') as f_voted:
    vote_writer = csv.writer(f_voted, delimiter='\t')
    skipnext = False
    for i, row in enumerate(data['udtagger']): # _' + bank]):

        # Add newlines between sentences:
        if row['ID'].startswith('1-') and i != 0:  # sentence begins with mwt
            vote_writer.writerow('')
            skipnext = True
        if row['ID'] == '1' and i != 0:
            if skipnext:
                skipnext = False
            else:
                vote_writer.writerow('')

        # UPOS_popular, UPOS_popularity = popularity_vote(data, i)
        UPOS_popular, UPOS_popularity, best_models = popularity_vote(data, i)
        newrow = []
        for head in header:
            if head == 'LEMMA':
                newrow.append(data['Stanza'][i][head])
            elif head == 'UPOS':
                newrow.append(UPOS_popular)
            elif head == 'FEATS':
                if UPOS_popularity == 3:  # Now we can vote on FEATS:
                    FEATS_popular, FEATS_popularity = feats_vote(data, i)
                    if FEATS_popularity == 1:  # Vote even, default to Trankit:
                        # best_model = 'Trankit'
                        newrow.append(join_feats(data['Trankit'][i][head]))
                    else:
                        newrow.append((FEATS_popular))
                        # BUG: we should assign to best_model but don't know what it is...
                        # modify FEATS vote to match POS vote, or use append everywhere?
                        # Would it be possible to combine FEATS-vote and POS-vote?
                elif 'Trankit' in best_models:
                    best_model = 'Trankit'
                    newrow.append(join_feats(data[best_model][i][head]))
                else:
                    best_model = 'udtagger'
                    newrow.append(join_feats(data[best_model][i][head]))
            else:
                newrow.append(data[default][i][head])
        vote_writer.writerow(newrow)
        # vote_writer.writerow([UPOS_popular, UPOS_popularity])
        # vote_writer.writerow(best_models)
    vote_writer.writerow('')  # Add newline at the end.

# Voting cases:
# - three different UPOSes: Pick UPOS and FEATS from Trankit (and the whole line preferably?)
# - 2 vs 1: Pick winning UPOS, and select corresponding FEATS in order (of what's left): 
#     1. trankit -> If Trankit is among the best, take the whole line from there (apart from LEMMA).
#     2. udtagger -> pick udtagger if Trankit was in the minority.
#     3. stanza (i.e. Never pick Stanza!)
# - three same UPOSes: Vote FEATS: as a whole, or individual FEATs.
#    FIXME: The current implementation picks Trankit(?)

# Not necessary: All LEMMAs from Stanza, because it's the best. And udtagger has no LEMMAs.
