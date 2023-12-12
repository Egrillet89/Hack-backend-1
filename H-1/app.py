from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/h1', methods=['GET'])
def get_payload():
    return jsonify({"payload": "get"})

if __name__ == '__main__':
    app.run(debug=True)

