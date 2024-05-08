# Parser article

## test-data conllus

#### File name format:  

TB version | Model     | TB: test/GS | tokenization
-----------|-----------|-------------|-------------------
MM / HM    |Stanza-Mega| LLCT        |pretokenized-Trankit

**Done:**
- (Stanza_classical_Trankit_pre_proiel_output.conllu)  
  - (MM_Stanza-Classical_pretokenized-Trankit_Proiel.md)
- MM_Stanza-Classical_proiel_pretokenized-Trankit.conllu
  - MM_Stanza-Classical_proiel_pretokenized-Trankit.md

TODO: more of these later.

### w/o pretokenized:

#### Trankit

Line breaks have been removed from the inputs for all of these, why? There are even no `# text`'s to worry about.

```python
# to solve the line breaks
doc = doc.replace("\n", " ")
```

MM
trankit
5 plain tb's:  
- [x] ittb
- [x] llct
- [x] perseus
- [x] proiel
- [x] udante

4 merged:  

Classical  
- [x,s] perseus  
- [s] proiel  

[o] Lame 
 - [s] ittb
 - [s] llct
 - [s] udante  
 - [s] proiel  

Late 
 - [s] ittb
 - [s] llct
 - [x] udante  

Mega
 - [x] ittb
 - [x] llct
 - [x] perseus
 - [x] proiel
 - [x] udante


`kupariha/trankit/MM_ MERG_` 5 + 4 = 9 kpl

#### Stanza

MM
stanza
5 plain tb's
 - [x] ittb
 - [x] llct
 - [x] perseus
 - [x] proiel  
 - [x] udante  

```bash
[kupariha@puhti-login14 latin-stanza]$ mv MM_ITTB_slurm/Stanza_ittb_output.conllu ../Latin-Parsing/Results/conllu_files/MM_Stanza_ittb.conllu
[kupariha@puhti-login14 latin-stanza]$ mv MM_LLCT/Stanza_llct_output.conllu ../Latin-Parsing/Results/conllu_files/MM_Stanza_llct.conllu
[kupariha@puhti-login14 latin-stanza]$ mv MM_Perseus-stanza/Stanza_perseus_output.conllu ../Latin-Parsing/Results/conllu_files/MM_Stanza_perseus.conllu
[kupariha@puhti-login14 latin-stanza]$ mv MM_PROIEL-stanza/Stanza_Proiel_output.conllu ../Latin-Parsing/Results/conllu_files/MM_Stanza_proiel.conllu
[kupariha@puhti-login14 latin-stanza]$ cp ../../ehenriks/latin-stanza/Stanza_udante_output.conllu ../Latin-Parsing/Results/conllu_files/MM_Stanza_udante.conllu
```

2 merged: Classical and Mega

Classical  
- [x] perseus  
- [x] proiel  

Mega
 - [x] ittb
 - [x] llct
 - [x] perseus
 - [x] proiel  
 - [x] udante  



```
ehenriks/latin-stanza/Stanza_udante_output.conllu
kupariha/latin-stanza/MM_ITTB LLCT Perseus PROIEL
      --,,--         /MM_classical ja megawombatti
```
7 kpl

**Hunt and rename** the already done files(, or make new ones?)

Renaming in bash:

```bash
# make a backup of the directory
[kupariha@puhti-login11 Results]$ cp -a . ../Results.vara/
# option -n 
    # Do not make any changes.
[kupariha@puhti-login11 Results]$ rename -nv test_output MM_Trankit-Mega *.conllu
`test_output_ittb.conllu' -> `MM_Trankit-Mega_ittb.conllu'
`test_output_llct.conllu' -> `MM_Trankit-Mega_llct.conllu'
`test_output_perseus.conllu' -> `MM_Trankit-Mega_perseus.conllu'
`test_output_proiel.conllu' -> `MM_Trankit-Mega_proiel.conllu'
`test_output_UDante.conllu' -> `MM_Trankit-Mega_UDante.conllu'
```

## Use Trankit on the remaining cases

--> trankit/use_trankit.py

Get the input conllu from Latin-Variability

`cat > test.conllu`  
**Or** just read the conllu straight to perl.

`conllu_to_text.pl > test.txt`

Does trankit need the line breaks removed? Probably.  
– It does something without them.

**Compare:**  
MM_Trankit-Classical_perseus_linebreaks-replaced-w-space.conllu  
MM_Trankit-Classical_perseus_slurm.conllu

There are interesting differences in mwt's + some in tokenization and everywhere.

dict2conllu() / trankit2conllu() ?  
trankit first!


## Fix md tables

- Replace `+` with `|`
- Or perhaps `--+--` with `--|--` is safer?

**But:** Does this help taking the data to tables? tsv, excel, ... ?
