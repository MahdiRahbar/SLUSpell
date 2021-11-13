# -*- coding: utf-8 -*-

# check_import 
# Developers: --
# License: -

import pickle as pkl
import os
import sys
import pytest
_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_path, '..'))
from src.apps import spellchecker
from src.apps import langSpec


def get_filepaths(directory):
    file_paths = []  
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath) 

    return file_paths  

# @pytest.fixture
def test_open_pickle(path):
    path_list = get_filepaths(path)
    for p in path_list:
        if p.endswith('.pkl'):
            try:
                with open(p, 'rb') as f:                
                    data = pkl.load(f)
            except:
                raise AssertionError("Couldn't open file at: %s" % str(p))


if __name__ == "__main__":
    directory_path = os.path.join(_path, '..','src','apps','assets','dict') 
    test_open_pickle(directory_path)


