#!/usr/bin/env python3

# Run eval.py on all .conllu files in Results/conllu_files/
# Evaluate against test.conllu files in Latin-Variabity/
# Save the results to Results/Evaluation_metrics/

import pathlib
import subprocess

ud_tools = "/projappl/project_2008402/tools/"  # puhti
MM_golds = pathlib.Path("../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks")  # puhti
# NO this does not work:
# ud_tools = r"c:\Users\Hanna-Mari\Documents\Väitöskirja\tools\\"  # hm @ frakkis
# MM_golds = pathlib.Path("../misc_github/Latin-variability/morpho_harmonization/morpho-harmonized-treebanks")  # hm @ frakkis

# Results/conllu_files/*.conllu
rdir = pathlib.Path("Results/conllu_files/test_output")
wdir = pathlib.Path("Results/Evaluation_metrics")

# banks = ['ittb', 'llct', 'perseus', 'proiel', 'udante']

# for bank in banks:
# rdir = pathlib.Path("Results/conllu_files")/('vote_' + bank)
# case_sensitive requires Python 3.12!
# for conllu_file in rdir.glob('*.conllu', case_sensitive=False):
for conllu_file in rdir.glob('*.conllu'):
    wfile = (wdir/conllu_file.stem).with_suffix(".md")
    bank = str(conllu_file.stem).split('_')[2]
    print('bank', bank)
    print("conllu_file", conllu_file)
    print('wfile', wfile)
    # for gold_subdir in MM_golds.glob('*' + bank, case_sensitive=False):
    for gold_subdir in MM_golds.iterdir():
        print(gold_subdir)
        if str(gold_subdir).lower().endswith(bank):
            # Should match only one dir, is there a smart way to do this?
            print(gold_subdir, bank)
            gold_standard = gold_subdir/("MM-la_" + bank + "-ud-test.conllu")
            with open(wfile, "w") as f:
                subprocess.run([ud_tools + 'eval.py', '-v', 
                                gold_standard, 
                                conllu_file], 
                            stdout=f)
            break
