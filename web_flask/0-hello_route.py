#!/usr/bin/python3
# display Hello HBNB!
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


app.run(host='0.0.0.0', port=5000)
