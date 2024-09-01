#!/usr/bin/env bash

mkdir -p Results/analyse

for treebank in circse ittb llct perseus proiel udante
do

# The udtagger file for llct is named differently (as it is not from the merged banks)
UD=UD
if [ $treebank == "llct" ]
then
    UD=ud
fi

python3 Code/analyse.py \
Results/conllu_files/vote_${treebank}/MM_Trankit*.conllu \
Results/conllu_files/vote_${treebank}/MM_Stanza*.conllu \
Results/conllu_files/vote_${treebank}/MM_${UD}*.conllu \
--output Results/analyse/analyse-${treebank}.txt

done
