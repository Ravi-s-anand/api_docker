from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    if(request.method == 'GET'):
        data = {"data": "Welcome to my Homepage"}
        return jsonify(data)



@app.route('/biodata', methods=['POST'])
def biodata():
    if(request.method == 'POST'):
        incoming_json_data = request.get_json()    
        name = incoming_json_data["name"]
        age = incoming_json_data["age"]
        data = {"data": f"My name is {name} and age is {age}."}
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")