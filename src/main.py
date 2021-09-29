# -*- coding: utf-8 -*-

# Spell_Checker
# Developers: --
# License: -


from flask import Flask, render_template, request
from apps.spellchecker import SpellChecker

# added for debugging purposes
import logging, traceback 


app = Flask(__name__)


@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        input_text = request.form['input_text'] 
        language_selector = request.form['language_selector'] 
        formality_selector = request.form['formality_selector'] 

        spell_checker = SpellChecker(input_text, language_selector, formality_selector)
        spellChecked_text = spell_checker.call()
        return render_template('index.html', checked_text = spellChecked_text)  
        try:
            spell_checker = SpellChecker(input_text, language_selector, formality_selector)
            spellChecked_text = spell_checker.call()
            return render_template('index.html', checked_text = spellChecked_text)            
        except Exception as e:
            logging.error(traceback.format_exc())
            error_message = 'Something went wrong! Please try latter!'
            return render_template('index.html', checked_text = error_message)

            
    logging.error(traceback.format_exc())

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



if __name__ == "__main__":
    app.run(debug=True)