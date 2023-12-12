from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/h7', methods=['GET'])
def get_data():
    email = request.args.get('email')
    name = request.args.get('name')
    if email is None or name is None:
        return jsonify({
            "payload": {},
            "error": {"available": True, "err_msg": "Faltan parámetros"},
            "status": 400
        })
    else:
        return jsonify({
            "payload": {"email": email, "name": name},
            "error": {"available": False, "err_msg": None},
            "status": 200
        })

if __name__ == '__main__':
    app.run(debug=True)
