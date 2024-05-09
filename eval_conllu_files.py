# Run eval.py on all .conllu files in Results/conllu_files/
# Save the results to Results/Evaluation_metrics/

import pathlib
import subprocess

# Results/conllu_files/*.conllu
rdir = pathlib.Path("Results/conllu_files")
wdir = pathlib.Path("Results/Evaluation_metrics")

for conllu_file in rdir.glob('*.conllu'):
    wfile = wdir/conllu_file.stem/".md"
    bank = conllu_file.split('_')[3]
    gold_standard = "../Latin-Variability/" #FIXME
    with open(wfile, "w") as f:
        subprocess.run(['eval.py', '-v', gold_standard, conllu_file], stdout=f)
