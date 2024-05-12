# Like conllu-split-feats.py, but load input files separately from
# different places and different names based on a todo list (actually 
# a dict).

import pathlib
import re

wdir = pathlib.Path("Results/conllu_files")
rdir = pathlib.Path("Results/conllu_files")
rdir_je = pathlib.Path("../../jenna/latin-tagger-outputs")

todo = {
        'ITTB': [['Trankit', 'Mega'], ['Stanza', 'Mega', 'pretokenized']], 
        'LLCT': [['Trankit', 'Mega'], ['Stanza', 'Mega', 'pretokenized']],
        'Perseus': [['Trankit', 'Mega'], ['Stanza', 'Classical', 'pretokenized']],
        'PROIEL': [['Trankit', 'Mega'], ['Stanza', 'Classical', 'pretokenized']],
        'UDante': [['Trankit', 'Mega'], ['Stanza', 'Mega', 'pretokenized']],
        }

# Dream data format: {}

for bank in todo:
    print(todo[bank])

    # load hm files, first only Trankit?
    for file in rdir.glob('MM_Trankit*'):
        
        if todo[bank][0] in file:  # sisältyy?

        # if (todo[bank][0][kaikki] in file) or (todo[bank][1][kaikki] in file):
            pass

    # load Stanza files separately?:
    for file in rdir.glob('*_pretokenized-Trankit.conllu'):
        pass
    # load jenna files
    for file in rdir_je.glob('*' + bank.lower() + '*.conllu'):
        pass

    # load all in variable `data`?

