# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score

Corpus = pd.read_csv('training_neg.csv',encoding="utf-16", error_bad_lines=False)
Corpus = Corpus.dropna()
Corpus[['polarity']] = Corpus[['polarity']].astype(int)
Corpus.sample(frac=1).reset_index(drop=True)
for index, words in Corpus.iterrows():
    if words[1] == -1:
        Corpus.at[index, 'polarity'] = 0

Corpus['sentence'] = [entry.lower() for entry in Corpus['sentence']]
# Step - c : Tokenization : In this each entry in the corpus will be broken into set of words
#Corpus['sentence']= [word_tokenize(entry) for entry in Corpus['sentence']]

Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(Corpus['sentence'],Corpus['polarity'],test_size=0.2)
Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(Corpus['sentence'])
Train_X_Tfidf = Tfidf_vect.transform(Train_X)
Test_X_Tfidf = Tfidf_vect.transform(Test_X)

from sklearn.metrics import accuracy_score
# fit the training dataset on the NB classifier
Naive = naive_bayes.MultinomialNB()
Naive.fit(Train_X_Tfidf,Train_Y)
# predict the labels on validation dataset
predictions_NB = Naive.predict(Test_X_Tfidf)
# Use accuracy_score function to get the accuracy
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, Test_Y)*100)
#===============================================
# Classifier - Algorithm - SVM
# fit the training dataset on the classifier
SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(Train_X_Tfidf,Train_Y)
# predict the labels on validation dataset
predictions_SVM = SVM.predict(Test_X_Tfidf)
# Use accuracy_score function to get the accuracy
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, Test_Y)*100)
