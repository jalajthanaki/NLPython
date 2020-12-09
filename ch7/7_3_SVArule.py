from pycorenlp import StanfordCoreNLP
from nltk.tree import Tree

nlp = StanfordCoreNLP('http://localhost:9000')


def rulelogic(sentnece):
    leaves_list = []
    text = (sentnece)

    output = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    parsetree = output['sentences'][0]['parse']
    #print parsetree
    for i in Tree.fromstring(parsetree).subtrees():
        if i.label() == 'PRP':
            #print i.leaves(), i.label()
            leaves_list.append(i.leaves())
        if i.label() == 'VBP' or i.label() == 'VBZ':
            #print i.leaves(), i.label()
            leaves_list.append(i.label())
    #print leaves_list
    if (any("We" in x for x in leaves_list) or any("I" in x for x in leaves_list) or any(
                    "You" in x for x in leaves_list) or any("They" in x for x in leaves_list)) and any("VBZ" in x for x in leaves_list):
        print("Alert: \nPlease check Subject and verb in the sentence.\nYou may have plural subject and singular verb. ")
    elif(any("He" in x for x in leaves_list) or any("She" in x for x in leaves_list) or any(
                    "It" in x for x in leaves_list)) and any("VBP" in x for x in leaves_list):
        print("Alert: \nPlease check subject and verb in the sentence.\n" \
              "You may have singular subject and plural verb.")
    else:
        print("You have correct sentence.")

if __name__ == "__main__":
    rulelogic('We know cooking.')
    # 'He drink tomato soup in the morning.'
    # 'We plays game online.
    # She know cooking.
