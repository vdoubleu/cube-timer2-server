from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify("hello")

if __name__ == '__main__':
    app.run();
