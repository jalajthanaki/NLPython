# Run this script with command line argument
# python sentimentanalysis_SVM.py /home/jalaj/PycharmProjects/NLPython/NLPython/ch8/sentimentanalysis/data  /home/jalaj/PycharmProjects/NLPython/NLPython/ch8/sentimentanalysis/data

import sys
import os
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

def usage():
    print("Usage:")
    print("python %s <data_dir>" % sys.argv[0])

if __name__ == '__main__':

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    data_dir = sys.argv[1]
    classes = ['pos', 'neg']

    # Read the data
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    for curr_class in classes:
        dirname = os.path.join(data_dir, curr_class)
        for fname in os.listdir(dirname):
            with open(os.path.join(dirname, fname), 'r') as f:
                content = f.read()
                if fname.startswith('cv9'):
                    test_data.append(content)
                    test_labels.append(curr_class)
                else:
                    train_data.append(content)
                    train_labels.append(curr_class)

    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)

    clf = MultinomialNB()
    t0 = time.time()
    clf.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction = clf.predict(test_vectors)


    t2 = time.time()
    time_train = t1-t0
    time_predict = t2-t1


    # Print results in a nice table
    print("Results for NaiveBayes (MultinomialNB) ")
    print("Training time: %fs; Prediction time: %fs" % (time_train, time_predict))
    print(classification_report(test_labels, prediction))
    print "Reviews Prediction"
    print prediction[10] + "----"+test_data[10]

    print "\nReviews Prediction"
    print prediction[100] + "----" + test_data[100]
