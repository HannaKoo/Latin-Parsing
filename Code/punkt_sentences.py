#!/usr/bin/env python3

# Add a '.' at the end of every sentence in a conllu file.
# Should we try to write a conllu file or is a txt enough?

# A txt is enough to parse, but then conllu eval.py will not evaluate them,
# because of the extra dots. And if the dots are removed, the token
# numbering has holes, which will again upset eval.py.

# Read all lines
# (Find the next empty line, take the number from the ^ previous line, add
# one and the '.'.)
# Or just write txt!: 
# Take the second column, add a punkt whenever there's an empty line.

# What about mwt's? Take the mwt header line and drop the parts.

# TODO: Remove the space before a dot. Capitalize sentences?
# TODO: This splits lines after each sentence, would it be better to split at
# some line length?

import pathlib
import csv

rdir = pathlib.Path("../../UD_Latin-CIRCSE")
rfile = pathlib.Path("la_circse-ud-test.conllu")
wdir = pathlib.Path("../Latin-Parsing/Data")
wfile = pathlib.Path("la_circsepunkt-ud-test.txt")

with open(rdir/rfile, 'r', newline='', encoding='utf8') as f, \
     open(wdir/wfile, 'w', encoding='utf8') as txt:
    tsv_reader = csv.reader(f, delimiter='\t')
    for row in tsv_reader:
        # print(row)
        if len(row) == 0:
            txt.write('.\n')
        elif row[0][0] == '#':
            continue
        elif '-' in row[0]:  # mwt, skip over the parts:
            txt.write(row[1] + ' ')
            mwt_end = int(row[0].split('-')[1])
            # print(mwt_end)
            while int(next(tsv_reader)[0]) < mwt_end:
                pass  # would continue be better? different?
        else:        
            txt.write(row[1] + ' ')
