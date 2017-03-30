from nltk.stem import PorterStemmer

word = "unexpected"
text = "disagreement"
text1 = "disagree"
text2= "agreement"
text3 = "quirkiness"

def stemmer_porter():
    port = PorterStemmer()
    print " ".join([port.stem(i) for i in word.split()])
    print " ".join([port.stem(i) for i in text.split()])
    print " ".join([port.stem(i) for i in text1.split()])
    print " ".join([port.stem(i) for i in text2.split()])
    print " ".join([port.stem(i) for i in text3.split()])

if __name__ == "__main__":
    stemmer_porter()
