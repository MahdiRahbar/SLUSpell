import pytest
import os 
import sys


_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_path, '..'))
from sluspell.apps import spellchecker
from open_test import OpenTest
from check_import import test_open_pickle

# def test():
#     # with pytest.raises(SystemExit):
#     pass

if __name__ == "__main__":
    _testPath = os.path.join(_path, 'assets')
    file_path = [os.path.join(_testPath, 'corrections500.tsv'),]

    newObj = OpenTest(file_path[0])
    tests, answers =  newObj.get_tests()
    newObj.test_input()

    dir_path_dict = os.path.join(_path, '..','sluspell','apps','assets','dict') 
    test_open_pickle(dir_path_dict)
    
    