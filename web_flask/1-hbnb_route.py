#!/usr/bin/python3
"""display different messages"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
