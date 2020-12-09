from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')


def stnfordpostagdemofunction(text):
    output = nlp.annotate(text, properties={
        'annotators': 'pos',
        'outputFormat': 'json'
    })
    for s in output["sentences"]:
        for t in s["tokens"]:
            print(str(t["word"])+ " --- postag --"+ str(t["pos"]))


if __name__ == "__main__":
    stnfordpostagdemofunction("This is a car.")
