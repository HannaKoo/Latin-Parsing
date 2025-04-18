#!/usr/bin/env python3

# Combine Evaluation_metrics into one big table.

import pathlib
from pprint import pprint
import csv

first_column_width = 58

include = ['ModelName'.ljust(first_column_width), 'Tokens', 'UPOS', 'UFeats', 'Lemmas', 'UAS', 'LAS']

# Only use F1 score (column 3, zero-based)
f1column = 3

# rdir = pathlib.Path('Results/Evaluation_metrics')
# wdir = pathlib.Path('Results/Evaluation_metrics')
rdir = pathlib.Path('Results/Evaluation_metrics/prevote')
wdir = pathlib.Path('Results/Evaluation_metrics/prevote')

with open(wdir/'eval_table.tsv', 'w', newline='') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerow(include)
    for file in sorted(rdir.glob('*.md')):
        f1s = []
        with open(file, 'r') as f:
            print( '_'.join( file.stem.split('_')[0:4] ) )
            # f1s.append( '_'.join( file.stem.split('_')[0:4] ) )
            f1s.append(file.stem[:first_column_width].ljust(first_column_width, '.'))
            single = list(f)
            pprint(single)
            for row in single:
                row = row.split('|')
                if row[0].strip() in include:
                    head = row[0]
                    f1 = row[f1column].strip()
                    f1s.append(f1)
        tsv_writer.writerow(f1s)
