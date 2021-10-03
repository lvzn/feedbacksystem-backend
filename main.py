from flask import jsonify, request, Flask
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
    saveFeedbackToDatabase(data)
    return "OK"

def saveFeedbackToDatabase(data):
    connection = pymysql.connect(host=url, user=username, passwd=password, database="dev_feedback")

    with connection:
        with connection.cursor(DictCursor) as cursor:              
            cursor.execute('insert into reviews (r1, r2, submitdate) values (%s, %s, curdate())', (data["overall_feedback"], data["staff_feedback"]))
            cursor.execute("commit")

app.run()
