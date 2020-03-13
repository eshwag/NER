
# coding: utf-8

# In[2]:


class Features():
    
    '''
        Inputs:
        X :List of data containing [(word,pos_tag,lemmatized_word,label/tag) for each sentence]
        
        num_words : How many words (pre and post) to consider. Default = 1.
        
        -- example: --
        
        >> crf = Features(X = fin, num_words = 1)
        
        >> features,labels = crf.get
        
        >> features[1]
        
        Output:
        
            [{'bias': 1.0,
              'word.isupper': False,
              'word.islower': 'lalitha',
              'word.istitle': True,
              'word.isdigit': False,
              'word.isalpha': True,
              'pos_tag': 'PROPN',
              'Beg_Of_Sent': True,
              '+1.word.isupper': False,
              '+1.word.islower': 'has',
              '+1.word.istitle': False,
              '+1.word.isdigit': False,
              '+1.word.isalpha': True,
              '+1.pos_tag': 'VERB'},
             {'bias': 1.0,
              'word.isupper': False,
              'word.islower': 'has',
              'word.istitle': False,
              'word.isdigit': False,
              'word.isalpha': True,
              'pos_tag': 'VERB',
              '-1.word.isupper': False,
              '-1.word.islower': 'lalitha',
              '-1.word.istitle': True,
              '-1.word.isdigit': False,
              '-1.word.isalpha': True,
              '-1.pos_tag': 'PROPN',
              '+1.word.isupper': False,
              '+1.word.islower': 'iphone',
              '+1.word.istitle': False,
              '+1.word.isdigit': False,
              '+1.word.isalpha': True,
              '+1.pos_tag': 'NOUN'},
             {'bias': 1.0,
              'word.isupper': False,
              'word.islower': 'iphone',
              'word.istitle': False,
              'word.isdigit': False,
              'word.isalpha': True,
              'pos_tag': 'NOUN',
              '-1.word.isupper': False,
              '-1.word.islower': 'has',
              '-1.word.istitle': False,
              '-1.word.isdigit': False,
              '-1.word.isalpha': True,
              '-1.pos_tag': 'VERB',
              'End_Of_Sent': True}]
              
        >> label[1]
        
        Output:
        
        ['I', 'O', 'P']
        
        
        '''

    
    def __init__(self,X, num_words):
        
        self.X = X
        self.num_words = num_words
        
    @property    
    def get(self):
        '''
        returns : features and lables of data
        
        
        '''
        def word_features(sentence,position):
            
            if self.num_words == 2:
                
                # word 
                word = sentence[position][0]
                # parts of speech tag 
                pos_tag = sentence[position][1]

                features={

                    'bias': 1.0,

                    'word.isupper': word.isupper(),
                    'word.islower': word.lower(),
                    'word.istitle': word.istitle(),
                    'word.isdigit': word.isdigit(),
                    'word.isalpha': word.isalpha(),
                    'pos_tag': pos_tag,
                }

                # if it is not first word in sentence
                if position > 1:

                    # previous word 
                    word = sentence[position-1][0]
                    # previous word's parts of speech tag
                    pos_tag = sentence[position-1][1]
                    
                    # previous word 
                    word1 = sentence[position-2][0]
                    # previous word's parts of speech tag
                    pos_tag1 = sentence[position-2][1]
                    
                    
                    features.update({
                        '-1.word.isupper': word.isupper(),
                        '-1.word.islower': word.lower(),
                        '-1.word.istitle': word.istitle(),
                        '-1.word.isdigit': word.isdigit(),
                        '-1.word.isalpha': word.isalpha(),
                        '-1.pos_tag': pos_tag,
                        
                        '-2.word.isupper': word1.isupper(),
                        '-2.word.islower': word1.lower(),
                        '-2.word.istitle': word1.istitle(),
                        '-2.word.isdigit': word1.isdigit(),
                        '-2.word.isalpha': word1.isalpha(),
                        '-2.pos_tag': pos_tag1,



                    })
                    
                # if it is not first word in sentence

                elif position > 0:

                    # previous word 
                    word = sentence[position-1][0]
                    # previous word's parts of speech tag
                    pos_tag = sentence[position-1][1]

                    features.update({
                        '-1.word.isupper': word.isupper(),
                        '-1.word.islower': word.lower(),
                        '-1.word.istitle': word.istitle(),
                        '-1.word.isdigit': word.isdigit(),
                        '-1.word.isalpha': word.isalpha(),
                        '-1.pos_tag': pos_tag,



                    })

                else:
                    # word is at Beggining of sentence
                    features['Beg_Of_Sent'] = True


                # if it is not the last word in the sentence
                if position < len(sentence)-2 :

                    # previous word 
                    word = sentence[position+1][0]
                    # previous word's parts of speech tag
                    pos_tag = sentence[position+1][1]
                    
                    # previous word 
                    word1 = sentence[position+2][0]
                    # previous word's parts of speech tag
                    pos_tag1 = sentence[position+2][1]
                    
                    
                    features.update({
                        
                        '+1.word.isupper': word.isupper(),
                        '+1.word.islower': word.lower(),
                        '+1.word.istitle': word.istitle(),
                        '+1.word.isdigit': word.isdigit(),
                        '+1.word.isalpha': word.isalpha(),
                        '+1.pos_tag': pos_tag,
                        
                        '+2.word.isupper': word1.isupper(),
                        '+2.word.islower': word1.lower(),
                        '+2.word.istitle': word1.istitle(),
                        '+2.word.isdigit': word1.isdigit(),
                        '+2.word.isalpha': word1.isalpha(),
                        '+2.pos_tag': pos_tag1,
                        
                        })
                         
                        
                elif position < len(sentence) - 1 :

                    # next word
                    word = sentence[position+1][0]
                    # next word's parts of speech 
                    pos_tag = sentence[position+1][1]

                    features.update({
                        '+1.word.isupper': word.isupper(),
                        '+1.word.islower': word.lower(),
                        '+1.word.istitle': word.istitle(),
                        '+1.word.isdigit': word.isdigit(),
                        '+1.word.isalpha': word.isalpha(),
                        '+1.pos_tag': pos_tag,


                    })

                else:
                    # it is the last word in sentence
                    features['End_Of_Sent'] = True

                return features
            
            elif self.num_words == 1:
                # word 
                word = sentence[position][0]
                # parts of speech tag 
                pos_tag = sentence[position][1]

                features={

                    'bias': 1.0,

                    'word.isupper': word.isupper(),
                    'word.islower': word.lower(),
                    'word.istitle': word.istitle(),
                    'word.isdigit': word.isdigit(),
                    'word.isalpha': word.isalpha(),
                    'pos_tag': pos_tag,
                }

                # if it is not first word in sentence 
                if position > 0:

                    # previous word 
                    word = sentence[position-1][0]
                    # previous word's parts of speech tag
                    pos_tag = sentence[position-1][1]

                    features.update({
                        '-1.word.isupper': word.isupper(),
                        '-1.word.islower': word.lower(),
                        '-1.word.istitle': word.istitle(),
                        '-1.word.isdigit': word.isdigit(),
                        '-1.word.isalpha': word.isalpha(),
                        '-1.pos_tag': pos_tag,



                    })

                else:
                    # word is at Beggining of sentence
                    features['Beg_Of_Sent'] = True


                # if it is not the last word in the sentence 
                if position < len(sentence) - 1 :

                    # next word
                    word = sentence[position+1][0]
                    # next word's parts of speech 
                    pos_tag = sentence[position+1][1]

                    features.update({
                        '+1.word.isupper': word.isupper(),
                        '+1.word.islower': word.lower(),
                        '+1.word.istitle': word.istitle(),
                        '+1.word.isdigit': word.isdigit(),
                        '+1.word.isalpha': word.isalpha(),
                        '+1.pos_tag': pos_tag,


                    })

                else:
                    # it is the last word in sentence
                    features['End_Of_Sent'] = True

                return features
                

        def sent_features(sent):
            # from each sentence return list of word features
            return [word_features(sent,position) for position in range(len(sent))]

        def sent_labels(sent):
            # from each sentence return list of labels (tags)
            return [label for tok,pos,lem,label in sent]

        features = [sent_features(sent) for sent in self.X]

        labels = [sent_labels(sent) for sent in self.X]

        return features,labels

