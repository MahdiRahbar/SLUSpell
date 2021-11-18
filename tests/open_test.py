# -*- coding: utf-8 -*-

# open_test
# Developers: Mahdi Rahbar, Nicolas Prudencio
# License: GNU General Public License v3.0

import re
import os 
import sys 
import time

_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_path, '..'))
from sluspell.apps.spellchecker import SpellChecker

class OpenTest:
    def __init__(self, path):
        self.path = path 
        self.tests, self.answers = self.get_tests()

    def open_file(self):
        """
        - description: This method opens the test files 
            and returns a list of lines. 
        - output: list 
        """
        with open(self.path, encoding = 'utf8') as f: 
            test_cases = f.read().strip('\n').split('\n')
        return test_cases 

    def prepare_tests(self, text_delimiter = '\t'):
        """
        - description: This method gets a delimeter and 
            returns a list of lists, containing tests 
            and their corresponding correct answers.
        - output: list 
        """
        tests = self.open_file()
        temp_tests = []
        for i in range(len(tests)):
            temp_tests.append(tests[i].split(text_delimiter))
        return temp_tests

    def get_tests(self):
        """
        - description: This method returns two separate lists, 
            containing test cases and their corresponding 
            answers. 
        - ouput: Two lists 
        """
        test_list = self.prepare_tests()
        test_cases = []
        test_results = []
        for i in range(len(test_list)):
            test_cases.append(test_list[i][0])
            if len(test_list[i])>1:
                test_results.append(test_list[i][1])
        return test_cases, test_results
    
    def call(self):
        return self.get_tests()


class SpellCheckAPI:
    def __init__(self, text, lang='en', formality='formal'):
        self.text = text 
        self.spell_checker = SpellChecker(text, lang, formality)
        self.spellChecked_text = self.spell_checker.call()

    #   {'word':chunk_list[i],'correct':"",
    #       'new_string':'','correction_flag':False, 
    #       'check_flag': check_list[i] , 'cap_flag':cap_list[i],
    #       'id':0})

    def make_combinations(self):
        text_candidates_list = [] 
        for i in range(len(self.spellChecked_text)):            
            if self.spellChecked_text[i]['correction_flag']:
                correct_list = self.spellChecked_text[i]['correct']                                  
                if len(text_candidates_list)>0:
                    for j in range(len(correct_list)):  
                        for k in range(len(text_candidates_list)):
                            text_candidates_list[k] = text_candidates_list[k] + correct_list[j]
                else:
                    text_candidates_list = text_candidates_list + correct_list
            else:
                if len(text_candidates_list)> 0:
                    for k in range(len(text_candidates_list)):
                        text_candidates_list[k] = text_candidates_list[k] + self.spellChecked_text[i]['word']  
                else: 
                    text_candidates_list += [self.spellChecked_text[i]['word']]
        return text_candidates_list

    def single_corrected_case(self):
        corrected_string = '' 
        for i in range(len(self.spellChecked_text)):            
            if self.spellChecked_text[i]['correction_flag']:
                correct_word = self.spellChecked_text[i]['correct']
                corrected_string = corrected_string + correct_word[0]
            else: 
                corrected_string = corrected_string + self.spellChecked_text[i]['word']
        return corrected_string

    def call(self):
        # return self.make_combinations()
        return self.single_corrected_case()
                    

class TestTextList:
    def __init__(self, tests, answers, lang, formality):
        self.tests = tests
        self.answers = answers
        self.lang = lang 
        self.formality = formality

    def test_input_list(self):
        test_id = 1
        counter = 0
        start_time = time.time()
        if self.tests and self.answers:
            for test, answer in zip(self.tests, self.answers):
                spellObj = SpellCheckAPI(test, self.lang, self.formality)
                candidate_list = spellObj.call()
                if self.assertTextList(candidate_list, answer, test_id = test_id ):
                    counter +=1 
                test_id += 1 
        else:
            raise AssertionError("No test file and answer file is found!")
        print()
        print("------------------------------------------------------------------------")
        print("The final accuracy of the application on the current test set is: %{:.2f}".format((counter)/len(self.tests)*100) )
        print("Finished in %d:%d s."%(((time.time()-start_time)/60),(time.time()-start_time)%60))

    def testlogger(self, file_name = 'sluspell_test.tsv'):
        for test, answer in zip(self.tests, self.answers):
            try:
                spellObj = SpellCheckAPI(test, self.lang, self.formality)
                corrected_string = spellObj.call()
                corrected_string = re.sub( r"&lt;", "<", corrected_string) 
                corrected_string = re.sub( r"&gt;",">", corrected_string)
                # cap_flag_list = [bool(re.match("([A-Z])", char)) for char in test]
                # to_upper = lambda word: (list(x) for x in itertools.permutations(word))
                new_line = test + '\t' + corrected_string
                self.logger(new_line, file_name )
            except:
                pass


    def logger(self, new_line, file_name):
        with open(file_name, "a", encoding= "utf-8") as f:
            f.write(new_line)
            f.write("\n")


    def test_input_single(self):
        test_id = 1
        counter = 0
        start_time = time.time()
        if self.tests and self.answers:
            for test, answer in zip(self.tests, self.answers):
                try:
                    spellObj = SpellCheckAPI(test, self.lang, self.formality)
                    corrected_string = spellObj.call()
                    corrected_string = re.sub( r"&lt;", "<", corrected_string) 
                    corrected_string = re.sub( r"&gt;",">", corrected_string)

                    # cap_flag_list = [bool(re.match("([A-Z])", char)) for char in test]
                    # to_upper = lambda word: (list(x) for x in itertools.permutations(word))

                    if test[0]==test[0].upper():
                        lower_flag = False
                    else:
                        lower_flag = True
                    if self.assertTextSingle(corrected_string , answer, test_id = test_id, lower_flag= lower_flag ):
                        counter +=1 
                    test_id += 1 
                except Exception as e: 
                    print("------------------------------------------------------------------------")
                    print("An exception raised in test case  %d."%test_id)
                    print(e)
                    print()
                    test_id += 1
        else:
            raise AssertionError("No test file and answer file is found!")
        print()
        print("------------------------------------------------------------------------")
        print("The final accuracy of the application on the current test set is: %{:.2f}".format((counter)/len(self.tests)*100) )
        print("Finished in %d:%d s."%(((time.time()-start_time)/60),(time.time()-start_time)%60))
    
    def assertTextList(self, test_case, correct_case , test_id = None, 
                    message= '' ):
        test_case_lower = []
        for i in range(len(test_case)):
            test_case_lower.append(test_case[i].lower())
        try:
            assert (correct_case in test_case) or (correct_case in test_case_lower) 
            return True 
        except AssertionError as e:
            print('Test case {}: The input test case does not match with the correct case. \n\n Excepted: {} \n but received: {}\n--------------------------\n'.format(test_id,correct_case, test_case))
            return False
        
    def assertTextSingle(self, test_case, correct_case , test_id = None, lower_flag= False, 
                message= '' ):
        if test_case!=None and lower_flag: 
            test_case = test_case.lower()
        try:
            assert (correct_case == test_case) 
            return True 
        except AssertionError as e:
            print('Test case {}: The input test case does not match with the correct case. \n\n Excepted: {} \n but received: {}\n--------------------------\n'.format(test_id,correct_case, test_case))
            return False