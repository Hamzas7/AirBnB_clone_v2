#!/usr/bin/python3
"""script to start a flask app on localhost
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """first route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """more specific routes"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def dynamic_text(text=None):
    """dynamic routes """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_dynamic(text='is_cool'):
    """dynamic routes with multiple routes and defaults"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def only_digits_dynamic(n=None):
    """only type specific routes"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def first_template(n=None):
    """first template routes"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def conditional_templating(n=None):
    """checking input data using templating"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
