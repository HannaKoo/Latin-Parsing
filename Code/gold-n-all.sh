#!/usr/bin/env bash

rdir=Results/conllu_files
wdir=Results/conllu_files/gold_extended
# golddir=../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks
golddir=../../Latin-variability/morpho_harmonization/morpho-harmonized-treebanks  # puhti

mkdir -p $wdir

# Puhti: Run module load python-data to get Python 3.10!
for treebank in CIRCSE ITTB LLCT Perseus PROIEL UDante
do

    MM=MM-
    UD=UD
    if [ $treebank == LLCT ]
    then
        UD=ud  # LLCT udtagger file name has 'ud' instead of 'UD'
    fi

    if [ $treebank == CIRCSE ]
    then
        golddir=../..
        MM=""
    fi

    python3 Code/gold-extend.py \
    $rdir/vote_${treebank,,}/MM_Trankit*.conllu \
    $rdir/vote_${treebank,,}/MM_Stanza*.conllu \
    $rdir/vote_${treebank,,}/MM_${UD}*.conllu \
    --gold ${golddir}/UD_Latin-${treebank}/${MM}la_${treebank,,}-ud-test.conllu \
    --output $wdir/${treebank}.hypergold.conllu
done

# UD_Latin-CIRCSE/la_circse-ud-test.conllu
