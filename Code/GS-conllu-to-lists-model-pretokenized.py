import coto


# Using the predicted file: 
# Error analysis for POS tags, need to find the lines where the is complete disagreement
# Need to find the lines where there is 100 % consensus

# Need to figure out how to use GS tokenized file in Trankit and Stanza

# Pretokenized input - Trankit instructions

# In some cases, we might already have a tokenized document and want to use this module. Here is how we can do it:

# To make the existing GS files into a "list of lists type of file"? Same as Stanza? 

#pretokenized_doc = [
#  ['Hello', '!'],
#  ['This', 'is', 'Trankit', '.']
#]

text = coto.conllu_to_list(tiedosto)

# Opening the conllu file (need to be done total of five times, the GS found in each separate folder, done at a later stage)

# Looking at the conllu file column number 2 i.e. FORM, and reading that into a list of lists

# Each sentence should be one list

# Each word in sentence added in turns

# Skipping all multi word token lines

# Senatus populusque Romanus

# [Senatus, populus, que, Romanus]

#tagged_doc = p.posdep(pretokenized_doc)



## https://trankit.readthedocs.io/en/latest/posdep.html

# Stanza instructions for pretokenized

# Start with Pretokenized Text

# In some cases, you might have already tokenized your text, and just want to use Stanza for downstream processing. In these cases, you can feed in pretokenized (and sentence split) text to the pipeline, as newline (\n) separated sentences, where each sentence is space separated tokens. Just set tokenize_pretokenized as True to bypass the neural tokenizer.

# The code below shows an example of bypassing the neural tokenizer:

# import stanza

# nlp = stanza.Pipeline(lang='en', processors='tokenize', tokenize_pretokenized=True)
# doc = nlp('This is token.ization done my way!\nSentence split, too!')
# for i, sentence in enumerate(doc.sentences):
#     print(f'====== Sentence {i+1} tokens =======')
#     print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')

# An alternative to passing in a string is to pass in a list of lists of strings, representing a document with sentences, each sentence a list of tokens.


# Need to find the lines where none of the results match the GS tag

