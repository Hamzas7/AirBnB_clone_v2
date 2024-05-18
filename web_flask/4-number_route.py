#!/usr/bin/python3
"""script to start a flask app on localhost
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """basic routing"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """specific routing"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def dynamic_text(text=None):
    """dynamic routing"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_dynamic(text='is_cool'):
    """dynamic w/ defaults"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def only_digits_dynamic(n=None):
    """type specific routing"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
