#!/usr/bin/python3
"""
 A Script that starts a flask web application
 Display "Hello HBNB!"
"""

from flask import Flask, request, render_template


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


@app.route("/number/<int:n>")
def number(n):
    """ Displays "n is a number" """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """ Displays HTML page when n is integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """ Displays HTML page when n is integer"""
    if (n % 2 == 0):
        n = "{} is even".format(n)
        return render_template("6-number_odd_or_even.html", n=n)
    else:
        n = "{} is odd".format(n)
        return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run()
