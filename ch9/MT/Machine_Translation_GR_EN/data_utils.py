# |------------------------------------------------|
# |Creates a dataset from raw text files           |
# |------------------------------------------------|
# |Dataset: OpenSubtitles                          |
# |Url: http://opus.lingfil.uu.se/OpenSubtitles.php| 
# |Creator: Nemanja Tomic                          |
# |------------------------------------------------|

import cPickle as pickle
from collections import Counter

def read_sentences(file_path):
	sentences = []

	with open(file_path, 'r') as reader:
		for s in reader:
			sentences.append(s.strip())

	return sentences

def create_dataset(en_sentences, de_sentences):

	en_vocab_dict = Counter(word.strip(',." ;:)(][?!') for sentence in en_sentences for word in sentence.split())
	de_vocab_dict = Counter(word.strip(',." ;:)(][?!') for sentence in de_sentences for word in sentence.split())

	en_vocab = map(lambda x: x[0], sorted(en_vocab_dict.items(), key = lambda x: -x[1]))
	de_vocab = map(lambda x: x[0], sorted(de_vocab_dict.items(), key = lambda x: -x[1]))

	en_vocab = en_vocab[:20000]
	de_vocab = de_vocab[:30000]

	start_idx = 2
	en_word2idx = dict([(word, idx+start_idx) for idx, word in enumerate(en_vocab)])
	en_word2idx['<ukn>'] = 0
	en_word2idx['<pad>'] = 1

	en_idx2word = dict([(idx, word) for word, idx in en_word2idx.iteritems()])


	start_idx = 4
	de_word2idx = dict([(word, idx+start_idx) for idx, word in enumerate(de_vocab)])
	de_word2idx['<ukn>'] = 0
	de_word2idx['<go>']  = 1
	de_word2idx['<eos>'] = 2
	de_word2idx['<pad>'] = 3

	de_idx2word = dict([(idx, word) for word, idx in de_word2idx.iteritems()])

	x = [[en_word2idx.get(word.strip(',." ;:)(][?!'), 0) for word in sentence.split()] for sentence in en_sentences]
	y = [[de_word2idx.get(word.strip(',." ;:)(][?!'), 0) for word in sentence.split()] for sentence in de_sentences]

	X = []
	Y = []
	for i in range(len(x)):
		n1 = len(x[i])
		n2 = len(y[i])
		n = n1 if n1 < n2 else n2 
		if abs(n1 - n2) <= 0.3 * n:
			if n1 <= 15 and n2 <= 15:
				X.append(x[i])
				Y.append(y[i])

	return X, Y, en_word2idx, en_idx2word, en_vocab, de_word2idx, de_idx2word, de_vocab

def save_dataset(file_path, obj):
	with open(file_path, 'wb') as f:
		pickle.dump(obj, f, -1)

def read_dataset(file_path):
	with open(file_path, 'rb') as f:
		return pickle.load(f)

def main():
	en_sentences = read_sentences('data/data.en')
	de_sentences = read_sentences('data/data.de')

	save_dataset('./data.pkl', create_dataset(en_sentences, de_sentences))

if __name__ == '__main__':
	main()