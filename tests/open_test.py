# -*- coding: utf-8 -*-

# open_test
# Developers: Mahdi Rahbar, Nicolas Prudencio
# License: GNU General Public License v3.0


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
            test_results.append(test_list[i][1])
        return test_cases, test_results

    def test_input(self):
        test_id = 1
        if self.tests and self.answers:
            for test, answer in zip(self.tests, self.answers):
                self.assertText(test,answer, test_id = test_id )
                test_id += 1 
        else:
            raise AssertionError("No file test and answer file is defined.")
    
    def assertText(self, test_case, correct_case , test_id = None, 
                    message= '' ):
        try:
            assert test_case == correct_case
        except AssertionError as e:
            print('Test case {}: The input test case does not match with the correct case. \n\n Excepted: {} \n but received: {}\n--------------------------\n'.format(test_id,correct_case, test_case))
