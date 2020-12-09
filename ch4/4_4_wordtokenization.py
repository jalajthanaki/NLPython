from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

def wordtokenization():
    content = """Stemming is funnier than a bummer says the sushi loving computer scientist.
    She really wants to buy cars. She told me angrily. It is better for you.
    Man is walking. We are meeting tomorrow. You really don't know..!"""
    print(word_tokenize(content))

def wordlemmatization():
    wordlemma = WordNetLemmatizer()
    print(wordlemma.lemmatize('cars'))
    print(wordlemma.lemmatize('walking',pos='v'))
    print(wordlemma.lemmatize('meeting',pos='n'))
    print(wordlemma.lemmatize('meeting',pos='v'))
    print(wordlemma.lemmatize('better',pos='a'))

def wordlowercase():
    text= "I am a person. Do you know what is time now?"
    print(text.lower())

if __name__ =="__main__":
    wordtokenization()
    print("\n")
    print("----------Word Lemmatization----------")
    wordlemmatization()
    print("\n")
    print("----------converting data to lower case ----------")
    wordlowercase()