from nltk.corpus import stopwords


def stopwordlist():
    stopwordlist = stopwords.words('english')
    print("")
    print("------List of stop words-------")
    for s in stopwordlist:
        print(s)

def customizedstopwordremove():
    stop_words = set(["hi", "bye"])
    line = """hi this is foo. bye"""
    print("")
    print("--------Customized stopword removal---------")
    print(" ".join(word for word in line.split() if word not in stop_words))

def stopwordremove():
    stop = set(stopwords.words('english'))
    sentence = "this is a test sentence. I am very happy today."
    print("")
    print("--------Stop word removal from raw text---------")
    print(" ".join([i for i in sentence.lower().split() if i not in stop]))




if __name__ == "__main__":
    stopwordlist()
    customizedstopwordremove()
    stopwordremove()
