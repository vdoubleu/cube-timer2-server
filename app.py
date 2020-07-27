from flask import Flask, request, jsonify
from mongoConnect import connect
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/gettime', methods=['GET'])
def gettime():
    user_id = request.args.get("id", None)

    return jsonify(user_id)

@app.route('/addtime', methods=['POST'])
def posttime():
    load_dotenv()
    user = os.getenv("DBUSER")
    pw = os.getenv("PW")

    uri = "mongodb+srv://" + user + ":" + pw + "@cluster0.gnkvv.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(uri)

    db = client.test
    times_coll = db.times_collection

    data = request.get_json()
    user_id = data['id']
    user_time = data['time']

    if times_coll.find_one({'id': user_id}) is not None:
        times_coll.update_one({'id': user_id}, {'$push': {'time': user_time}})
    else:
        times_coll.insert_one({'id': user_id, 'time': [user_time]})

    return jsonify({'id': user_id, 'time': user_time})

@app.route('/deleteone', methods=['POST'])
def deleteone():
    param = request.form.get('id')

    return jsonify("deleteone")

@app.route('/deleteall', methods=['POST'])
def deleteall():
    param = request.form.get('id')

    return jsonify("deleteall")

@app.route('/', methods=['GET'])
def test():
    app.logger.info("hey")
    return "hello"

if __name__ == '__main__':
    app.run();
