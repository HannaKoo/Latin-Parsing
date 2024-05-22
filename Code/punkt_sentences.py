#!/usr/bin/env python3

# Add a '.' at the end of every sentence in a conllu file.
# Should we try to write a conllu file or is a txt enough?

# Read all lines
# (Find the next empty line, take the number from the ^ previous line, add one and the '.'.)
# Or just write txt!: 
# Take the second column, add a punkt whenever there's an empty line.

# What about mwt's? Should take the mwt header line and drop the parts,
# but it would be easier to drop the header.

import pathlib
import csv

rdir = pathlib.Path("../../UD_Latin-CIRCSE")
rfile = pathlib.Path("la_circse-ud-test.conllu")
wdir = pathlib.Path("../trankit")
wfile = pathlib.Path("la_circsepunkt-ud-test.txt")

with open(rdir/rfile, 'r', newline='', encoding='utf8') as f, \
     open(wdir/wfile, 'w', encoding='utf8') as txt:
    tsv_reader = csv.reader(f, delimiter='\t')
    for row in tsv_reader:
        if len(row) == 0:
            txt.write('.\n')
        elif row[0][0] == '#':
            continue
        else:        
            txt.write(row[1] + ' ')
