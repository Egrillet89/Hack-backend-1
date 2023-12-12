from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/h8', methods=['POST'])
def post_endpoint():
    data = request.get_json()  
    email = data.get('email')
    name = data.get('name')
    response = {
        "payload": {"email": email, "name": name},
        "error": {"available": False, "err_msg": None},
        "status": 200
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
