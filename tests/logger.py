    
import re
import os 
import sys 
import time
from open_test import *

_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_path, '..'))
from sluspell.apps.spellchecker import SpellChecker
    
def testlogger(tests, lang, formality, file_name = 'sluspell_test.tsv'):
    counter = 0 
    for test in tests:
        if counter%10 ==0 :
            print("Test case %d"%(counter+1))
        counter += 1 
        try:
            spellObj = SpellCheckAPI(test, lang, formality)
            corrected_string = spellObj.call()
            corrected_string = re.sub( r"&lt;", "<", corrected_string) 
            corrected_string = re.sub( r"&gt;",">", corrected_string)

            if test[0]!=test[0].upper():
                corrected_string = corrected_string.lower()

            # cap_flag_list = [bool(re.match("([A-Z])", char)) for char in test]
            # to_upper = lambda word: (list(x) for x in itertools.permutations(word))
            new_line = test + '\t' + corrected_string
            logger(new_line, file_name)
        except: 
            new_line = test + '\t' + 'EXCEPTION'
            logger(new_line, file_name)

def logger(new_line, file_name):
    with open(file_name, "a" , encoding= "utf-8") as f:
        f.write(new_line)
        f.write("\n")