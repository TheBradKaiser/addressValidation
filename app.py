from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

@app.route('/',  methods=['POST', "GET"])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        addressDict = {}
        for i in request.form:
            print(i)
            print(request.form[i])
            if request.form[i] == "":
                return render_template("index.html", result = "missing: "+ i) 
            addressDict[i] = request.form[i]
        result = checkStructure(addressDict)
        
        return render_template("index.html",result = result)


def checkStructure(addressStr):
    return "valid address"


