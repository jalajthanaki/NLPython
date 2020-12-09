import re

def searchvsmatch():
    line = "I love animals.";

    matchObj = re.match(r'animals', line, re.M | re.I)
    if matchObj:
        print("match: ", matchObj.group())
    else:
        print("No match!!")

    searchObj = re.search(r'animals', line, re.M | re.I)
    if searchObj:
        print("search: ", searchObj.group())
    else:
        print("Nothing found!!")


def basicregex():
    line = "This is test sentence and test sentence is also a sentence."
    contactInfo = 'Doe, John: 1111-1212'
    print("-----------Output of re.findall()--------")
    # re.findall() finds all occurences of sentence from line variable.
    findallobj = re.findall(r'sentence', line)
    print(findallobj)

    # re.search() and group wise extraction
    groupwiseobj = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
    print("\n")
    print("-----------Output of Groups--------")
    print("1st group ------- " + groupwiseobj.group(1))
    print("2nd group ------- " + groupwiseobj.group(2))
    print("3rd group ------- " + groupwiseobj.group(3))

    # re.sub() replace string
    phone = "1111-2222-3333 # This is Phone Number"

    # Delete Python-style comments
    num = re.sub(r'#.*$', "", phone)
    print("\n")
    print("-----------Output of re.sub()--------")
    print("Phone Num : ", num)

    # Replace John to Peter  in contactInfo
    contactInforevised = re.sub(r'John', "Peter", contactInfo)
    print("Revised contactINFO : ", contactInforevised)


def advanceregex():
    text = "I play on playground. It is the best ground."

    positivelookaheadobjpattern = re.findall(r'play(?=ground)',text,re.M | re.I)
    print("Positive lookahead: " + str(positivelookaheadobjpattern))
    positivelookaheadobj = re.search(r'play(?=ground)',text,re.M | re.I)
    print("Positive lookahead character index: "+ str(positivelookaheadobj.span()))

    possitivelookbehindobjpattern = re.findall(r'(?<=play)ground',text,re.M | re.I)
    print("Positive lookbehind: " + str(possitivelookbehindobjpattern))
    possitivelookbehindobj = re.search(r'(?<=play)ground',text,re.M | re.I)
    print("Positive lookbehind character index: " + str(possitivelookbehindobj.span()))

    negativelookaheadobjpattern = re.findall(r'play(?!ground)', text, re.M | re.I)
    print("Negative lookahead: " + str(negativelookaheadobjpattern))
    negativelookaheadobj = re.search(r'play(?!ground)', text, re.M | re.I)
    print("Negative lookahead character index: " + str(negativelookaheadobj.span()))

    negativelookbehindobjpattern = re.findall(r'(?<!play)ground', text, re.M | re.I)
    print("negative lookbehind: " + str(negativelookbehindobjpattern))
    negativelookbehindobj = re.search(r'(?<!play)ground', text, re.M | re.I)
    print("Negative lookbehind character index: " + str(negativelookbehindobj.span()))

if __name__ == "__main__":
    print("\n")
    print("---------re.match() vs re.search()")
    searchvsmatch()
    print("\n")
    basicregex()
    print("\n")
    advanceregex()