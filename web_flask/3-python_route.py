#!/usr/bin/python3
"""
 A Script that starts a flask web application
 Display "Hello HBNB!"
"""

from flask import Flask, request


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hbnb():
    """ Displays Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb():
    """ Display hello hbnb on the hbnb route"""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """ Displays "C" followed by the value of the text"""
    return "C " + text.replace("_", " ")


@app.route("/python", defaults={'text': 'is cool'})
@app.route("/python/<text>")
def python(text):
    """ Displays python is cool"""
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run()
