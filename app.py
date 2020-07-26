from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    name = request.args.get("name", None)

    return jsonify(name)

if __name__ == '__main__':
    app.run();
