#!/usr/bin/python3
"""
 A Script that starts a flask web application
 Display "Hello HBNB!"
"""

from flask import Flask


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


if __name__ == "__main__":
    app.run()
