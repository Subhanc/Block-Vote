import json
import flask
import requests


import os
from flask import Flask, request
app = Flask(__name__)
# from app import routes

@app.route('/')

def hello():
    print(request.args)
    resp = flask.Response(json.dumps(getData()))

    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/data', methods = ['GET'])
def handleGet():
    return json.dumps("test")

@app.route('/castBallot', methods = ['POST'])
def castBallot():
    passphrase = request.args['passphrase']
    vote = request.args['vote']
    os.system('python ../castBallot.py ' + passphrase + ' ' + vote)

def getData():
     os.system('python ../createVoter.py')
     return "clay harbor enemy utility margin pretty hub comic piece aerobic umbrella acquire"

if __name__ == '__main__':
    app.run(debug = True)