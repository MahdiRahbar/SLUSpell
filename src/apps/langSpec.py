# -*- coding: utf-8 -*-

# langSpec
# Developers: Mahdi Rahabr
# License: -

import string



class LangSpec:
    PUNC = string.punctuation
    def __init__(self, lang):
        self.lang = lang 

class Text:
    def __init__(self, input_text):
        self.input_text = input_text
        self.word_list = self.split_string()

    def split_string(self):
        return self.input_text.split(' ')

    def to_lower(self):
        for i in range(len(self.word_list)):
            self.word_list[i] = self.word_list[i].lower()
        return self.word_list

    def check_punc(self, input_str):
        word= str()
        b_punc = str()
        e_punc = str()
        if word[0] in PUNC:
            b_punc = word[0]
            word.pop(0)
        if word[-1] in PUNC:
            b_punc = word[-1]
            word.pop(-1)
        return word, b_punc, e_punc


    def call(self):
        return self.to_lower()

    


    
class Irish(Text):
    def __init__(self):
        super(Irish, self).__init__()

    def to_lower(self, input_text):
        '''
            This function process the words in Irish language and 
                convert them based on the rules in Irish. 
            input: - 
            output: returns the fianl string
        '''
        irish_upper = ('A','E','I','O','U','Á','É','Í','Ó','Ú')
        irish_exp = ('n','t')
        for i in range(len(self.word_list)):
            if (self.word_list[i][0] in irish_exp) and \
                (self.word_list[i][1] in irish_upper):
                self.word_list[i] =  self.word_list[i][0].lower() + \
                                     '-' + self.word_list[i][1:].lower()
            else: 
                self.word_list[i] = self.word_list[i].lower()
        return self.word_list 

class English(Text):
    def __init__(self):
        super(English, self).__init__()
