from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from ..Kmeans.recommender import *

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

@app.route('/getActivities', methods=['POST'])
def getActivities():
    # put data into list
    userdata = []
    for key in request.json:
        userdata.append(request.json[key])
    # hardcode column 10 (point of interest) to 3
    userdata.insert(9,3)
    # call recommend function in data.py to get activities
    result = recommend(userdata)
    # call show_itinerary function in data.py to get streets
    itinerary = show_itinerary(result, 'Reno, NV')  # hardcode city
    return itinerary

# @app.route('/food_recommend', methods=['POST'])
# def food_recommend():
    # do nothing for now 

if __name__ == '__main__':
    app.run()