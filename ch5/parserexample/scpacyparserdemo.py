import spacy
from spacy.en import English
parser = English()
nlp = spacy.load('en')

def spacyparserdemo():
        example = u"The boy with the spotted dog quickly ran after the firetruck."
        parsedEx = parser(example)
        # shown as: original token, dependency tag, head word, left dependents, right dependents
        print "\n-----------original token, dependency tag, head word, left dependents, right dependents-------\n"
        for token in parsedEx:
            print(
            token.orth_, token.dep_, token.head.orth_, [t.orth_ for t in token.lefts], [t.orth_ for t in token.rights])

if __name__ == "__main__":
    spacyparserdemo()
