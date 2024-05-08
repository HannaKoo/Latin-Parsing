# Parser article

## test-data conllus

#### File name format:  

TB version | Model | tokenization | TB: test/GS

**Done:**
- (Stanza_classical_Trankit_pre_proiel_output.conllu)  
  - (MM_Stanza-Classical_pretokenized-Trankit_Proiel.md)
- MM_Stanza-Classical_proiel_pretokenized-Trankit.conllu
  - MM_Stanza-Classical_proiel_pretokenized-Trankit.md

TODO: more of these later.

### w/o pretokenized:

#### Trankit

Line breaks have been removed from the inputs for all of these, why? There are no `# text`'s.

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

[ ] Classical  
- [x] perseus  
- [ ] proiel  

[ ] Lame 
 - [ ] ittb
 - [ ] llct
 - [ ] udante  
 - [ ] proiel  

[ ] Late 
 - [ ] ittb
 - [ ] llct
 - [/] udante  

[ ] Mega
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
2 merged: Classical and Mega

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
[kupariha@puhti-login11 Results]$ rename -nv test_output MM_Trankit-Mega *  
`test_output_ittb.conllu' -> `MM_Trankit-Mega_ittb.conllu'
`test_output_llct.conllu' -> `MM_Trankit-Mega_llct.conllu'
`test_output_perseus.conllu' -> `MM_Trankit-Mega_perseus.conllu'
`test_output_proiel.conllu' -> `MM_Trankit-Mega_proiel.conllu'
`test_output_UDante.conllu' -> `MM_Trankit-Mega_UDante.conllu'
[kupariha@puhti-login11 Results]$ 
```

## Fix md tables

- Replace `+` with `|`
- Or perhaps `--+--` with `--|--` is safer?

**But:** Does this help taking the data to tables? tsv, excel, ... ?
