# This script is for generating parsing tree by using NLTK.
# We are using python wrapper for stanford CoreNLP called-"pycorenlp" to generate Parsing result for us.B06923_03_09
# NLTK gives us tree representation of stanford parser.
import nltk
from nltk import CFG
from nltk.tree import *
from pycorenlp import StanfordCoreNLP
from collections import defaultdict

# Part 1: Define a grammar and generate parse result using NLTK
def definegrammar_pasrereult():
    Grammar = nltk.CFG.fromstring(""" 
    S -> NP VP 
    PP -> P NP 
    NP -> Det N | Det N PP | 'I' 
    VP -> V NP | VP PP 
    Det -> 'an' | 'my' 
    N -> 'elephant' | 'pajamas' 
    V -> 'shot' 
    P -> 'in' 
    """)
    sent = "I shot an elephant".split()
    parser = nltk.ChartParser(Grammar)
    trees = parser.parse(sent)
    for tree in trees:
        print tree

# Part 2: Draw the parse tree
def draw_parser_tree():
    dp1 = Tree('dp', [Tree('d', ['the']), Tree('np', ['dog'])])
    dp2 = Tree('dp', [Tree('d', ['the']), Tree('np', ['cat'])])
    vp = Tree('vp', [Tree('v', ['chased']), dp2])
    tree = Tree('s', [dp1, vp])
    print(tree)
    print(tree.pformat_latex_qtree())
    tree.pretty_print()


# Part 3: Stanford parser wrapper library "pycorenlp"
# you need to install pycorenlp as well as you need to download stanford-corenlp-full-* from standford corenlp website.
def stanford_parsing_result():
    text =""" I shot an elephant. The dog chased the cat. School go to boy. """
    nlp = StanfordCoreNLP('http://localhost:9000')
    res = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    print(res['sentences'][0]['parse'])
    print(res['sentences'][2]['parse'])


if __name__ == "__main__":
    print "\n--------Parsing result as per defined grammar-------"
    definegrammar_pasrereult()
    print "\n--------Drawing Parse Tree-------"
    draw_parser_tree()
    print "\n--------Stanford Parser result------"
    stanford_parsing_result()
