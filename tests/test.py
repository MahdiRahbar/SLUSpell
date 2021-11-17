import pytest
import os 
import sys


_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_path, '..'))
from sluspell.apps import spellchecker
from open_test import *
from check_import import test_open_pickle

# def test():
#     # with pytest.raises(SystemExit):
#     pass

if __name__ == "__main__":
    _testPath = os.path.join(_path, 'assets')
    file_path = [os.path.join(_testPath, 'corrections500.tsv'),]

    open_obj = OpenTest(file_path[0])
    tests, answers =  open_obj.get_tests()
    test_obj = TestTextList(tests, answers, 'ga', 'formal')
    test_obj.test_input_single()

    dir_path_dict = os.path.join(_path, '..','sluspell','apps','assets','dict') 
    test_open_pickle(dir_path_dict)
    
    