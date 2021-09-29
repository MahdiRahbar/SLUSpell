# -*- coding: utf-8 -*-

# Spell_Checker
# Developers: --
# License: -


import re 
from collections import Counter 


class SpellChecker():
    def __init__(self, input_text, language_selector, formality_selector):
        self.input_text = input_text
        self.language_selector = language_selector
        self.formality_selector = formality_selector

    def call(self):
        Checked_text =  self.input_text
        return Checked_text
    def errorCount(self):  #this is to send the error count total to the front end, still need to link it to html, nicolas 9/29/2021
        Checked_text =  self.input_text
        Error_Count = len(Checked_text)
        return Error_Count

        



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
        return self.word_dict[given_word]/ sum(self.word_dict)


class Spell_Checker():
    def __init__():
        pass
    
    def correction(self, word): 
        "Most probable spelling correction for word."
        return max(candidates(word), key=P)

    def candidates(self, word): 
        "Generate possible spelling corrections for word."
        return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

    def known(self, words): 
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in WORDS)

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
        return (e2 for e1 in edits1(word) for e2 in edits1(e1))



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






