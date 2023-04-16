from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route('/add', methods=['POST'])
def add():
    num1 = request.json['num1']
    num2 = request.json['num2']
    result = num1 + num2
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()