# -*- coding: utf-8 -*-

# langSpec
# Developers: Mahdi Rahabr
# License: -

import string
import re



class LangSpec:
    PUNC = string.punctuation
    def __init__(self, input_text, lang):
        self.lang = lang 
        self.input_text = input_text
        self.textObj = None

    def call(self):
        if self.lang=='en':
            self.text = English(self.input_text)
        elif self.lang=='ga':
            self.text = Irish(self.input_text) 
        return self.text

    


class Text:
    def __init__(self, input_text):
        self.input_text = input_text
        self.string_chunks = []

    def to_lower(self,input_word):
        # 2        
        return input_word.lower()

    def check_punc(self, input_str):


        punc = '!!!!!""""#$$%&\'()*+,-..../:;<===>?????!!!!!!@[\\]^_`{|}~                                            \t\t\t\t\t'
        stop_punc = '!!!!!""""#\'()....:;?????!!!!!!'
        # str_chunck = [x.group() for x in re.finditer( r'(\w+[-\']*\w*|\s+|[!,.:?]+)', input_str)]   #    r'(\w*\'*\w+?|\s+|[!,.:?]+)'
        str_chunck = []

        p = re.compile(r'(\w+[-\']*\w*|\s+|[!,.:?]+)') 
        for m in p.finditer(input_str):
            str_chunck.append(m.group(0))

        check_flag = []
        cap_flag = []
        cap_f = True
        rule = re.compile(r'\w+')
        for c in str_chunck:
            punc_flag = False

            check_flag.append(not(c in punc))
            
            if rule.search(c): 
                cap_flag.append(cap_f)
            cap_f = False
            if c in stop_punc:
                cap_flag.append(cap_f)
                cap_f = True
            else: 
                cap_flag.append(cap_f)
            
        return str_chunck, check_flag, cap_flag

    def create_ds(self):
        # 3
        # p = re.compile("\w+")
        chunk_list, check_list, cap_list = self.check_punc(self.input_text)
        for i in range(len(chunk_list)):                
            self.string_chunks.append({'word':chunk_list[i],'correct':"", 'new_string':'','correction_flag':False, 'check_flag': check_list[i] , 'cap_flag':cap_list[i],  'id':0})

        return self.string_chunks
    

    def call(self):
        return self.create_ds()



    


    
class Irish(Text):
    def __init__(self,input_text):
        super(Irish, self).__init__(input_text)

    def to_lower(self, input_word):
        '''
            This function process the words in Irish language and 
                convert them based on the rules in Irish. 
            input: - 
            output: returns the fianl string
        '''
        irish_upper = ('A','E','I','O','U','Á','É','Í','Ó','Ú')
        irish_exp = ('n','t')        
        if (input_word[0] in irish_exp) and \
            (input_word[1] in irish_upper):
            input_word =  input_word[0].lower() + \
                                    '-' + input_word[1:].lower()
        else: 
            input_word = input_word.lower()
        return input_word

class English(Text):
    def __init__(self, input_text):
        super(English, self).__init__(input_text)
