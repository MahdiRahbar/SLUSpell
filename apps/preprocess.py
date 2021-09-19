# -*- coding: utf-8 -*-

# Spell_Checker
# Developers: --
# License: -


import re 
from collections import Counter 

def Words(text):
    '''
    Return a list of words.  

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

    


def Cap_begin(text):
    '''
    Return a list of words.  

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

