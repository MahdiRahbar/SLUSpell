<a href="https://opensource.org/licenses/GPL-3.0"><img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg" alt="License"></a>
[![Build Status](https://app.travis-ci.com/MahdiRahbar/SLUSpell.svg?branch=main)](https://app.travis-ci.com/MahdiRahbar/SLUSpell)
[![PyPI version](https://badge.fury.io/py/SLUSpell.svg)](https://badge.fury.io/py/SLUSpell)
<!-- [![PyPi version](https://pypip.in/v/SLUSpell/badge.png)](https://crate.io/packages/SLUSpell/)
[![PyPi download](https://pypip.in/d/SLUSpell/badge.png)](https://crate.io/packages/SLUSpell/) -->



# SLUSpell

SLUSpell is an open-source project that provides a simple user interface for spell checking. This project currently supports English and Irish. 

*****
## Usage Guide 

### Install (Recommended)
To install SLUSpell, you can simply use the following commands: 
```Python
# on windows
pip install sluspell

# on Linux/Mac 
pip3 install sluspell
```

### Usage guide from source
To use the project, you should first fork the repo and clone it on your computer, or you might just easily download it. After that, you should install the project dependencies. 

#### Dependencies
You can easily install the dependencies by entering the following command in the project directory on windows OS:
```Python
pip install -r requirements.txt
```
or the following command on Linux or Mac OS: 
```Python
pip3 install -r requirements.txt
```
#### Quick Start
To run the application first, go to the */src* directory and run the following command on Windows OS: 
```Python
python main.py
```
or the below command on Linux or Mac OS:
```Python 
python3 main.py
```

## Out of repo contributions
- **Irish large preprocessed data**

[This repo](https://github.com/Annoyed-Raven/Irish_processing) contains pure Irish words extracted from several sources. Some of the main text files before preprocessing contained around 1400 non-Irish characters.



## Todo 
1. Using more accurate dictionaries.
2. Adding more test cases to check the robustness of the application. 
3. Adding more complicated models to handle misspelled cases better.

## License
SLUSpell is licensed under the terms of GNU General Public License v3. This library can be used for both academic and commercial purposes. For more information, check out the [LICENSE](https://github.com/MahdiRahbar/Spell_Checker/blob/main/LICENSE.txt) file.
