from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/h3', methods=['PUT'])
def put_method():
    if request.method == 'PUT':
        return jsonify({"payload":"put"}), 200

if __name__ == '__main__':
    app.run(debug=True)
