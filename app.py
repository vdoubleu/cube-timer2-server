from flask import Flask, request, jsonify
from mongoConnect import connect

app = Flask(__name__)

@app.route('/gettime', methods=['GET'])
def gettime():
    times_coll = connect()

    user_id = request.args.get("id")
    
    if user_id is None:
        return jsonify("user not found")
    
    get_data = times_coll.find_one({"id": user_id})
    times = get_data["time"]

    reformatted_times = []

    count = 0
    for x in times:
        reformatted_times.append({"name": str(count), "solvetime": x})
        count += 1

    if get_data is not None:
        return jsonify({"reformtime": reformatted_times})
    else:
        return jsonify(None)

    return jsonify(user_id)

@app.route('/addtime', methods=['POST'])
def posttime():
    times_coll = connect()

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
    times_coll = connect()

    data = request.get_json()
    user_id = data['id']

    times_coll.update_one({"id": user_id}, {"$pop": {"time": 1}})

    return jsonify("deleteone")

@app.route('/deleteall', methods=['POST'])
def deleteall():
    times_coll = connect()

    data = request.get_json()
    user_id = data['id']

    times_coll.update_one({"id": user_id}, {"$set": {"time": []}})

    return jsonify("deleteall")

@app.route('/', methods=['GET'])
def test():
    app.logger.info("hey")
    return "hello"

if __name__ == '__main__':
    app.run();
