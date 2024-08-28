#!/usr/bin/env bash

rdir=Results/conllu_files
wdir=Results/conllu_files/gold_extended
golddir=../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks

mkdir -p $wdir

# for treebank in llct
# for treebank in ITTB Perseus PROIEL UDante
for treebank in UDante
do
    py Code/gold-extend.py \
    $rdir/vote_${treebank,,}/MM_Trankit*.conllu \
    $rdir/vote_${treebank,,}/MM_Stanza*.conllu \
    $rdir/vote_${treebank,,}/MM_UD*.conllu \
    --gold ${golddir}/UD_Latin-${treebank}/MM-la_${treebank,,}-ud-test.conllu \
    --output $wdir/${treebank}.hypergold.conllu
done
# for others:
    # $rdir/vote_${treebank}/MM_ud*.conllu \
