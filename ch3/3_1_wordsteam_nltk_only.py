#!/usr/bin/env python3
"""
Alternative version of wordsteam.py using only NLTK library.
This version avoids polyglot dependency issues and works reliably with Python 3.

This script demonstrates stemming using NLTK's Porter, Lancaster, and Snowball stemmers.
It is part of morphological analysis from Chapter 3.
"""

from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer

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
    """Demonstrate Porter Stemmer for derivational and inflectional morphemes."""
    port = PorterStemmer()
    print("\nDerivational Morphemes (Porter Stemmer)")
    print(" ".join([port.stem(i) for i in text6.split()]))
    print(" ".join([port.stem(i) for i in text7.split()]))
    print("\nInflectional Morphemes (Porter Stemmer)")
    print(" ".join([port.stem(i) for i in text8.split()]))
    print(" ".join([port.stem(i) for i in text9.split()]))
    print("\nSome examples (Porter Stemmer)")
    print(" ".join([port.stem(i) for i in word.split()]))
    print(" ".join([port.stem(i) for i in text.split()]))
    print(" ".join([port.stem(i) for i in text1.split()]))
    print(" ".join([port.stem(i) for i in text2.split()]))
    print(" ".join([port.stem(i) for i in text3.split()]))
    print(" ".join([port.stem(i) for i in text4.split()]))
    print(" ".join([port.stem(i) for i in text5.split()]))


def stemmer_lancaster():
    """Demonstrate Lancaster Stemmer (more aggressive than Porter)."""
    lanc = LancasterStemmer()
    print("\n" + "="*60)
    print("Lancaster Stemmer (More Aggressive)")
    print("="*60)
    print("\nDerivational Morphemes")
    for w in words_derv:
        print("{:<20}{}".format(w, lanc.stem(w)))
    print("\nInflectional Morphemes")
    for w in word_infle:
        print("{:<20}{}".format(w, lanc.stem(w)))
    print("\nSome examples")
    for w in words:
        print("{:<20}{}".format(w, lanc.stem(w)))


def stemmer_snowball():
    """Demonstrate Snowball Stemmer (improved Porter algorithm)."""
    snow = SnowballStemmer('english')
    print("\n" + "="*60)
    print("Snowball Stemmer (Improved Porter)")
    print("="*60)
    print("\nDerivational Morphemes")
    for w in words_derv:
        print("{:<20}{}".format(w, snow.stem(w)))
    print("\nInflectional Morphemes")
    for w in word_infle:
        print("{:<20}{}".format(w, snow.stem(w)))
    print("\nSome examples")
    for w in words:
        print("{:<20}{}".format(w, snow.stem(w)))


def compare_stemmers():
    """Compare all three stemmers side by side."""
    port = PorterStemmer()
    lanc = LancasterStemmer()
    snow = SnowballStemmer('english')
    
    print("\n" + "="*60)
    print("Stemmer Comparison")
    print("="*60)
    print("\n{:<20}{:<15}{:<15}{:<15}".format("Word", "Porter", "Lancaster", "Snowball"))
    print("-" * 60)
    
    all_words = words_derv + word_infle + words
    for w in all_words:
        print("{:<20}{:<15}{:<15}{:<15}".format(
            w, 
            port.stem(w), 
            lanc.stem(w), 
            snow.stem(w)
        ))


if __name__ == "__main__":
    print("="*60)
    print("Word Stemming Examples using NLTK")
    print("="*60)
    
    stemmer_porter()
    
    stemmer_lancaster()
    stemmer_snowball()
    
    compare_stemmers()
    
    print("\n" + "="*60)
    print("Note: This version uses only NLTK library.")
    print("For morpheme analysis similar to polyglot, consider using:")
    print("  - spaCy (modern, well-maintained)")
    print("  - stanza (Stanford NLP)")
    print("="*60)
