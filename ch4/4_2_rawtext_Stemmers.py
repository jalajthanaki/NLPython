from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

text = """Stemming is funnier than a bummer says the sushi loving computer scientist.
She really wants to buy cars. She told me angrily.
It is better for you. Man is walking. We are meeting tomorrow."""


def stemmer_porter():
    port = PorterStemmer()
    print("\nStemmer")
    return " ".join([port.stem(i) for i in text.split()])

def lammatizer():
    wordnet_lemmatizer = WordNetLemmatizer()
    ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'
    # Pos = verb
    print("\nVerb lemma")
    print(" ".join([wordnet_lemmatizer.lemmatize(i,pos="v") for i in text.split()]))
    # Pos =  noun
    print("\nNoun lemma")
    print(" ".join([wordnet_lemmatizer.lemmatize(i,pos="n") for i in text.split()]))
    # Pos = Adjective
    print("\nAdjective lemma")
    print(" ".join([wordnet_lemmatizer.lemmatize(i, pos="a") for i in text.split()]))
    # Pos = satellite adjectives
    print("\nSatellite adjectives lemma")
    print(" ".join([wordnet_lemmatizer.lemmatize(i, pos="s") for i in text.split()]))
    print("\nAdverb lemma")
    # POS = Adverb
    print(" ".join([wordnet_lemmatizer.lemmatize(i, pos="r") for i in text.split()]))

if __name__ == "__main__":
    print(stemmer_porter())
    lammatizer()