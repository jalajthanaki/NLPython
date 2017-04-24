from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')


def generateparsetree(sentnece):
    text = (sentnece)
    output = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    parsetree = output['sentences'][0]['parse']
    return parsetree

def patternextractor(sentence, parsetree):
    tree = generateparsetree(sentence)


def run(sentence):
    patternextractor(sentence)

if __name__ == "__main__":
    run('He drink tomato soup in the morning')
