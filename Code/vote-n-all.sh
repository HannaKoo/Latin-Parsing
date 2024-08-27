#!/usr/bin/env bash

rdir=Results/conllu_files
wdir=Results/conllu_files/voted_extended

for treebank in llct
# for treebank in ittb perseus proiel udante
do
    py Code/vote-n-extend.py \
    $rdir/vote_${treebank}/MM_Trankit*.conllu \
    $rdir/vote_${treebank}/MM_Stanza*.conllu \
    $rdir/vote_${treebank}/MM_ud*.conllu \
    --output $wdir/${treebank}.hyper.conllu
done
# for others:
    # $rdir/vote_${treebank}/MM_UD*.conllu \
