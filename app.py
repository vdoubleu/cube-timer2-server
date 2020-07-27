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
    load_dotenv()
    user = os.getenv("DBUSER")
    pw = os.getenv("PW")


    #uri = "mongodb://vdoubleu:victor12345@ds153096.mlab.com:53096/heroku_lws15pr3"
    uri = "mongodb+srv://vdoubleu:passwordVW12345@cluster0.gnkvv.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(uri)

    db = client.test
    times_coll = db.times_collection

    app.run();
