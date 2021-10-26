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

Corpus = pd.read_csv('fichier_complet.csv',encoding="utf-16", error_bad_lines=False)
Corpus = Corpus.dropna()
Corpus[['polarity']] = Corpus[['polarity']].astype(int)
Corpus.sample(frac=1).reset_index(drop=True)
for index, words in Corpus.iterrows():
    if words[1] == -1:
        Corpus.at[index, 'polarity'] = 0
#===============================================
Corpus['comment'] = [entry.lower() for entry in Corpus['comment']]
# Step - c : Tokenization : In this each entry in the corpus will be broken into set of words
#Corpus['sentence']= [word_tokenize(entry) for entry in Corpus['sentence']]
#===============================================
Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(Corpus['comment'],Corpus['polarity'],test_size=0.2)
Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(Corpus['comment'])
Train_X_Tfidf = Tfidf_vect.transform(Train_X)
Test_X_Tfidf = Tfidf_vect.transform(Test_X)
#==============================================
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
from tkinter import *
#import ipynb as df
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from pandastable import Table, TableModel
import pandas as pd
import numpy as np
import googleapiclient.discovery
root = tkinter.Tk()
#link = 'list2.xlsx'

coms = []
results = []

#Corpus = pd.read_csv('training_neg.csv',encoding="utf-16", error_bad_lines=False)





def OpenDF():
    desc_dic = {}
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyBOBGXZBxLxvaTDtIwLz3DC8TNZl7BKZCc")
    
    s = X.get()
    request = youtube.commentThreads().list( part="snippet,replies", videoId = s )
    res = request.execute()
    response =  res
    
    for key in res.keys():
        ncoms =(res['pageInfo']['totalResults'])
    for i in range(0,ncoms):
        rpcom = (res['items'][i]['snippet']['topLevelComment'] ['snippet']['textOriginal'])
        
        coms.append(rpcom)
    Train_X_Tfidf = Tfidf_vect.transform(coms)
    global results
    results = SVM.predict(Train_X_Tfidf)
    print(len(results))
    #window = tkinter.Toplevel(root)
    #window.geometry('400x500')
    #f = Frame(window, dataframe=Corpus,showtoolbar=True, showstatusbar=True)
    #f.pack()
    #pt = Table(f)
    #pt.show()
    
   


Title = root.title( "Video Analyze ")
root.geometry('400x500')
root.configure(background='#8ab5ba')


label = Label(root, text ="veuillez entrer le lien de la video :",width=30, foreground="black",font=("Arial Bold", 14))
label.place(x=20,y=60)
label0 = Label(root, text ="Lien :", foreground="black",bg='#8ab5ba',font=("Arial", 8))
label0.place(x=20,y=120)
X= Entry(root,width=30)
X.place(x=60,y=120)
browse = Button(root, text="Scrape",width=13,bg="green", fg="white", command=OpenDF)
browse.place(x=280,y=116)

label1 = Label(root, text ="les données de la vidéo :",width=36, foreground="black",font=("Arial Bold", 12))
label1.place(x=20,y=160)
W= Entry(root,width=60)
W.place(x=20,y=200)


label2 = Label(root, text ="veuillez choisir le classifieur souhaiter :",width=36, foreground="black",font=("Arial Bold", 12))
label2.place(x=20,y=240)

v = IntVar()
v.set(0)
Radiobutton(root, text="DNN",padx=20, variable=v,value=0,bg='#8ab5ba').place(x=30,y=270)
Radiobutton(root, text="linéaire",padx=20, variable=v,value=1,bg='#8ab5ba').place(x=30,y=290)
Radiobutton(root, text="linéaire/DNN combiné ",padx=20, variable=v,value=2,bg='#8ab5ba').place(x=30,y=310)
Radiobutton(root, text="KNN",padx=20, variable=v,value=3,bg='#8ab5ba').place(x=30,y=330)
Radiobutton(root, text="SVM",padx=20, variable=v,value=4,bg='#8ab5ba').place(x=30,y=350)
Radiobutton(root, text="Naive bays",padx=20, variable=v,value=5,bg='#8ab5ba').place(x=30,y=370)


def resultat(a):
    if int(W.get()) > 0 :
        if float(O.get()) > 0 and float(O.get())<1:
            import pandas as pd
            w1 = int(W.get())#30 #window size (win)
            o1 = float(O.get())#0.2
            df = pd.read_excel(r''+text_var.get())
            records1 = df.values.tolist()
            key1 = [] #1 colomn : key (concat des colonnes des recordes) colomn 2: index de record convenable au key 
            for i in range(0,300):
                key1.append([])
                key1[i].append(records1[i][0][:3])
                key1[i].append(i)
                for j in range(1,4):
                    key1[i][0]=key1[i][0]+records1[i][j][:3] 

            key1.sort()
            if a==0:
                print('1')
                doublons =[] 
                b=0
                doublons,b=DCS(w1,o1,records1,key1)
                tkinter.messagebox.showinfo("Les doublons :","nombre de comparaison ="+str(b)+"\n les doublons sont :"+"-".join(str(v) for v in doublons))
            if a==1:
                doublons =[] 
                b=0
                print('2')
                doublons,b=DCSP(w1,o1,records1,key1)
                tkinter.messagebox.showinfo("Les doublons :","nombre de comparaison ="+str(b)+"\n les doublons sont :"+"-".join(str(v) for v in doublons))
            if a==2:
                doublons =[] 
                b=0
                print('3')
                doublons,b=EDCS(w1,o1,records1,key1)
                tkinter.messagebox.showinfo("Les doublons :","nombre de comparaison ="+str(b)+"\n les doublons sont :"+"-".join(str(v) for v in doublons))
            if a==3:
                doublons =[] 
                b=0
                print('4')
                doublons,b=EDCSP(w1,o1,records1,key1)
                tkinter.messagebox.showinfo("Les doublons :","nombre de comparaison ="+str(b)+"\n les doublons sont :"+"-".join(str(v) for v in doublons))
        else:
            tkinter.messagebox.showinfo("Erreur :","Le montant phi doit etre entre 1 et 0 !!")
    else:
        tkinter.messagebox.showinfo("Erreur :","La taille du fenetre de comparaison doit etre au moins 1 !!")
        

def res():
    elm_count0 = np.count_nonzero(results == 0)
    elm_count1 = np.count_nonzero(results == 1)
    print(len(results))
    pos = (elm_count1*100)/len(results)
    neg = (elm_count0*100)/len(results)
    tkinter.messagebox.showinfo("polarité de video :","nombre de commentaires positive ="+str(elm_count1)+"("+str(int(pos))+"%)\n nombre de commentaires negatives :"+str(elm_count0)+"("+str(int(neg))+"%).")
            
        
appliquer = Button(root, text="Appliquer",width=20,bg="blue", fg="white", command=lambda : res())
#appliquer = Button(root, text="Appliquer",width=20,bg="blue", fg="white", command=lambda : resultat(v.get()))
appliquer.place(x=120,y=410)
        
    
root.mainloop()