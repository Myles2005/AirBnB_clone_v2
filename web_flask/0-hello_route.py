#!/usr/bin/python3
""" Flask Application """

from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def home():
    """Home page
    Return: Hello HBNB!
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

