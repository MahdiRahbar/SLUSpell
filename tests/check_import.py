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
from sluspell.apps import spellchecker
from sluspell.apps import langSpec
__test__ = True


def get_filepaths(directory):
    file_paths = []  
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath) 

    return file_paths  

# @pytest.fixture
directory_path = os.path.join(_path, '..','sluspell','apps','assets','dict') 

def test_open_pickle(dir_path = directory_path):
    path_list = get_filepaths(dir_path)
    for p in path_list:
        if p.endswith('.pkl'):
            try:
                with open(p, 'rb') as f:                
                    data = pkl.load(f)
            except:
                print("Couldn't open file at: %s" % str(p))
    return


# if __name__ == "__main__":
#     directory_path = os.path.join(_path, '..','sluspell','apps','assets','dict') 
#     test_open_pickle(directory_path)


