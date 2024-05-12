# Based on auctoritate/Code/conllu-split-feats.py 2024-05-10

# Collect and combine corresponding columns from different conllu-files for comparison.
# - Input files must have same tokenization and other line breaks 
#   - (FIXME: mwt's differ! What to do? Follow (only) ID's! 
#   - Also some have "# text =" and some don't. Skip # lines.
#   - Or prepare files beforehand: feedback.py) 
# Then split FEATS-column on '|'. Then split feats on '=' and make a dict.

import pathlib
import csv
import re
from collections import Counter
from pprint import pprint

# ITTB: TrMegaITTB-StMegaPreITTB-CustomITTB
# LLCT: TrMegaLLCT-StMegaPreLLCT-CustomLLCT
# Perseus: TrMegaPerseus-StClassPrePerseus-CustomPerseus
# PROIEL: TrMegaPRO-StClassPrePRO-CustomPRO
# UDante: TrMegaUdante-StMegaPreUDante-CustomUDante

todo = {
        'ITTB': [['Trankit', 'Mega'], ['Stanza', 'Mega', 'pretokenized']], 
        'LLCT': [['Trankit', 'Mega'], ['Stanza', 'Mega', 'pretokenized']],
        
        }

# wdir = pathlib.Path("Results/conllu_files")
wdir = pathlib.Path("Results/conllu_files")
# rdir = pathlib.Path("Results/conllu_files")
rdir = pathlib.Path("Results/conllu_files/test_vote")
# rdir_je = pathlib.Path("../../jenna/latin-tagger-outputs")
# MM_Stanza-Classical_proiel_pretokenized-Trankit.conllu
# filename_pattern_hm = "MM_(.*)_(.*)_.*"
filename_pattern = "MM_(.*)_(.*)_.*"
#                         ^^^^ ^^^^ = file id / origin, eg. Stanza-Mega ... ittb
# jenna/latin-tagger-outputs/MM-la_proiel-ud-test.udtagger.conllu
# filename_pattern_je = "MM-la_(.*)-.*\.(.*)\.conllu"
#                            ^^^^     ^^^^ = eg. proiel ... udtagger
# Should this be lazy?

def read_conllus(rdir, filename_pattern):
    # Read conllu files in rdir into a dict based data structure
    # FIXME:
    # {'stanza-classical-proiel': [{'ID': '1', 'FORM': 'Deinde', ...}, {...}], 'UDPipe2-udante': [{'ID': '1', 'FORM': 'Deinde', ...}, {...}], ...}
    # {origin: [{header: value}]}
    #           ^^^^^^^^^^^^^^^ = row
    # Where row corresponds to the lines in the input and output files
    
    files = list(rdir.iterdir())  # + list(rdir_je.iterdir())
    # This reads all files in rdir and rdir_je.
    # (TODO: put filename_pattern here (glob.glob? But that doesn't understand RE?)
    # Plan-B: test filename in the loop using RE. <-- FIXME: Do Plan-B)

    data = {}  # (dict of lists of dicts)
    header = ['ID','FORM','LEMMA','UPOS','XPOS','FEATS','HEAD','DEPREL','DEPS','MISC']
    p = re.compile(filename_pattern)
    for file in files:
        print("Reading  ", file)
    # if todo in file:  # FIXME
        m = p.match(file.stem)
        origin = m.group(1) + '-' + m.group(2)
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

def popularity_vote(data, line_nr):
    # Count most popular UPOS and its count on data line line_nr,
    # returns tuple (most popular UPOS, it's count).
    # if there are no UPOS, return (None, None).
    # FIXME: line nr is a problem here, use ID instead, somehow.
    UPOSes = []
    for origin in data:
        UPOS = data[origin][line_nr]['UPOS']
        if UPOS != None:  # TODO: Try .get(key, with default)
            UPOSes.append(UPOS)
        if UPOSes == []:
            return None, None
    return Counter(UPOSes).most_common(1)[0]


data = read_conllus(rdir, filename_pattern)
# read_conllus(rdir_je, filename_pattern_je)
data, featkeys = split_feats(data)
# TODO: Get rid of featkeys
# Write a function to get feats from data.

# example: The first non-empty FEATS is on line 10; This should print Abl.
# print(data['stanza-ittb'][10]['FEATS']['Case'])

wdir.mkdir(parents=True, exist_ok=True)

with open(wdir/'feats.txt', 'w', encoding='utf8') as f_feats:
    feats = {}
    for origin in data:
        feats[origin] = []
        for row in data[origin]:
            if row['FEATS']:
                f_feats.write(str(row['FEATS']) + '\n')
                # (Separating key and value with '=' looked clearer than this dict-look)

with open(wdir/'featkeys.txt', 'w', encoding='utf8') as f_featkeys:
    # Print featkeys sorted, so it does not change with every run and confuse git.
    f_featkeys.write("featkeys: " + str(sorted(featkeys)) + "\n")
    f_featkeys.write("len: " + str(len(featkeys)))

with open(wdir/'data.txt', 'w', encoding='utf8') as f_data:
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
writeheaders2 = [''] * 4

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

wfile = (wdir/"feats-split.tsv")
with wfile.open('w', newline='', encoding='utf8') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerow(writeheaders1)
    tsv_writer.writerow(writeheaders2)

    for i, row in enumerate(data['stanza-ittb']):
        # TODO: Implement popularity vote function (with option to change it).
        UPOS_popular, UPOS_popularity = popularity_vote(data, i)
        newrow = [row['ID'], row['FORM'], UPOS_popular, UPOS_popularity] 
        for j in include_feats:
            for origin in data:
                if data[origin][i]['FEATS']:
                    if j in data[origin][i]['FEATS']:
                        newrow.append(data[origin][i]['FEATS'][j])
                    else:
                        newrow.append('')  # insert placeholder for empty column
        tsv_writer.writerow(newrow)
