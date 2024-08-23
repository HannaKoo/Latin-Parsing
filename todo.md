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

TODO: more of these later. ... DONE.

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

##### 4 merged:  

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

udtagger: 5 kpl


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


## Make eval tables

`eval_conllu_files.py` works!

Now it writes the native eval `--+--`

Should it write `|`-replaced .md or tsv or what? The `+` is at least easy to compare to the default output.

### Notes

linebreaks(slurm) vs nolinebreaks (MM_Trankit_Classical_perseus): No real difference in numbers, within 1 %.

Replace `#...` lines:  
`#.*\n`  
perseus 1720 removed

ittb 4256 removed

llct 1776 removed

udante 908 removed

(proiel done earlier).


CIRCSE
4398 removed

ITTB_ittb 4256 removed

LLCT_llct 1776 removed

PROIEL_proiel 2434 removed

UDante_udante 908 removed


## Fix md tables

- Replace `+` with `|`
- Or perhaps `--+--` with `--|--` is safer?

**But:** Does this help taking the data to tables? tsv, excel, LaTeX,  ... ?


## Vote

- mkdir conllu_files/vote_ittb ... vote_udante/  
- mv Trankit Stanza_pretokenized_fedback udtaggerCustom

#### feedback.py  

copy mwt and `# text =` back to stanza_pretokenized

Nono! Trankit has mwt, Stanza has `# text =` !

---------------------------------------------------

And, udtagger has **different sentence tokenization**! Custom_proiel has 
15379 lines, Trankit-Mega_proiel_nolinebreaks has 15329 lines. So 
50 more sentences are split in udtagger conllu? 
- No, there are differences both ways, 50 is netto.

Stanza-Classical_proiel_pretokenized-Trankit `# lines` removed has 15320 
lines!
- This is due to the missing mwt lines, 9 kpl.

Perseus also has similar differences in sentence tokenization.

**And:**

What's this **primum cessit** (perseus udtagger, line 152), it is split in Trankit-Mega_perseus_nolinebreaks


```
1	Ut	Ut	SCONJ	c--------	_	2	mark	_	_
2	primum cessit	primum cessit	ADV	v3spia---	_	9	advcl	_	_
3	furor	furor	NOUN	n-s---mn-	Case=Nom|Gender=Masc|Number=Sing	2	nsubj	_	_
4	et	et	CCONJ	c--------	_	7	cc	_	_
```

line 224:
```
11	ad aethera	ad aethera	ADP	n-p---na-	_	9	obj	_	_
12	virtus	virtus	NOUN	n-s---fn-	Case=Nom|Gender=Fem|Number=Sing	10	nsubj	_	_
```

line 319 has a mwt that is not in Trankit-Mega:
```
6	,	,	PUNCT	u--------	_	10	punct	_	_
7-8	nec	_	_	_	_	_	_	_	_
7	ne	ne	ADV	d--------	_	10	advmod	_	_
8	c	que	CCONJ	c--------	_	10	cc	_	_
9	duro	durus	ADJ	a-s---na-	Case=Abl|Gender=Neut|Number=Sing	12	amod	_	_
```
ditto l. 527

556:
```
8	fuso crateres	fuso crateres	VERB	n-p---ma-	Aspect=Perf|Case=Abl|Gender=Masc|Number=Sing|VerbForm=Part|Voice=Pass	4	conj	_	_
9	olivo	olivo	ADJ	n-s---nb-	Case=Abl|Gender=Neut|Number=Sing	2	obl	_	_
10	.	.	PUNCT	u--------	_	2	punct	_	_
```

udtagger 12096 lines vs Trankit-Mega 11995 lines

**It matches** MM_Trankit_perseus_test_output_nolinebreaks.conllu **!**

-----------------------------------------------------------

`test_vote/` includes 71 lines from the beginning of files plus a sentence towards the end with some words where `pos`s disagree completely, eg. contractarum.

Tokenization is same on these.


### Fix missing empty lines regex:

```
\n1\t  
\n\n1\t
```

### Problems with mwt, probably, 

at least when:
```
1-2 Nonni
 <--- Will enter an empty line here.
1 No
2 Niin
```

### Find all mwt with:

`\n[0-9]*-[0-9]`


## CIRCSE

Use all Stanza models on CIRCSE – Classical, Perseus, PROIEL at least.

## CIRCSEpunkt

Add `.` at the end of every sentence. Write to a txt file.

Run models on the txt.

Remove the `.` from the resulting conllus:  
`[0-9]*\t\..*\n`

MM_Stanza-classical_slurm_circsepunkt.conllu 1263 removed

Same number from the others, of course.

### eval.py not working on these:

Kun pisteet poistaa conlluista niin sinne jää numerointiin aukkoja aina kun piste on jäänyt lauseen keskelle. eval.py kosahtaa siihen.

Pitää varmaan tehdä pisteellinen GS. Mutta sekin on vaikee... Tai sitten ei.

Punkt line looks like this:  
`[0-9]*	\.	\.	PUNCT	u--------	_	[0-9]*	punct	_	_`  
e.g.:  
`14  .   .   PUNCT   u--------   _   13  punct   _   _`  
Where to get the HEAD (13 in the example)?


# 2024-08-23 udtagger merged -> Vote

```bash
cd Results/conllu_files/
mkdir voted_udtagger-merge
python3 ../../Code/vote.py vote_ittb/MM_Trankit* vote_ittb/MM_Stanza* vote_ittb/MM_UD* --output voted_udtagger-merge/MM_voted_ittb.conllu
python3 ../../Code/vote.py vote_llct/MM_Trankit* vote_llct/MM_Stanza* vote_llct/MM_ud* --output voted_udtagger-merge/MM_voted_llct.conllu  # No merged!
treebank=perseus
echo $treebank 
python3 ../../Code/vote.py vote_$treebank/MM_Trankit* vote_$treebank/MM_Stanza* vote_$treebank/MM_UD* --output voted_udtagger-merge/MM_voted_$treebank.conllu
treebank=proiel
python3 ../../Code/vote.py vote_$treebank/MM_Trankit* vote_$treebank/MM_Stanza* vote_$treebank/MM_UD* --output voted_udtagger-merge/MM_voted_$treebank.conllu
treebank=udante
python3 ../../Code/vote.py vote_$treebank/MM_Trankit* vote_$treebank/MM_Stanza* vote_$treebank/MM_UD* --output voted_udtagger-merge/MM_voted_$treebank.conllu
```
