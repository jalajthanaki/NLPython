from gensim import models
w = models.Word2Vec.load_word2vec_format('/home/jalaj/Downloads/GoogleNews-vectors-negative300.bin', binary=True)
if 'the' in w.wv.vocab:
    print("Vector for word 'the' \n")
    print(w.wv['the'])
else:
    print("Vocabulary doesn't include word 'the'\n")
if 'a' in w.wv.vocab:
    print("Vector for word 'a' \n")
    print(w.wv['a'])
else:
    print("Vocabulary doesn't include word 'a'\n")