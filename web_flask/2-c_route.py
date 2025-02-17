#!/usr/bin/python3
"""replace underscore"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def message(text):
    return 'C %s' % escape(text).replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
