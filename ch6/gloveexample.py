import itertools
from gensim.models.word2vec import Text8Corpus
from glove import Corpus, Glove

# for installing text8 corpus you should follow this commands

# wget http://mattmahoney.net/dc/text8.zip -P /tmp
# unzip text8.zip


sentences = list(itertools.islice(Text8Corpus('/tmp/text8'), None))
corpus = Corpus()
corpus.fit(sentences, window=10)
glove = Glove(no_components=100, learning_rate=0.05)
glove.fit(corpus.matrix, epochs=30, no_threads=4, verbose=True)
glove.add_dictionary(corpus.dictionary)

print(glove.most_similar('frog', number=10))
print(glove.most_similar('girl', number=10))
print(glove.most_similar('car', number=10))