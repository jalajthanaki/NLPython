# This script give you idea how stemming has been placed by using NLTK libraries.
# It is part of morphological analysis

from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

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


def alternative_stemmers():
    print("\n" + "="*60)
    print("Alternative Stemmers (Snowball and Lancaster)")
    print("="*60)
    
    snowball = SnowballStemmer("english")
    lancaster = LancasterStemmer()
    
    print("\nDerivational Morphemes using Snowball Stemmer")
    for w in words_derv:
        print("{:<20}{}".format(w, snowball.stem(w)))
    
    print("\nInflectional Morphemes using Snowball Stemmer")
    for w in word_infle:
        print("{:<20}{}".format(w, snowball.stem(w)))
    
    print("\nDerivational Morphemes using Lancaster Stemmer")
    for w in words_derv:
        print("{:<20}{}".format(w, lancaster.stem(w)))
    
    print("\nInflectional Morphemes using Lancaster Stemmer")
    for w in word_infle:
        print("{:<20}{}".format(w, lancaster.stem(w)))
    
    print("\nComparison of all three stemmers:")
    print("{:<20}{:<20}{:<20}{:<20}".format("Word", "Porter", "Snowball", "Lancaster"))
    print("-" * 80)
    port = PorterStemmer()
    test_words = ["happiness", "unkind", "dogs", "expected", "running", "flies"]
    for w in test_words:
        print("{:<20}{:<20}{:<20}{:<20}".format(
            w, 
            port.stem(w), 
            snowball.stem(w), 
            lancaster.stem(w)
        ))


if __name__ == "__main__":
    stemmer_porter()
    alternative_stemmers()
