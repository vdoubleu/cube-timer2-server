from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/gettime', methods=['GET'])
def gettime():
    user_id = request.args.get("id", None)

    return jsonify(user_id)

@app.route('/addtime', methods=['POST'])
def posttime():
    user_id = request.form.get('id')
    user_time = request.form.get('time')

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
    return "hello"

if __name__ == '__main__':
    load_dotenv()
    user = os.getenv("DBUSER")
    pw = os.getenv("PW")

    uri = "mongodb://" + user + ":" + pw + "@ds153096.mlab.com:53096/heroku_lws15pr3"
    client = MongoClient(uri)

    db = client.get_default_database()
    times_coll = db['times_collection']

    app.run();
