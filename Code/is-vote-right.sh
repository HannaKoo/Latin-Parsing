#!/usr/bin/env bash

# Create tables of form:
# proiel	yesright	thatswrong
# allsame	13295	      132
# two2one	  463	      154
# evenvote	   15	       19

for file in Results/conllu_files/gold_extended/*.hypergold.conllu
do
    echo $file
    for vote in header allsame two2one evenvote
    do
        for correct in yesright thatswrong
        do
            if [ $vote == header ]
            then
                echo $correct
            else
                echo $vote
            fi
        done
    done
done
