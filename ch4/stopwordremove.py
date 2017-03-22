from nltk.corpus import stopwords


def stopwordlist():
    stopwordlist = stopwords.words('english')
    for s in stopwordlist:
        print s

def customizedstopwordremove():
    stop_words = set(["hi", "bye"])
    line = """hi this is foo. bye"""
    print " ".join(word for word in line.split() if word not in stop_words)

def stopwordremove():
    stop = set(stopwords.words('english'))
    sentence = "this is a test sentence. I am very happy today."
    print [i for i in sentence.lower().split() if i not in stop]
def fileloadandremovestopwords():
    word_list = open("xxx.y.txt", "r")
    stops = set(stopwords.words('english'))

    for line in word_list:
        for w in line.split():
            if w.lower() not in stops:
                print w


if __name__ == "__main__":
    stopwordlist()
    customizedstopwordremove()