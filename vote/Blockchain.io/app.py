import json
import flask
import requests

import os
from flask import Flask, request
app = Flask(__name__)
from app import routes

@app.route('/')
@app.route('/index')

def hello():
    print(request.args)
    # resp = flask.Response(json.dumps(getData()))

    # resp.headers['Access-Control-Allow-Origin'] = '*'
    return request.args

@app.route('/data', methods = ['GET'])
def handleGet():
    return json.dumps("test")


def getData():
     os.system('python /Users/jacob/Desktop/Python/vote/createVoter.py')
     return "clay harbor enemy utility margin pretty hub comic piece aerobic umbrella acquire"

if __name__ == '__main__':
    app.run(debug = True)