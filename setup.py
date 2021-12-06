import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# https://stackoverflow.com/questions/53779509/upload-failed-403-invalid-or-non-existent-authentication-information-python - python setup.py sdist bdist_wheel - twine upload dist/*
setup(
    name='SLUSpell',  
    version='0.1.4',
    scripts=['setup'] ,
    author="Mahdi Rahbar",
    author_email="mahdirahbar01@gmail.com",
    description="SLUSpell is an open-source spell checker that uses multiple techniques to find misspelled words.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mahdirahbar/SLUSpell",
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: OS Independent",
     ],
    packages=  ["sluspell"],
    package_data = {"sluspell":["*.pkl","*.py","*.html","*.js","*.css","*.svg","*.txt"]},
    include_package_data=True,
    install_requires=["flask", "numpy"],
    entry_points={
        "console_scripts": [
            "sluspell=sluspell.main:main",
        ]
    },
 )



