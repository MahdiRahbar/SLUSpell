# -*- coding: utf-8 -*-

# Spell_Checker
# Developers: --
# License: -


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        

@app.route('/login', methods =['GET'])
def login():
    return render_template('auth/login.html')

@app.route('/register', methods =['GET'])
def register():
    return render_template('auth/register.html')



if __name__ == "__main__":
    app.run(debug=True)