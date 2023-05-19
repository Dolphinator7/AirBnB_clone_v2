#!/usr/bin/python3
"""Module - script that starts a Flask web application"""
from flask import Flask

app = Flask('web_flask')

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

