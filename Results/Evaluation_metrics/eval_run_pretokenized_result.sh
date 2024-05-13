[kupariha@puhti-login12 Latin-Parsing]$ ./eval_conllu_files.py 
bank perseus
conllu_file Results/conllu_files/raw_pretokenized/MM_Stanza-Classical_perseus_pretokenized-Trankit.conllu
wfile Results/Evaluation_metrics/MM_Stanza-Classical_perseus_pretokenized-Trankit.md
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL_vulgate
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-ITTB
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL_classical
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-UDante
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-LLCT
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-Perseus
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-Perseus perseus
Traceback (most recent call last):
  File "/projappl/project_2008402/tools/eval.py", line 774, in <module>
    main()
  File "/projappl/project_2008402/tools/eval.py", line 769, in main
    evaluation = evaluate_wrapper(args)
  File "/projappl/project_2008402/tools/eval.py", line 705, in evaluate_wrapper
    return evaluate(gold_ud, system_ud)
  File "/projappl/project_2008402/tools/eval.py", line 652, in evaluate
    "".join(map(_encode, system_ud.characters[index:index + 20]))
__main__.UDError: The concatenation of tokens in gold file and in system file differ!
File '../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-Perseus/MM-la_perseus-ud-test.conllu':
  Token no. 1283 on line no. 1661 is the last one with all characters reproduced in the other file.
  The previous 10 tokens are 'motuque vias patefecit aquarum . Exspatiata ruunt per apertos flumina'.
  The next 10 tokens are 'campos cumque satis arbusta simul pecudesque virosque tectaque cumque suis'.
File 'Results/conllu_files/raw_pretokenized/MM_Stanza-Classical_perseus_pretokenized-Trankit.conllu':
  Token no. 1304 on line no. 1597 is the last one with all characters reproduced in the other file.
  The previous 10 tokens are 'que vias patefecit aquarum . Exspatiata ruunt per apertos flumina'.
  The next 10 tokens are 'campocumum que satis arbusta simul pecudes que viros que tectatecum'.
First 20 differing characters in gold file: 'scumquesatisarbustas' and system file: 'cumumquesatisarbusta'
bank proiel
conllu_file Results/conllu_files/raw_pretokenized/MM_Stanza-Classical_proiel_pretokenized-Trankit.conllu
wfile Results/Evaluation_metrics/MM_Stanza-Classical_proiel_pretokenized-Trankit.md
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL_vulgate
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-ITTB
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL proiel
bank udante
conllu_file Results/conllu_files/raw_pretokenized/MM_Stanza-Mega_udante_pretokenized-Trankit.conllu
wfile Results/Evaluation_metrics/MM_Stanza-Mega_udante_pretokenized-Trankit.md
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL_vulgate
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-ITTB
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL_classical
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-UDante
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-UDante udante
Traceback (most recent call last):
  File "/projappl/project_2008402/tools/eval.py", line 774, in <module>
    main()
  File "/projappl/project_2008402/tools/eval.py", line 769, in main
    evaluation = evaluate_wrapper(args)
  File "/projappl/project_2008402/tools/eval.py", line 705, in evaluate_wrapper
    return evaluate(gold_ud, system_ud)
  File "/projappl/project_2008402/tools/eval.py", line 652, in evaluate
    "".join(map(_encode, system_ud.characters[index:index + 20]))
__main__.UDError: The concatenation of tokens in gold file and in system file differ!
File '../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-UDante/MM-la_udante-ud-test.conllu':
  Token no. 1712 on line no. 1915 is the last one with all characters reproduced in the other file.
  The previous 10 tokens are 'aliorum scriptorum volumina quibus mundus universaliter et membratim describitur ,'.
  The next 10 tokens are 'ratiocinantesque in nobis situationes varias mundi locorum et eorum habitudinem'.
File 'Results/conllu_files/raw_pretokenized/MM_Stanza-Mega_udante_pretokenized-Trankit.conllu':
  Token no. 1713 on line no. 1862 is the last one with all characters reproduced in the other file.
  The previous 10 tokens are 'aliorum scriptorum volumina quibus mundus universaliter et membratim describitur ,'.
  The next 10 tokens are 'rratinantes que in nobis situationes varias mundi locorum et eorum'.
First 20 differing characters in gold file: 'atiocinantesqueinnob' and system file: 'ratinantesqueinnobis'
bank ittb
conllu_file Results/conllu_files/raw_pretokenized/MM_Stanza-Mega_ittb_pretokenized-Trankit.conllu
wfile Results/Evaluation_metrics/MM_Stanza-Mega_ittb_pretokenized-Trankit.md
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL_vulgate
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-ITTB
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-ITTB ittb
bank proiel
conllu_file Results/conllu_files/raw_pretokenized/MM_Stanza-Classical_proiel_pretokenized-Trankit_comments-rm.conllu
wfile Results/Evaluation_metrics/MM_Stanza-Classical_proiel_pretokenized-Trankit_comments-rm.md
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL_vulgate
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-ITTB
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL proiel
bank llct
conllu_file Results/conllu_files/raw_pretokenized/MM_Stanza-Mega_llct_pretokenized-Trankit.conllu
wfile Results/Evaluation_metrics/MM_Stanza-Mega_llct_pretokenized-Trankit.md
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL_vulgate
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-ITTB
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL_classical
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-UDante
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-LLCT
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-LLCT llct
[kupariha@puhti-login12 Latin-Parsing]$ 