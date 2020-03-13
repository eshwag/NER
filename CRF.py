import pandas as pd
import time
import pickle
import re
from NER.generate_features import Features
from NER.tags import tagger
from sklearn_crfsuite import CRF
from sklearn_crfsuite.metrics import flat_classification_report,flat_accuracy_score
import spacy
import nltk
import editdistance
class ConditionalRandomField():
    
    def __init__(self,num_features):
        self.num_features = num_features
    
    def train(self,data,y,tag):
        self.data=data
        self.y=y
        self.tag=tag
        # Tagging each word in data to its corresponding tag
        a = tagger(data)
        taggdata=a.tag()
        return taggdata
    def train1(self,data,y,tag):
        #tagged_data = a.fit(a.tag(),y,tag)
        # Features as conditional random field accepts 
        feaobj= Features(data,self.num_features)
        x_train,y_train = feaobj.get
        print("labelled data")
        # Using conditional random field as features
        crf = CRF(algorithm='lbfgs',c1=0.1,c2=0.1,max_iterations=100,all_possible_transitions=False)
        print(crf)
        crf.fit(x_train,y_train)

        # Saving the model which is trained 
        filename = 'finalized_model.sav'
        pickle.dump(crf, open(filename, 'wb'))

        # Prediction on train
        pred = crf.predict(x_train)

        # printing classification report and Accuracy
        print('\n \n Prediction On Trained Data:\n \n',flat_classification_report(y_train,pred))
        print('Accuracy:',flat_accuracy_score(y_train,pred))
       

    def predict(self,data,y = None, tag = None):
        if (y != None) and (tag != None):
            # Tagging each word in data to its corresponding tag
            t = tagger(X = data)
            tagged_data_ = t.fit(X = t.tag(),y = y,tag = tag)
            
            # Generates features required for conditional random field
            f = Features(X = tagged_data_,num_words=self.num_features)
            x_test,y_test = f.get
            
            # Gets trained model from finalized_model.sav
            loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
            
            # prediction on test data 
            result = loaded_model.predict(x_test)
            
            #printing classification report and Accuracy
            print('\n\n Classification Report: \n',flat_classification_report(y_test,result))
            print('Accuracy:',flat_accuracy_score(y_test,result))

        elif (y == None) and (tag == None):
            # data is tagged with list of tuples (token, pos tag, leammatized word, other tag)
            t = tagger(X = data)
            tagged_data_ = t.tag()

            # Generates features required for conditional random field
            f = Features(X = tagged_data_,num_words= self.num_features)
            x_test,_ = f.get

            # Gets trained model from finalized_model.sav
            loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

            # prediction on test data 
            result = loaded_model.predict(x_test)

#         # tokenizing test data
#         final=pd.DataFrame()
#         final['description'] = [re.findall('[A-Za-z0-9]+',i) for i in data]
#         final['result']=result
#         def func(df,tag):
#             mainlist=[]
#             for i in range(len(df)):
#                 sublist=[]
#                 desc=df['result'].iloc[i]
#                 for j in range(len(desc)):
#                     if(tag==desc[j]):
#                         sublist.append(df['description'].iloc[i][j])
#                 if(len(sublist)!=0):
#                     mainlist.append(' '.join(sublist))
#                 else:
#                     mainlist.append("not assigned")
#             return mainlist
#         products=func(final,'P')
#         issues=func(final,'I')
#         finalresult=pd.DataFrame()
#         finalresult['Products']=products
#         finalresult['Issues']=issues

        return result
