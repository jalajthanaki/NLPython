import spacy
nlp = spacy.load('en')
doc = nlp(u'London is a big city in the United Kingdom.')
print "\n-------Example 1 ------\n"
for ent in doc.ents:
    print(ent.label_, ent.text)
    # GPE London
    # GPE United Kingdom
doc1 = nlp(u'While in France, Christine Lagarde discussed short-term stimulus efforts in a '
           u'recent interview on 5:00 P.M. with the Wall Street Journal')
print "\n-------Example 2 ------\n"
for ent1 in doc1.ents:
    print(ent1.label_, ent1.text)