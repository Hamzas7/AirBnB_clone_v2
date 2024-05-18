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
    """Specific routing"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def dynamic_text(text=None):
    """dynamic routing"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
