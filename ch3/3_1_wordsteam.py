# This script give you idea how stemming has been placed by using NLTK library.
# It is part of morphological analysis

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk

word = "unexpected"
text = "disagreement"
text1 = "disagree"
text2 = "agreement"
text3 = "quirkiness"
text4 = "historical"
text5 = "canonical"
text6 = "happiness"
text7 = "unkind"
text8 = "dogs"
text9 = "expected"
words_derv = ["happiness", "unkind"]
word_infle = ["dogs", "expected"]
words = ["unexpected", "disagreement", "disagree", "agreement", "quirkiness", "canonical", "historical"]

def stemmer_porter():
    port = PorterStemmer()
    print("\nDerivational Morphemes")
    print(" ".join([port.stem(i) for i in text6.split()]))
    print(" ".join([port.stem(i) for i in text7.split()]))
    print("\nInflectional  Morphemes")
    print(" ".join([port.stem(i) for i in text8.split()]))
    print(" ".join([port.stem(i) for i in text9.split()]))
    print("\nSome examples")
    print(" ".join([port.stem(i) for i in word.split()]))
    print(" ".join([port.stem(i) for i in text.split()]))
    print(" ".join([port.stem(i) for i in text1.split()]))
    print(" ".join([port.stem(i) for i in text2.split()]))
    print(" ".join([port.stem(i) for i in text3.split()]))
    print(" ".join([port.stem(i) for i in text4.split()]))
    print(" ".join([port.stem(i) for i in text5.split()]))


def nltk_lemmatizer():
    """
    Alternative to polyglot using NLTK's WordNetLemmatizer.
    This demonstrates morphological analysis using lemmatization.
    """
    lemmatizer = WordNetLemmatizer()
    
    print("\nDerivational Morphemes using NLTK lemmatizer")
    for w in words_derv:
        noun_form = lemmatizer.lemmatize(w, pos='n')
        adj_form = lemmatizer.lemmatize(w, pos='a')
        verb_form = lemmatizer.lemmatize(w, pos='v')
        print("{:<20}Noun: {:<15} Adj: {:<15} Verb: {}".format(w, noun_form, adj_form, verb_form))
    
    print("\nInflectional Morphemes using NLTK lemmatizer")
    for w in word_infle:
        noun_form = lemmatizer.lemmatize(w, pos='n')
        verb_form = lemmatizer.lemmatize(w, pos='v')
        print("{:<20}Noun: {:<15} Verb: {}".format(w, noun_form, verb_form))
    
    print("\nSome Morphemes examples using NLTK lemmatizer")
    for w in words:
        noun_form = lemmatizer.lemmatize(w, pos='n')
        adj_form = lemmatizer.lemmatize(w, pos='a')
        verb_form = lemmatizer.lemmatize(w, pos='v')
        print("{:<20}Noun: {:<15} Adj: {:<15} Verb: {}".format(w, noun_form, adj_form, verb_form))


if __name__ == "__main__":
    stemmer_porter()
    nltk_lemmatizer()
