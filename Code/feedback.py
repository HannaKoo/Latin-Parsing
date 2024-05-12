#!/usr/bin/env python3

# Copy: 
#  - mwt from Trankit-Mega
#  (- # text = ... from Stanza-pretokenized)
# to combined file. Or forget the # text's, because udtaggers don't
# have them either.
# TODO: Check that the tokenization matches while we're here.
# And don't forget to copy the empty lines, that should match already.

import csv  # But how to read tsv, and copy as lines?
# just split('\t') ?
import pathlib

rdir = pathlib.Path('Results/conllu_files/raw_pretokenized')
wdir = pathlib.Path('Results/conllu_files')
conlludir = pathlib.Path('Results/conllu_files')

# eg. MM_Stanza-Classical_proiel_pretokenized-Trankit.conllu
#     MM_Trankit-Mega_proiel_nolinebreaks.conllu

for st_file in rdir.glob('*'):
    bank = st_file.stem.split('_')[2]
    print("Now doing:", bank)
    tr_filename = pathlib.Path("MM_Trankit-Mega_" + bank + "_nolinebreaks.conllu")
    tr_file = conlludir/("vote_" + bank)/tr_filename
    wfilename = pathlib.Path(st_file.stem + "_fedback.conllu")
    wfile = wdir/("vote_" + bank)/wfilename
    print("Opening:")
    print(st_file)
    print(tr_file)
    print(wfile)
    with open(st_file,'r', encoding='utf8') as st, \
         open(tr_file,'r',encoding='utf8') as tr, \
         open(wfile,'w', encoding='utf8') as fixd:
        for i, tr_line in enumerate(tr):
            if '-' in tr_line.split('\t')[0]:
                print(i, tr_line)
                fixd.write(tr_line)
            else:
                fixd.write(st.readline())
