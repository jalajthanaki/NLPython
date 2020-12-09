from nltk.corpus import stopwords

# there are two solution for the chaper 4 exerices 1

def readfileandremovestopword():
    file_contents = open("/home/jalaj/PycharmProjects/NLPython/NLPython/data/rawtextcorpus.txt", "r").read()
    words = file_contents.lower().split()
    stops = set(stopwords.words("english"))
    preprocessed_words = [w for w in words if not w in stops]
    print("")
    return (" ".join(preprocessed_words))


def fileloadandremovestopwords():
    processedword = []
    word_list = open("/home/jalaj/PycharmProjects/NLPython/NLPython/data/rawtextcorpus.txt", "r")
    stops = set(stopwords.words('english'))
    for line in word_list:
        for w in line.split():
            if w.lower() not in stops:
                processedword.append(w)
    return processedword

if __name__ == "__main__":
    print("---------------")
    print(readfileandremovestopword())
    print("\n")
    print("---------------")
    print("\n")
    print(fileloadandremovestopwords())