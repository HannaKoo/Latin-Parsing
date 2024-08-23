#!/usr/bin/env python3

# Combine Evaluation_metrics into one big table.

# Only use F1 score (column 3 from 0)

import pathlib
from pprint import pprint
import csv

include = ['ModelName'.ljust(47), 'Tokens', 'UPOS', 'UFeats', 'Lemmas', 'UAS', 'LAS']

# rdir = pathlib.Path('Results/Evaluation_metrics')
# wdir = pathlib.Path('Results/Evaluation_metrics')
rdir = pathlib.Path('Results/Evaluation_metrics/voted')
wdir = pathlib.Path('Results/Evaluation_metrics/voted')

with open(wdir/'eval_table.tsv', 'w', newline='') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerow(include)
    for file in sorted(rdir.glob('*.md')):
        f1s = []
        with open(file, 'r') as f:
            print( '_'.join( file.stem.split('_')[0:4] ) )
            # f1s.append( '_'.join( file.stem.split('_')[0:4] ) )
            f1s.append(file.stem.ljust(47, '.'))
            single = list(f)
            pprint(single)
            for row in single:
                row = row.split('|')
                if row[0].strip() in include:
                    head = row[0]
                    f1 = row[3].strip()
                    f1s.append(f1)
        tsv_writer.writerow(f1s)
