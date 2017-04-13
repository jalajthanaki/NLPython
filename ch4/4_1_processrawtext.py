import nltk
from nltk.corpus import gutenberg as cg
from nltk.tokenize import sent_tokenize as st


# Get raw data form file
def fileread():
    file_contents = open("/home/jalaj/PycharmProjects/NLPython/NLPython/data/rawtextcorpus.txt", "r").read()
    # print file_contents
    return file_contents
# assign text data to local variable
def localtextvalue():
    text = """ one paragraph, of 100-250 words, which summarizes the purpose, methods, results and conclusions of the paper.
    It is not easy to include all this information in just a few words. Start by writing a summary that includes whatever you think is important,
    and then gradually prune it down to size by removing unnecessary words, while still retaini ng the necessary concepts.
    Don't use abbreviations or citations in the abstract. It should be able to stand alone without any footnotes. Fig 1.1.1 shows below."""
    # print text
    return text

# Use NLTK corpus which we seen in chapter 2 as well
def readcorpus():
    raw_content_cg = cg.raw("burgess-busterbrown.txt")
    # print raw_content_cg[0:1000]
    return raw_content_cg[0:1000]

if __name__ == "__main__":
    print ""
    print "----------Output from Raw Text file-----------"
    print ""
    filecontentdetails = fileread()
    print filecontentdetails
    # sentence tokenizer
    st_list_rawfile = st(filecontentdetails)
    print len(st_list_rawfile)

    print ""
    print "-------Output from assigned variable-------"
    print ""
    localveriabledata = localtextvalue()
    print localveriabledata
    # sentence tokenizer
    st_list_local = st(localveriabledata)
    print len(st_list_local)
    print st_list_local

    print ""
    print "-------Output Corpus data--------------"
    print ""
    fromcorpusdata = readcorpus()
    print fromcorpusdata
    # sentence tokenizer
    st_list_corpus = st(fromcorpusdata)
    print len(st_list_corpus)
