import re
import spacy
import nltk
import editdistance
import pandas as pd
from langdetect import detect
from googletrans import Translator
class tagger:
    def __init__(self,X):
        self.X = X
    def tag(self):
        # Removing all the special characters
        preprocessed_data = [' '.join(re.findall('[A-Za-z0-9]+',doc)) for doc in self.X]
        # loading spacy 
        nlp = spacy.load('en_core_web_sm')
        # pos tagging
        doc_tag = []
        for doc in preprocessed_data:
            # using spaCy's model
            sent = nlp(doc)
            tags = []
            for j in sent:
                # appending word, pos_tag, lemmatized word
                tags.append((j.text,j.pos_,j.lemma_))
            # appending tags for each document
            doc_tag.append(tags)
            # tagging all enities as others initally
            entity = []
            for sent in doc_tag:
                temp = []
                for tok in sent:
                    # appending O - Others
                    temp.append(tok+('O',))
                entity.append(temp)

        return entity
    
    def fit(self,X,y,tag): 
        self.y=y
        self.tag=tag
        a = len(y)
        b = len(tag)
        if  (a == b == 2) or (a == b == 1):
            final_tag = []
            for sent in X:
                nlp =spacy.load('en_core_web_sm')
                y1 =[nltk.tokenize.regexp_tokenize(i,'[a-zA-Z0-9]+') for i in y[0]]
                flat_list=[item for sublist in y1 for item in sublist]
                tags = []
                for tok,pos,lem,tagg in sent:
                    for t in range(len(flat_list)):
                        tt=max(len(tok),len(flat_list[t]))
                        edit=1-editdistance.eval(tok.lower(),flat_list[t])/tt
                        if tok.lower() == flat_list[t].lower() or edit > 0.34:
                            tagg = tag[0]
                    tags.append((tok,pos,lem,tagg))
                   # for each document append corresponding tag
                final_tag.append(tags)
                print("products tagged")
                # Tokenizing
            y2 = [nltk.tokenize.regexp_tokenize(i,'[a-zA-Z0-9]+') for i in y[1]]
            flat_list1= [item for sublist in y2 for item in sublist]       
            final_tag1 = []
            for sent in final_tag:
                tags = []
                for tok,pos,lem,tagg in sent:
                    for t in range(len(flat_list1)):
                        tt=max(len(tok),len(flat_list1[t]))
                        edit=1-editdistance.eval(tok.lower(),flat_list1[t])/tt
                        if tok.lower() == flat_list1[t].lower() or edit > 0.34:
                            tagg = 'I'
                    tags.append((tok,pos,lem,tagg))
                final_tag1.append(tags)
                print("issue tagged")
        elif (a > 2)|(b>2):
            raise Exception('Only two targets or two tags should be given')
            final_tag1 = [] 
        elif (a != b):
            raise Exception('Arguments passed incorrectly: Length Mismatch -(Targets and Tags)')

        return final_tag1

    if __name__ == '__main__':
        tagger

