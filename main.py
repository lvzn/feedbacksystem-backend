from dotenv import load_dotenv
load_dotenv('./.env')

import os
from logging import debug
from flask import Flask
from flask import jsonify,request
import pymysql
import datetime
url = os.getenv('DBURL')
username = os.getenv('USER')
password = os.getenv('PASSWORD')
con = pymysql.connect(host=url, user=username, password=password)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/api", methods=["POST", "GET"])
def getFeedback():
    data = request.json
    print(os.getenv('DBURL'))
    return data
def saveFeedbackToDatabase():
    print(os.environ["DBURL"])

app.run()