from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/h5', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return jsonify({"payload":"success", "error": False})
    else:
        return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)
