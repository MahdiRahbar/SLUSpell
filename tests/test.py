import pytest
import os 
import sys


_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_path, '..'))
from src.apps import spellchecker
from open_test import OpenTest



_testPath = os.path.join(_path, 'assets')

file_path = [os.path.join(_testPath, 'corrections500.tsv'),]
newObj = OpenTest(file_path[0])
tests, answers =  newObj.get_tests()

def test_ga(tests, answers):
    pass

def test():
    with pytest.raises(SystemExit):
        pass