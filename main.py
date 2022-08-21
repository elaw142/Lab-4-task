from markupsafe import escape
from flask import Flask, render_template

from factorial import compute_factorial

app = Flask(__name__)


@app.route('/')
def show_main():
    return render_template('index.html')


@app.route('/user/<username>')
def show_user_profile(username):
    return f'Hello {escape(username)}! Welcome to COMPSCI235 Lab 3'


@app.route('/factorial/<int:input_val>')
def show_factorial(input_val):
    factorial = compute_factorial(input_val)
    return render_template('factorial.html',
        input=input_val, 
        factorial=factorial)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
