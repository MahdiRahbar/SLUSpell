# -*- coding: utf-8 -*-

# Spell_Checker
# Developers: --
# License: -


import pickle as pkl
import os 
import re 
from collections import Counter 
import string 
from string import punctuation

import sys
# sys.path.append()
from .langSpec import * 

from numpy import log

_path = os.path.abspath(os.path.dirname(__file__))

class Dictionary:
    def __init__(self, lang, formality) -> None:
        self.lang = lang 
        self.formality = formality
        _path = os.path.abspath(os.path.dirname(__file__))
        self.main_dict_path = os.path.join(_path,'assets', 'dict', "{}-common.txt".format(self.lang))
        self.uni_dict_path = os.path.join(_path,'assets', 'dict', "{}_dict.pkl".format(self.lang))
        self.bi_dict_path = os.path.join(_path,'assets', 'dict', "{}_bi_dict.pkl".format(self.lang))
        # self.word_dict = self.read_dict_file()

    def read_dict_file(self):
        WORDS = Counter(self.read_dict(open(self.main_dict_path,encoding='utf-8').read()))
        return WORDS 

    def read_dict(self, text): 
        return re.findall(r'\w+', text.lower())

    def cal_proba(self, given_word):
        return self.word_dict[given_word]/ sum(self.word_dict.values())

    def open_prob_dict(self):
        with open(self.uni_dict_path, 'rb') as f:
            uni_dict = pkl.load(f)
        return uni_dict 

    def open_bi_prob_dict(self):
        with open(self.bi_dict_path, 'rb') as f:
            bi_dict = pkl.load(f)
        return bi_dict 


class WordCheck:
    def __init__(self, text,language, formality):
        text = text.replace('\u202f', ' ').replace('\xa0', ' ')
        self.text = text
        self.formality = formality
        self.language = language  
        self.dict_obj = Dictionary(self.language, self.formality)

        self.mis_counter = 0

        self.API_dict = {}
        self.lanObj = LangSpec(text, self.language)   
        self.word_list = self.words(text)
        self.text_obj = self.lanObj.call()
        self.text_chunks = self.text_obj.call()
        self.wordList_len = len(self.word_list)
        self.uni_dict, self.bi_dict = self.get_dict()

        self.letters = set(''.join(self.open_pickle(os.path.join(_path,'assets', 'dict', "{}_chars.pkl".format(self.language)))).lower() + '\'-')


    def open_pickle(self, path):
        with open(path, 'rb') as f:
            return pkl.load(f)
    
    def get_dict(self):
        uni_dict = self.dict_obj.open_prob_dict()
        bi_dict = self.dict_obj.open_bi_prob_dict()
        return uni_dict, bi_dict
     

    def cal_proba_alt(self, given_word):
        if given_word in self.alt_dict.keys():
            return self.alt_dict[given_word]/ sum(self.alt_dict.values())
        else:
            return self.word_dict[given_word]/ sum(self.word_dict.values())


    def words(self, text):
        '''
        Return a list of words + their starting and ending index

        @type  text: string
        @type  temp_list: list
        @return:  list of start_index, end_index, word.

        Previous important changes:
        # return re.findall(r'\w+', text.lower())
        '''
        self.word_list = []
        p = re.compile("\w+[-\']*\w*")  # \w*\'re|\w*\'nt|\w\'t|[iI]\'m|
        for m in p.finditer(text):
            self.word_list.append(m.group(0).lower())
        # self.word_list = [x.group() for x in re.finditer( "\w+[-\']*\w*", input_str)]
        return self.word_list

    
    def correction(self, word): 
        "Most probable spelling correction for word."
        # return max(self.candidates(word), key=self.dict_obj.cal_proba)
        new_candidates = list(self.candidates(word))

        word_index = self.word_list.index(word)
        candidate_list = []
        prob_list = []
        

        for i in range(len(new_candidates)):
            if (word_index+1)!=len(self.word_list):
                next_word_exist = (new_candidates[i], self.word_list[word_index+1]) in self.bi_dict.keys()
            else:
                next_word_exist = False

            if (word_index-1)>=0:
                previous_word_exist= (self.word_list[word_index-1], new_candidates[i]) in self.bi_dict.keys()
            else:
                previous_word_exist = False
            

            if (self.wordList_len > 1) and (word_index == 0 ) and (word_index+1!=len(self.word_list)) and next_word_exist:
                _prob = log(self.bi_dict[(new_candidates[i], self.word_list[word_index+1])]) #* log(self.uni_dict[new_candidates[i]])
                prob_list.append(_prob)
                candidate_list.append(new_candidates[i])
                # else:  It can consider the unigram probability
            
            elif (self.wordList_len > 1) and (word_index > 0 ) and previous_word_exist:
                _prob = log(self.bi_dict[(self.word_list[word_index-1],new_candidates[i])]) # * log(self.uni_dict[new_candidates[i]])
                prob_list.append(_prob)
                candidate_list.append(new_candidates[i])
            elif (self.wordList_len > 1) and next_word_exist:
                _prob = log(self.bi_dict[(new_candidates[i], self.word_list[word_index+1])]) # * log(self.uni_dict[new_candidates[i]])
                prob_list.append(_prob)
                candidate_list.append(new_candidates[i]) 
            elif (word_index == 0 ) and (new_candidates[i] in self.uni_dict.keys()):            
                prob_list.append(log(self.uni_dict[new_candidates[i]]))
                candidate_list.append(new_candidates[i])
            else:                
                prob_list.append(sys.float_info.epsilon)  # log(self.uni_dict[new_candidates[i]])
                candidate_list.append(new_candidates[i])            
        


        if len(candidate_list)>0:
            _, candidate_list = zip(*sorted(zip(prob_list, candidate_list),reverse= True))
            self.word_list[word_index] = candidate_list[0]
            if len(candidate_list)< 3:
                return candidate_list
            else:
                return candidate_list[:3]
        


    def candidates(self, word): 
        "Generate possible spelling corrections for word."
        return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word])

    def known(self, words): 
        "The subset of `words` that appear in the dictionary of self.word_dict."
        return set(w for w in words if w in self.uni_dict.keys())

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        letters    = self.letters
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word): 
        "All edits that are two edits away from `word`."
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))  
    
    def check_exceptions(self, word, position):
        if bool(re.match(r"(<+\d*\.*\d*\w*>*|\d+\.*[-+/*]*\d*|[%s]+|[\u263a-\U0001f645]+)"%punctuation, word)):
            return True 
        elif bool(re.match(r"([A-Z][A-Za-z]*)", word)) and position>0 :
            return True 
        elif bool(re.match(r"\\+w*", word)) and position>0 :
            return True
        elif bool(re.match(r"('s)\s*$", word)) and position>0 :
            return True 
        else:
            return False 

    def run_checker(self):  
        for i in range(len(self.text_chunks)):
            if self.check_exceptions(self.text_chunks[i]['word'],i):
                self.text_chunks[i]['correction_flag'] = False                      
                temp_word = re.sub(r"<", "&lt;", self.text_chunks[i]['word'])
                temp_word = re.sub(r">", "&gt;", temp_word)
                self.text_chunks[i]['word'] = temp_word
                self.text_chunks[i]['correct'] = self.text_chunks[i]['word']                
                self.text_chunks[i]['new_string'] = self.text_chunks[i]['word'] 

            elif (self.text_chunks[i]['check_flag']) == True and (self.text_obj.to_lower(self.text_chunks[i]['word']) not in self.uni_dict): 
                temp_word_list = list(self.correction(self.text_obj.to_lower(self.text_chunks[i]['word'])))            
                self.text_chunks[i]['correction_flag'] = True
                
                if self.text_chunks[i]['cap_flag']:
                    for j in range(len(temp_word_list)):
                        temp_word_list[j] = self.capitalize(temp_word_list[j])

                self.text_chunks[i]['correct'] = temp_word_list
                self.text_chunks[i]['id'] = i
                ## 
                self.text_chunks[i] = self.highliter(self.text_chunks[i])
                ##
            else: 
                self.text_chunks[i]['id'] = i

                if self.text_chunks[i]['cap_flag'] and  (self.text_chunks[i]['word'][0]!=self.text_chunks[i]['word'][0].upper()):
                    self.text_chunks[i]['correction_flag'] = True
                    self.text_chunks[i]['correct'] = [self.capitalize(self.text_chunks[i]['word'])]
                    self.text_chunks[i]= self.highliter(self.text_chunks[i])
                else:
                    self.text_chunks[i]['correction_flag'] = False
                    self.text_chunks[i]['correct'] = self.text_chunks[i]['word']                
                    self.text_chunks[i]['new_string'] = self.text_chunks[i]['word'] 

            
            self.API_dict[i] = self.jsonify(self.text_chunks[i]['new_string'],
                    self.text_chunks[i]['word'],
                    self.text_chunks[i]['correct'],
                    self.text_chunks[i]['correction_flag'],
                    self.text_chunks[i]['id'])


    
    def highliter(self, word):
        tagged_word =  "<span class='highlight highlight{}' onclick='show_correct({})' >".format(word['id'],word['id'])+\
                        "{}</span>".format(word['word'])   # onmouseout='hide_correct({})'
        
        word['new_string'] = tagged_word
        return word            

    def jsonify(self,new_string,word,correct,correction_flag,word_id):
        return {'new_string': new_string, 'word': word, 'correct':correct, 
                                     'correction_flag':correction_flag ,'id':word_id}

    def cap_begin(self, text):
        '''
        Return a list of characters that are supposed to be written in capital
            as well as their positional index.  

        @type  text: string
        @type  temp_list: list
        @return:  list of start_index, end_index, word.

        Previous important changes:
        # re.sub(r"(?:^|(?:[.!?]\s+))(.)",lambda m: m.group(0).upper(), text)
        '''    
        temp_list = []
        p = re.compile("(?:^|(?:[.!?]\s+))(.)")    
        for m in p.finditer(text):
            temp_list.append([m.group(0)['id'],"",m.start(), m.end(),False])
        return temp_list
    
    def capitalize(self, word): 
        if len(word)>1:
            return word[0].upper() + word[1:]
        else: 
            return word.upper()

    def call(self):
        self.run_checker()
        return self.API_dict

    
    def call_corrector(self, id, list_index):
        for i in range(len(self.text_chunks)):
            if self.text_chunks[i]['id'] == id: 
                self.text_chunks[i]['correction_flag'] = False
                self.text_chunks[i]['word'] = self.text_chunks[i]['correct'][list_index]
                self.text_chunks[i]['new_string'] = self.text_chunks[i]['correct'][list_index]
                self.API_dict[i]['correction_flag'] = False
                self.API_dict[i]['word'] = self.text_chunks[i]['correct'][list_index]
                self.API_dict[i]['new_string'] = self.text_chunks[i]['correct'][list_index]

        return self.API_dict
        



class SpellChecker:
    def __init__(self, input_text, language_selector, formality_selector):
        self.input_text = input_text
        self.language_selector = language_selector
        self.formality_selector = formality_selector
        self.word_check = WordCheck(self.input_text,  self.language_selector, self.formality_selector)

    def call(self):
        output_str = self.word_check.call()
        return output_str

    def call_corrector(self, id, list_index):
        return self.word_check.call_corrector(id, list_index)
        









