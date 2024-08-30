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

### eval

kupariha/Latin-Parsing/Results/Evaluation_metrics/voted/eval_table.tsv

## Analyze vote results

Run `analyse.py` for Perseus (py for Windows...):
```bash
py Code\analyse.py Results\conllu_files\vote_perseus\MM_Trankit-Mega_perseus_nolinebreaks.conllu Results\conllu_files\vote_perseus\MM_Stanza-Classical_perseus_pretokenized-Trankit_comments-rm_fedback.conllu Results\conllu_files\vote_perseus\MM_UD-custom-classical_perseus_pretokenized-Trankit-mega.conllu --output Results\analyse-perseus.txt
```

# Insert predicted and gold UPOSes in voted conllu files for manual comparison

Multi word tokens (mwt) are skipped. The resulting files will only have the mwt header line, without analysis.
And the mwt sub tokens' analysis will not be there.

`gold-extend.py`, `gold-n-all.sh`

**Problem:** Eternal loop when Trankit has tokenized multiple words in one token, like 'quo posito' in ITTB.

What to do? Skip those lines. Seems to work, **but:**

Perseus: Trankit tokenization has split a word in the middle and made the latter part into an mwt, this again results in looping the gold file eternally!:
```conllu
1	Phoebus	Phoebus	PROPN	n-s---mn-	Case=Nom|Gender=Masc|Number=Sing	2	nsubj	_	_
2	amat	amo	VERB	v3spia---	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act	0	root	_	_
3	vis	vis	NOUN	n-s---fn-	Case=Nom|Gender=Fem|Number=Sing	2	nsubj	_	_
4-5	aeque	_	_	_	_	_	_	_	_
4	ae	ae	ADJ	a-s---fg-	Case=Gen|Gender=Fem|Number=Sing	6	xcomp	_	_
5	que	que	CCONJ	c--------	_	6	cc	_	_
6	cupit	cupio	VERB	v3sria---	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act	2	conj	_	_
```
Gold Standard:
```conllu
1	Phoebus	Phoebus	PROPN	n-s---mn-	Case=Nom|Gender=Masc|Number=Sing	2	nsubj	_	LId=Phoebus1
2	amat	amo	VERB	v3spia---	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act	0	root	_	LId=amo1|TraditionalMood=Indicativus|TraditionalTense=Praesens
3-4	visaeque	_	_	_	_	_	_	_	LId=que1
3	visae	video	VERB	v-srppfg-	Aspect=Perf|Case=Gen|Gender=Fem|Number=Sing|VerbForm=Part|Voice=Pass	2	nmod	_	_
4	que	que	CCONJ	c--------	_	3	cc	_	LId=que1
5	cupit	cupio	VERB	v3spia---	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act	2	conj	_	LId=cupio1|TraditionalMood=Indicativus|TraditionalTense=Praesens
```

PROIEL:  
Trankit:
```
1	HS	monetary	PROPN	Ne	_	0	root	_	_
2	C_	c_	CCONJ	Df	_	1	nsubj	_	_
3	X_X_X_	X_X_X_	X	yy	_	1	nsubj	_	_
4	I_	i_	CCONJ	C-	_	1	conj	_	_
5	I_	i_	CCONJ	C-	_	1	conj	_	_
6	I_	i_	CCONJ	C-	_	1	conj	_	_
7	I_	i_	CCONJ	Df	_	1	conj	_	_
8	ZZZ	ZZZ	ADJ	yy	_	1	conj	_	_

1	quid	quis	PRON	Pi	Case=Acc|Gender=Neut|Number=Sing|PronType=Int	0	root	_	_
```
Gold:
```
6	HS	monetary	ADV	Df	_	5	advmod	_	Ref=1.13.6
7	C_X_X_X_I_I_I_I_ZZZ	expression	ADJ	Df	_	6	amod	_	Ref=1.13.6
```

(**Plan B:** Put a maximum on the `while True` loop, but how to get back to the right place in the gold standard? Is there a gold.seek(somewhere) method?)

UDante:  
Trankit:
```
1	Gerardus	Gherardus	PROPN	Sms2n	Case=Nom|Gender=Masc|InflClass=IndEurO|NameType=Giv|Number=Sing	0	root	_	_
2	de	de	ADP	e	_	3	case	_	_
3	Brunel	Brunel	PROPN	Propn|n|-|s|-|-|-|n|b|-	Case=Acc|Gender=Masc|InflClass=IndEurX|NameType=Giv|Number=Sing	1	obl	_	_
4	:	:	PUNCT	Pu	_	7	punct	_	_
5	Si	si	SCONJ	cs	_	7	mark	_	_
6	·m	·m	ADV	co	_	7	obj	_	_
7	sentis	sentio	VERB	va4ips2	Aspect=Imp|InflClass=LatI|Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin|Voice=Act	13	advcl	_	_
```
Gold:
```
1	Gerardus	gerardus	PROPN	Sms2n	Case=Nom|Gender=Masc|InflClass=IndEurO|Number=Sing	0	root	_	_
2	de	de	ADP	e	_	3	case	_	_
3	Brunel	brunel	PROPN	Si	Foreign=Yes|InflClass=Ind|NameType=Geo	1	flat:name	_	SpaceAfter=No
4	:	:	PUNCT	Pu	_	5	punct	_	_
5	Si	si	X	zi	Foreign=Yes	1	orphan	_	SpaceAfter=No
6	·	·	PUNCT	Pu	_	7	punct	_	SpaceAfter=No
7	m	m	X	zi	Foreign=Yes	5	flat:foreign	_	_
8	sentis	sentis	X	zi	Foreign=Yes	5	flat:foreign	_	_
```

**Yes!** `gold.tell()` - `gold.seek()` works:

```
[kupariha@puhti-login15 Latin-Parsing]$ Code/gold-n-all.sh 
['Results/conllu_files/vote_perseus/MM_Trankit-Mega_perseus_nolinebreaks.conllu', 'Results/conllu_files/vote_perseus/MM_Stanza-Classical_perseus_pretokenized-Trankit_comments-rm_fedback.conllu', 'Results/conllu_files/vote_perseus/MM_UD-custom-classical_perseus_pretokenized-Trankit-mega.conllu']
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-Perseus/MM-la_perseus-ud-test.conllu
Aborting, cols[0][FORM] = vis
Aborting, cols[0][FORM] = caldice
Aborting, cols[0][FORM] = rebrius
Aborting, cols[0][FORM] = cumadmiratione
Aborting, cols[0][FORM] = ne
Aborting, cols[0][FORM] = copinum
[kupariha@puhti-login15 Latin-Parsing]$ 
```
```
[kupariha@puhti-login15 Latin-Parsing]$ Code/gold-n-all.sh 
['Results/conllu_files/vote_proiel/MM_Trankit-Mega_proiel_nolinebreaks.conllu', 'Results/conllu_files/vote_proiel/MM_Stanza-PROIEL_proiel_pretokenized-Trankit_comments-rm_fedback.conllu', 'Results/conllu_files/vote_proiel/MM_UD-custom-megawombatti_memory_proiel_pretokenized-Trankit-mega.conllu']
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-PROIEL/MM-la_proiel-ud-test.conllu
Aborting, cols[0][FORM] = C_
Aborting, cols[0][FORM] = X_X_X_
Aborting, cols[0][FORM] = I_
Aborting, cols[0][FORM] = I_
Aborting, cols[0][FORM] = I_
Aborting, cols[0][FORM] = I_
Aborting, cols[0][FORM] = ZZZ
Aborting, cols[0][FORM] = ante
Aborting, cols[0][FORM] = cessiones
['Results/conllu_files/vote_udante/MM_Trankit-Mega_udante_nolinebreaks.conllu', 'Results/conllu_files/vote_udante/MM_Stanza-UDante_udante_pretokenized-Trankit_comments-rm_fedback.conllu', 'Results/conllu_files/vote_udante/MM_UD-custom-megawombatti_memory_udante_pretokenized-Trankit-mega.conllu']
../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks/UD_Latin-UDante/MM-la_udante-ud-test.conllu
Aborting, cols[0][FORM] = ·m
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = n
Aborting, cols[0][FORM] = d
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = l
Aborting, cols[0][FORM] = 'aigua
Aborting, cols[0][FORM] = d
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = t
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = o
Aborting, cols[0][FORM] = velle
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = l
Aborting, cols[0][FORM] = ch
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = L
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = fa·l
Aborting, cols[0][FORM] = d
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = l
Aborting, cols[0][FORM] = 'aigua
Aborting, cols[0][FORM] = d
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = d
Aborting, cols[0][FORM] = 'ombra
Aborting, cols[0][FORM] = ch
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = d
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = ch
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = m
Aborting, cols[0][FORM] = '
Aborting, cols[0][FORM] = ·m
[kupariha@puhti-login15 Latin-Parsing]$ 
```

## regex to find unanimous votes that go right/wrong

All voted the same, and were right:  
`([A-Z]+)\t[A-Z,]*\tallsame\t\1`

But how to find unanimous votes that go wrong? Can regex grouping backreferences have negation?
https://www.regular-expressions.info/refadv.html "Negative lookahead".

`([A-Z]+)\t\1,\1,\1\tallsame\t(?!\1)` seems to work.
https://stackoverflow.com/a/977316

- `([A-Z]+)`: non-empty, `+`, group of capital letters, eg. `ADJ`
- `\t\1,\1,\1`: a tab and the group repeated three times, separated with commas, eg. `ADJ,ADJ,ADJ`
- `\tallsame\t`: a tab, `allsame`, and a tab
- `(?!\1)`: the first group would be `\1`, `(?!)` is negative lookahead.

