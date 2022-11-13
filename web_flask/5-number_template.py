#!/usr/bin/python3
"""Jinja template"""
from flask import Flask, render_template
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


@app.route('/python')
@app.route('/python/<text>')
def display_python(text='is cool'):
    return 'Python %s' % escape(text).replace('_', ' ')


@app.route('/number/<int:n>')
def display_num(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def number__template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
