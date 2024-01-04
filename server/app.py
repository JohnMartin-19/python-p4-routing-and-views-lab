#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask</h1>'

@app.route('</string:print/parameter>')
def print_string(print):
    return f'<h1>Welcome to my flask app. By {print}</h1>'
@app.route('</integer:count/parameter>')
def count(int):
    return f'<h1>My Flask App has the following intergers: {int}</h1>'

@app.route('</interger:math/<num1><operation><num2>>')
def math(num1,operation,num2):
    return f'<h1>Welcome to my flask app. PLay with the operations below {num1,operation,num2}</h1>'
if __name__ == '__main__':
    app.run(port=5555, debug=True)
