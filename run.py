#!venv/bin/python
#from xd import app, db
import requests

import os
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world!"


if __name__ == '__main__':
    app.run(debug=True)



