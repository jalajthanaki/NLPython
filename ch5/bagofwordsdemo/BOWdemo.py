from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

ngram_vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(2, 2), min_df=1)
# List is noumber of document here there are two document and each has only one word
# we are considering n_gram = 2 on chapracter unit leve
counts = ngram_vectorizer.fit_transform(['words', 'wprds'])
# this check weather the given word character is present in the above teo word which are documents here.
ngram_vectorizer.get_feature_names() == ([' w', 'ds', 'or', 'pr', 'rd', 's ', 'wo', 'wp'])
print(counts.toarray().astype(int))
