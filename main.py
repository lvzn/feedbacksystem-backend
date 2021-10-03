from flask import jsonify, request, Flask
import datetime
import pymysql
import os
from dotenv import load_dotenv
from pymysql.cursors import DictCursor
load_dotenv('./.env')

url = os.getenv('DB_URL')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/api", methods=["POST", "GET"])
def getFeedback():
    data = request.json
    saveFeedbackToDatabase()
    return "OK"


def saveFeedbackToDatabase():
    connection = pymysql.connect(host=url, user=username, passwd=password)

    with connection:
        with connection.cursor(DictCursor) as cursor:
            cursor.execute("show databases")
            available_dbs = cursor.fetchall()

            print(available_dbs)


app.run()
