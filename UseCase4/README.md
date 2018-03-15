# Use Case: Aspect Term Exctractor

#### Description
Companies that provide services or products to their customers would like to know which aspects of their products are relevant to their customers. This knowledge will help to improve their products in the future. Are people talking mostly about the quality of the food, the price of an item or the battery life of a computer? All those terms are what we call "aspect terms".

This task can be solved using an Aspect Term Extractor. An ATE is a model that extracts the aspect terms from a review, i.e. for each word of one review, your model should predict if the word is an aspect term or not. Terms may consist of multiple words.

#### General Notes
This notebook addresses the following 3 topics:

- The features extraction process: What is the intuition behind your method, which features are the most important.
- The algorithm you selected (we ask you to explore at least 2 different algorithms)
- The metric that you used for quantifying the performance of your model

We use the term 'predict' and 'extract' interchangably.

#### Dependencies

In the process of creating this notebook, the following libraries were used:

seaborn
numpy
pandas
matplotlib
scikit-learn
sklearn-crfsuite


#### References
- https://www.aclweb.org/anthology/S/S14/S14-2038.pdf
- https://www.thinkmind.org/download.php?articleid=data_analytics_2017_5_20_60030
- http://nlpforhackers.io/training-pos-tagger/
- http://www.albertauyeung.com/post/python-sequence-labelling-with-crf/
