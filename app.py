from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/gettime', methods=['GET'])
def gettime():
    name = request.args.get("name", None)

    return jsonify(name)

@app.route('/addTime', methods=['POST'])
def posttime():
    user_name = request.form['name']
    user_time = request.form['id']

    if times_coll.find_one({'name': user_name}) is not None:
        times_coll.update_one({'name': user_name}, {'$push': {'time': user_time}})
    else:
        times_coll.insert_one({'name': user_name, 'time': [user_time]})

    return jsonify({'name': user_name, 'time': user_time})

@app.route('/deleteone', methods=['POST'])
def deleteone():
    param = request.form.get('name')

    return jsonify("deleteone")

@app.route('/deleteall', methods=['POST'])
def deleteall():
    param = request.form.get('name')

    return jsonify("deleteall")

if __name__ == '__main__':
    load_dotenv()
    user = os.getenv("USER")
    pw = os.getenv("PW")

    uri = "mongodb://" + user + ":" + pw + "@ds153096.mlab.com:53096/heroku_lws15pr3"
    client = MongoClient(uri,
                         connectTimeoutMS=30000,
                         socketTimeoutMS=None,
                         socketKeepAlive=True)

    db = client.get_default_database()
    times_coll = db.times_collection

    app.run();
