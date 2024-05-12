#!/usr/bin/env python3

# Copy: 
#  - mwt from Trankit-Mega
#  (- # text = ... from Stanza-pretokenized)
# to combined file. Or forget the # text's, because udtaggers don't
# have them either.
# BUG: This version assumes that all lines match, apart from the mwt's.
#  # text = ... lines or other extra throws the line counting off!
# TODO: Check that the tokenization matches while we're here.
# And don't forget to copy the empty lines, that should match already.

import pathlib

rdir = pathlib.Path('Results/conllu_files/raw_pretokenized')
wdirroot = pathlib.Path('Results/conllu_files')
conlluroot = pathlib.Path('Results/conllu_files')

# eg. MM_Stanza-Classical_proiel_pretokenized-Trankit.conllu
#     MM_Trankit-Mega_proiel_nolinebreaks.conllu

for st_file in rdir.glob('*'):
    bank = st_file.stem.split('_')[2]
    print("Now doing:", bank)
    tr_filename = pathlib.Path("MM_Trankit-Mega_" + bank + "_nolinebreaks.conllu")
    tr_file = conlluroot/("vote_" + bank)/tr_filename
    wfilename = pathlib.Path(st_file.stem + "_fedback.conllu")
    wfile = wdirroot/("vote_" + bank)/wfilename
    print("Opening:")
    print(st_file)
    print(tr_file)
    print(wfile)
    with open(st_file, 'r', encoding='utf8') as st, \
         open(tr_file, 'r', encoding='utf8') as tr, \
         open(wfile, 'w', encoding='utf8') as fixd:
        for tr_row in tr:
            if '-' in tr_row.split('\t')[0]:
                # BUG: If there's a '-' in #text or #sentid (ie. outside conllu rows)...
                print(tr_row)
                fixd.write(tr_row)
            else:
                fixd.write(st.readline())
