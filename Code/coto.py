# Read a conllu-file for pre-tokenization. 
# Take the word/token from the second column, and make a list of lists of sentences and tokens as in:
# [['Hello', '!'], ['I', 'am', 'ready', '!']]
# Start a new sentence when a bunch of lines begin with '#' or ' ' 
# Skip lines beginning with eg. 34-35 (enclitics) 
# 33	contraxerunt	_	_	_	_	_	_	_	_
# 34-35	illudque	_	_	_	_	_	_	_	_
# 34	illud	_	_	_	_	_	_	_	_
# 35	que	_	_	_	_	_	_	_	_
# 36	carnali	_	_	_	_	_	_	_	_
# BUG: A conllu file should have \n\n at the end, and then we get an empty []
# as the last "sentence".

import csv

def conllu_to_list(conllufilename):
    list = []
    sublist = []
    with open(conllufilename, 'r', newline='', encoding='utf8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if (not row) or (row[0][0] == '#'):  # empty or comment, start new sublist
                if sublist:  # Don't append empty list (when several comment/empty lines)
                    list.append(sublist)
                    sublist = []
            else:  # not comment or empty
                if not "-" in row[0]:  # Skip enclitics
                    sublist.append(row[1])
        if sublist: # to include the last sentence     
            list.append(sublist)
    return list


if __name__ == '__main__':
    conllufilename = "Data/GS_Hanna-Mari_tokenized.conllu"
    list = conllu_to_list(conllufilename)

    for thing in list:
        print()
        print(thing)
