#!/usr/bin/env bash

rdir=Results/conllu_files
wdir=Results/conllu_files/gold_extended
# golddir=../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks
golddir=../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks  # puhti

mkdir -p $wdir

# for treebank in LLCT
# for treebank in ITTB Perseus PROIEL UDante
for treebank in PROIEL UDante
do
    # Puhti: Run module load python-data to get Python 3.10!
    python Code/gold-extend.py \
    $rdir/vote_${treebank,,}/MM_Trankit*.conllu \
    $rdir/vote_${treebank,,}/MM_Stanza*.conllu \
    $rdir/vote_${treebank,,}/MM_UD*.conllu \
    --gold ${golddir}/UD_Latin-${treebank}/MM-la_${treebank,,}-ud-test.conllu \
    --output $wdir/${treebank}.hypergold.conllu
done
    # $rdir/vote_${treebank,,}/MM_ud*.conllu \
# for others:
# ud for llct, UD for others
