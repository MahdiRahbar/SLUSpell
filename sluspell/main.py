# -*- coding: utf-8 -*-

# Spell_Checker
# Developers: --
# License: -


# added for debugging purposes
import logging, traceback 
import pickle as pkl 
import os 
import sys


_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_path))
from flask import Flask, render_template, request, jsonify
from apps.spellchecker import SpellChecker


with open(os.path.join(_path,'templates','assets','main_page.pkl'), 'rb') as f:
    main_page = pkl.load(f)


app = Flask(__name__)


@app.route('/',  methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
        page_lang = 'English'
        return render_template('index.html' , message = main_page[page_lang])
    elif request.method == 'POST':
        page_lang = request.form['main_page_lang']
        if page_lang == "English":
            return render_template('index.html', message = main_page[page_lang])
        elif page_lang == "Irish": 
            return render_template('index.html', message = main_page[page_lang])
        else:
            return render_template('index.html' , message = main_page['English'])
    else:
        return "Something went wrong while loading the page!"


@app.route('/check', methods =['GET','POST'])
def check():
    try:
        if request.method == 'POST':      
            data = request.get_json(force=True)
            input_text = data['input_text'] 
            language_selector = data['language_selector'] 
            formality_selector = data['formality_selector']             
            if input_text and language_selector and formality_selector:
                global spell_checker # Global Variable 
                spell_checker = SpellChecker(input_text, language_selector, formality_selector)
                spellChecked_text = spell_checker.call()
                return jsonify({'checked_text' : spellChecked_text })
            return jsonify({'error' : "Something went wrong!" })        

    except Exception as e:
        logging.error(traceback.format_exc())
        error_message = 'Something went wrong! Please try latter!'
        return render_template('index.html', checked_text = error_message)

@app.route('/correct', methods =['GET','POST'])
def correct():
    try:
        if request.method == 'POST':      
            data = request.get_json(force=True)
            element_id = data['element_id'] 
            list_index = data['list_index'] 
            
            spellChecked_text = spell_checker.call_corrector(element_id, list_index)

            return jsonify({'checked_text' : spellChecked_text })
        return jsonify({'error' : "Something went wrong!" })        

    except Exception as e:
        logging.error(traceback.format_exc())
        error_message = 'Something went wrong! Please try latter!'
        return render_template('index.html', checked_text = error_message)
            
    

@app.route('/login', methods =['GET', 'Post'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        username = request.form['Username'] 
        password = request.form['Password']
        if (username).lower() == 'kscanne@gmail.com' and password.lower() == 'programmingisfun':
            return render_template('auth/login.html', message = 'Login Successful!')
        else: 
            error_message = 'The Login Information is Incorrect!'
            return render_template('auth/login.html', message = error_message)

@app.route('/register', methods =['GET'])
def register():
    return render_template('auth/register.html')


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()