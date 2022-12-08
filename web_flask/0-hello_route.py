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
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
