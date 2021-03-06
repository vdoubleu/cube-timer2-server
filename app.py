from flask import Flask, request, jsonify, after_this_request
from mongoConnect import connect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    return 'alive'

@app.route('/gettime', methods=['GET'])
def gettime():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    times_coll = connect()

    user_id = request.args.get("id")
    
    if user_id is None:
        return jsonify("user not found")
    
    get_data = times_coll.find_one({"id": user_id})
    if get_data is None:
        return jsonify({"reformtime": []})

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

    user_id = request.args.get("id")
    user_time = request.args.get("time")

    if times_coll.find_one({'id': user_id}) is not None:
        times_coll.update_one({'id': user_id}, {'$push': {'time': user_time}})
    else:
        times_coll.insert_one({'id': user_id, 'time': [user_time]})

    return jsonify({'id': user_id, 'time': user_time})

@app.route('/deleteone', methods=['GET'])
def deleteone():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    times_coll = connect()

    user_id = request.args.get("id")

    if user_id is None:
        return jsonify("user not found")

    times_coll.update_one({"id": user_id}, {"$pop": {"time": 1}})

    return jsonify("deleteone")

@app.route('/deleteall', methods=['GET'])
def deleteall():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    times_coll = connect()

    user_id = request.args.get("id")

    if user_id is None:
        return jsonify("user not found")

    times_coll.update_one({"id": user_id}, {"$set": {"time": []}})

    return jsonify("deleteall")

@app.route('/', methods=['GET'])
def test():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    app.logger.info("hey")
    return "hello"

if __name__ == '__main__':
    app.run();
