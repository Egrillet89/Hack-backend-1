from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/h6', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_request():
    method = request.method
    if method in ['GET', 'POST', 'PUT', 'DELETE']:
        return jsonify({"method": method, "payload": "success", "error": False})
    else:
        return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)
