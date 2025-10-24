# This script give you idea how stemming has been placed by using NLTK library.
# It is part of morphological analysis
# Alternative NLTK-based implementation provided for morphological analysis

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
words = ["unexpected", "disagreement", "disagree", "agreement", "quirkiness", "canonical" "historical"]

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


def nltk_alternative_stem():
    porter = PorterStemmer()
    lancaster = LancasterStemmer()
    snowball = SnowballStemmer('english')
    
    print("\nDerivational Morphemes using NLTK (alternative to polyglot)")
    for w in words_derv:
        print("{:<20}{}".format(w, porter.stem(w)))
    
    print("\nInflectional Morphemes using NLTK (alternative to polyglot)")
    for w in word_infle:
        print("{:<20}{}".format(w, porter.stem(w)))
    
    print("\nComparison of NLTK stemmers (Porter, Lancaster, Snowball)")
    test_words = words_derv + word_infle
    print("{:<15} {:<15} {:<15} {:<15}".format("Word", "Porter", "Lancaster", "Snowball"))
    print("-" * 60)
    for word in test_words:
        print("{:<15} {:<15} {:<15} {:<15}".format(
            word,
            porter.stem(word),
            lancaster.stem(word),
            snowball.stem(word)
        ))


if __name__ == "__main__":
    stemmer_porter()
    nltk_alternative_stem()
