# -*- coding: utf-8 -*-

# Spell_Checker
# Developers: --
# License: -


import re 
from collections import Counter 


class dictionary:
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
        return self.word_dict[given_word]/ sum(self.word_dict)




def words(text):
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
        temp_list.append([m.end(), m.end(),m.group(0)[-1]])
    return temp_list
   

def cap_begin(text):
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
        temp_list.append([m.end(), m.end(),m.group(0)[-1]])
    return temp_list






