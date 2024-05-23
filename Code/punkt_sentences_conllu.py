#!/usr/bin/env python3

# Add a '.' at the end of every sentence in a conllu file.
# Should we try to write a conllu file or is a txt enough?

# A txt is enough to parse, but then conllu eval.py will not evaluate them,
# because of the extra dots. And if the dots are removed, the token
# numbering has holes, which will again upset eval.py.

# Read all lines
# Find the next empty line, take the number from the ^ previous line, add
# one and the '.'. We should probably also fill in a template conllu line like
# 14  .   .   PUNCT   u--------   _   13  punct   _   _
# But where to get the HEAD? (13 in the example) Just subtract one from the
# current id?

# What about mwt's? Take the mwt header line and drop the parts.

# TODO: Remove the space before a dot. Capitalize sentences?
# TODO: This splits lines after each sentence, would it be better to split at
# some line length?

import pathlib
import csv

rdir = pathlib.Path("../../UD_Latin-CIRCSE")
rfile = pathlib.Path("la_circse-ud-test.conllu")
wdir = pathlib.Path("../Latin-Parsing/Data")
wfile = pathlib.Path("la_circsepunkt-ud-test.conllu")

template = ["14", ".", ".", "PUNCT", "u--------", "_", None, "punct", "_", "_"]
nrHEAD = 6

with open(rdir/rfile, 'r', newline='', encoding='utf8') as f, \
     open(wdir/wfile, 'w', newline='', encoding='utf8') as conl:
    tsv_reader = csv.reader(f, delimiter='\t')
    conllu_writer = csv.writer(conl, delimiter='\t')
    for row in tsv_reader:
        # print(row)
        if len(row) == 0:
            punkt = template
            punkt[0] = int(prev) + 1
            punkt[6] = '_'
            conllu_writer.writerow(punkt)
            conllu_writer.writerow('')
        # elif row[0][0] == '#':
        #     continue  # Copy comments as is?
        # elif '-' in row[0]:  # mwt, skip over the parts:
        #     # FIXME: Copy mwt as is. (Leave the whole elif out?)
        #     conllu_writer.writerow(row[1] + ' ')
        #     mwt_end = int(row[0].split('-')[1])
        #     # print(mwt_end)
        #     while int(next(tsv_reader)[0]) < mwt_end:
        #         pass  # would continue be better? different?
        else:        
            prev = (row[0])
            conllu_writer.writerow(row)
