#!/usr/bin/env python3
"""Flask Restaurant MS App
"""
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """"""
    return jsonify({})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
