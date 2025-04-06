# Latin-Parsing
Repository of all things necessary to optimize parsing tools for Latin

## Models will be added here 18th of November

(Trankit and Stanza models were actually added 6th of April 2025. And the Custom tagger models will follow later.)

Read the article: [Improving Latin Dependency Parsing by Combining Treebanks and Predictions](https://doi.org/10.18653/v1/2024.nlp4dh-1.21)

Download and use the models using the notebooks in [Models/GetModels/](Models/GetModels), they were written in [Google Colaboratory](https://colab.research.google.com), and should work there. But be careful, they might not all be tested. The Stanza-notebooks should run smoothly just by clicking *Run all*. But the Trankit-notebooks will probably require a kernel restart between the package installs and `import trankit`.

It seems the GitHub preview cannot show most of the notebooks, they should still work in Colab. Most of them were saved in Visual Studio Code, so you could try that also.

## Straight links to models:

These are just the model files, see the notebooks linked above to see examples of how to use them. **The notebooks download these automatically, so download these files only if you plan to use them somewhere else!**

### Trankit:
- https://a3s.fi/Latin-parsers-public/trankit-MM_ittb.zip
- https://a3s.fi/Latin-parsers-public/trankit-MM_llct.zip
- https://a3s.fi/Latin-parsers-public/trankit-MM_perseus.zip
- https://a3s.fi/Latin-parsers-public/trankit-MM_proiel.zip
- https://a3s.fi/Latin-parsers-public/trankit-MM_udante.zip
- https://a3s.fi/Latin-parsers-public/trankit-MERG_Classical.zip
- https://a3s.fi/Latin-parsers-public/trankit-MERG_Late-and-Christian.zip
- https://a3s.fi/Latin-parsers-public/trankit-MERG_Late-and-Medieval.zip
- https://a3s.fi/Latin-parsers-public/trankit-MERG_Five-Merged.zip
### Stanza:
- https://a3s.fi/Latin-parsers-public/stanza-MM_ittb.zip
- https://a3s.fi/Latin-parsers-public/stanza-MM_llct.zip
- https://a3s.fi/Latin-parsers-public/stanza-MM_perseus.zip
- https://a3s.fi/Latin-parsers-public/stanza-MM_proiel.zip
- https://a3s.fi/Latin-parsers-public/stanza-MM_udante.zip
- https://a3s.fi/Latin-parsers-public/stanza-MERG_Classical.zip
- https://a3s.fi/Latin-parsers-public/stanza-MERG_Five-Merged.zip
### Custom tagger:
- Will be added later.
