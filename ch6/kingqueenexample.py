from gensim import models

w = models.Word2Vec.load_word2vec_format('/home/jalaj/Downloads/GoogleNews-vectors-negative300.bin', binary=True)
print('King - man + woman:')
print('')
print(w.wv.most_similar(positive=['woman', 'king'], negative=['man']))

print('Similarity between man and woman:')
print(w.similarity('woman', 'man'))
