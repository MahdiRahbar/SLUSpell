# -*- coding: utf-8 -*-

# Spell_Checker
# Developers: --
# License: -


import pickle as pkl
import re 
from collections import Counter 



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

        self.counter = 0
        self.word_dict = self.get_dict()
        self.alt_dict = self.ext_dict()
        self.word_list = self.words(text)

    
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
        return self.alt_dict[given_word]/ sum(self.alt_dict.values())


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
            temp_list.append([m.group(0),"",m.start(), m.end(),False, 0])
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
            temp_word = self.correction(self.word_list[i][0],)            
            if self.word_list[i][0] != temp_word:
                self.word_list[i][3] = True
                self.word_list[i][1] = temp_word
                self.word_list[i] = self.highliter(self.word_list[i], i) # It has to contain the correct spelling
                self.counter += 1 
        
    
    def highliter(self, word, index):
        tagged_word = "<a>" + "<span class='highlight popup' id='higlight' onclick='popup_function()'><span class='popuptext' id='pop-up'>{}</span>{}</span>".format(word[1], word[0]) + "</a>"
        # The first span keeps the popup and has to keep the correct word
        word[0] = tagged_word
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
            temp_list.append([m.group(0)[-1],"",m.start(), m.end(),False])
        return temp_list

    def call(self):
        self.run_checker()
        output = ""
        for i in range(len(self.word_list)):            
            output += self.word_list[i][0] + " "
        return output  # , self.word_list[:][-1]



class SpellChecker:
    def __init__(self, input_text, language_selector, formality_selector):
        self.input_text = input_text
        self.language_selector = language_selector
        self.formality_selector = formality_selector

    def call(self):
        word_check = WordCheck(self.input_text,  self.language_selector, self.formality_selector)
        output_str = word_check.call()
        return output_str









