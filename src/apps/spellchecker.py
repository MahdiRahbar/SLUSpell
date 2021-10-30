# -*- coding: utf-8 -*-

# Spell_Checker
# Developers: --
# License: -


import pickle as pkl
import re 
from collections import Counter 
import string 



class Dictionary:
    def __init__(self, path) -> None:
        self.dict = ()
        self.path = path 
        self.word_dict = self.read_dict_file()

    def read_dict(self, text): 
        return re.findall(r'\w+', text.lower())

    def read_dict_file(self):
        WORDS = Counter(self.read_dict(open(self.path,encoding='utf-8').read()))
        return WORDS

    def cal_proba(self, given_word):
        return self.word_dict[given_word]/ sum(self.word_dict.values())



class WordCheck:
    def __init__(self, text,language, formality):
        self.formality = formality
        self.language = language  
        dictionary_path = "apps/assets/dict/{}-common.txt".format(self.language)
        self.dict_obj = Dictionary(dictionary_path)
        self.alt_dict_path = 'apps/assets/dict/twitter_sentiment140_dict.pkl'

        self.mis_counter = 0
        self.word_dict = self.get_dict()
        self.alt_dict = self.ext_dict()
        self.word_list = self.words(text)
        self.API_dict = {}

    
    def get_dict(self):
        word_dict = self.dict_obj.read_dict_file()
        return word_dict

    def ext_dict(self)->dict:        
        if self.formality == 'informal' :
            with open(self.alt_dict_path, 'rb') as f:
                alt_dict = pkl.load(f)
        else: 
            alt_dict = self.word_dict

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
        temp_list = []
        p = re.compile("\w+") 
        for m in p.finditer(text):
            # word, index, index, Correction Flag, ID for frontend
            # temp_list.append([m.group(0),"",m.start(), m.end(),False, 0])
            temp_list.append({'word':m.group(0),'correct':"", 'new_string':'','start_i':m.start(), 'end_i':m.end(),'correction_flag':False, 'id':0})
        return temp_list  
    
    def correction(self, word): 
        "Most probable spelling correction for word."
        return max(self.candidates(word), key=self.dict_obj.cal_proba)

    def candidates(self, word): 
        "Generate possible spelling corrections for word."
        return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word])

    def known(self, words): 
        "The subset of `words` that appear in the dictionary of self.word_dict."
        return set(w for w in words if w in self.word_dict)

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word): 
        "All edits that are two edits away from `word`."
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))  

    def run_checker(self):
        for i in range(len(self.word_list)):
            temp_word = self.correction(self.word_list[i]['word'],)            
            if self.word_list[i]['word'] != temp_word:
                self.word_list[i]['correction_flag'] = True
                self.word_list[i]['correct'] = temp_word
                # self.mis_counter += 1 
                # self.word_list[i]['id'] = self.mis_counter
                self.word_list[i]['id'] = i
                self.word_list[i] = self.highliter(self.word_list[i], i) # It has to contain the correct spelling
                self.API_dict[i] = {'new_string': self.word_list[i]['new_string'] , 'word': self.word_list[i]['word'], 'correct':self.word_list[i]['correct'], 
                                     'correction_flag':self.word_list[i]['correction_flag'] ,'id':self.word_list[i]['id']}
            else: 
                self.word_list[i]['correct'] = temp_word
                self.word_list[i]['new_string'] = temp_word
                self.word_list[i]['id'] = i
                self.API_dict[i] = {'new_string': self.word_list[i]['new_string'] , 'word': self.word_list[i]['word'], 'correct':self.word_list[i]['correct'], 
                                     'correction_flag':self.word_list[i]['correction_flag'] ,'id':self.word_list[i]['id']}

                    # temp_list.append({'word':m.group(0),'correct':"", 'new_string':'','start_i':m.start(), 'end_i':m.end(),'correction_flag':False, 'id':0})

    
    def highliter(self, word, index):
        # tagged_word =  "<span class='highlight highlight{}' onmouseover='show_popup({},\"{}\")' onmouseout='hide_popup({},\"{}\")'>".format(word['id'], word['correct'] ,word['id'], word['correct'])+\
        #                 "{}</span>".format(word['word'])
        tagged_word =  "<span class='highlight highlight{}' onclick='show_correct({})' >".format(word['id'],word['id'])+\
                        "{}</span>".format(word['word'])   # onmouseout='hide_correct({})'
        
        # "<span class='highlight popup highlight{} popup{}' id='higlight' onmouseover='show_popup({},\"{}\")' onmouseout='hide_popup({},\"{}\")'>".format(word[-1], word[-1], word[-1], word[1] ,word[-1], word[1]) + \
        #                 "<a onclick='async_correction({})'><span class='popuptext' id='pop-up{}'>{}</span></a>{}</span>".format(word[-1],word[-1], word[1], word[0]) 
                        
        # The first span keeps the popup and has to keep the correct word
        word['new_string'] = tagged_word
        return word            

    def check_flag(self):
        pass

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

    def call(self):
        self.run_checker()
        output = ""
        # for i in range(len(self.word_list)):            
            # output += self.word_list[i]['word'] + " "

        # return output  # , self.word_list[:][-1]
        return self.API_dict
    
    def call_corrector(self, id):
        output = ""
        for i in range(len(self.word_list)):
            if self.word_list[i]['id'] == id: 
                self.word_list[i]['correction_flag'] = False
                self.word_list[i]['word'] = self.word_list[i]['correct']
                self.word_list[i]['new_string'] = self.word_list[i]['correct']
                self.API_dict[i]['correction_flag'] = False
                self.API_dict[i]['word'] = self.word_list[i]['correct']
                self.API_dict[i]['new_string'] = self.word_list[i]['correct']

        # for i in range(len(self.word_list)):            
        #     output += self.word_list[i]['word'] + " "
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

    def call_corrector(self, id):
        return self.word_check.call_corrector(id)
        









