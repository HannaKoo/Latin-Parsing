# Latin-Parsing
Repository of all things necessary to use state-of-the-art parsing tools for Latin

## Trankit and Stanza Models Added

(Trankit and Stanza models were added 6th of April 2025. And the Custom tagger models will follow later.)

Read the article: [Improving Latin Dependency Parsing by Combining Treebanks and Predictions](https://doi.org/10.18653/v1/2024.nlp4dh-1.21)

Published at the NLP4DH workshop at EMNLP Miami 2024

### Abstract
*This paper introduces new models designed to improve the morpho-syntactic parsing of the five largest Latin treebanks in the Universal Dependencies (UD) framework. First, using two state-of-the-art parsers, Trankit and Stanza, along with our custom UD tagger, we train new models on the five treebanks both individually and by combining them into novel merged datasets. We also test the models on the CIRCSE test set. In an additional experiment, we evaluate whether this set can be accurately tagged using the novel LASLA corpus (https://github.com/CIRCSE/LASLA). Second, we aim to improve the results by combining the predictions of different models through an atomic morphological feature voting system. The results of our two main experiments demonstrate significant improvements, particularly for the smaller treebanks, with LAS scores increasing by 16.10 and 11.85%-points for UDante and Perseus, respectively (Gamba and Zeman, 2023a). Additionally, the votingsystem for morphological features (FEATS) brings improvements, especially for the smaller Latin treebanks: Perseus 3.15% and CIRCSE 2.47%-points. Tagging the CIRCSE set with our custom model using the LASLA model improves POS 6.71 and FEATS 11.04%-points compared to our best-performing UD PROIEL model. Our results show that larger datasets and ensemble predictions can significantly improve performance.*

## Jupyter notebooks for easy download

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
