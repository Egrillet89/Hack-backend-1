from flask import Flask, request, jsonify

app = Flask(__name__)

alias_list = ["foo", "bar", "baz", "qux", "fred"]

@app.route('/h9', methods=['GET'])
def get_alias():
    alias = request.args.get('alias')
    if alias in alias_list:
        return jsonify({
            "payload": alias,
            "error": {"available": False, "err_msg": None},
            "status": 200
        })
    else:
        return jsonify({
            "payload": "not found",
            "error": {"available": False, "err_msg": None},
            "status": 404
        })

if __name__ == '__main__':
    app.run(debug=True)
