
from apps.spellchecker import *
from tests.open_test import OpenTest


_path = os.path.abspath(os.path.dirname(__file__))
_testPath = os.path.join(_path,'tests', 'assets')

file_path = [os.path.join(_testPath, 'corrections500.tsv'),]
newObj = OpenTest(file_path[0])
tests, answers =  newObj.get_tests()