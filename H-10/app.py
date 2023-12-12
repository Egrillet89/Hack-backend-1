from flask import Flask, request, jsonify

app = Flask(__name__)

alias_list = ["foo", "bar", "baz", "qux", "fred"]

@app.route('/h10', methods=['POST'])
def check_alias():
    alias = request.json.get('alias')
    
    if alias in alias_list:
        return jsonify(payload=alias), 200
    else:
        return jsonify(payload="not found"), 404

if __name__ == '__main__':
    app.run(debug=True)
