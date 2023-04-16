from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from ..Kmeans.recommender import *
from ..Backend.combined_recommender import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
    # itinerary = show_itinerary(result, 'Reno, NV')  # hardcode city
    return userdata
    # return "success"

from dateutil import parser
@app.route('/createItinerary', methods=['POST'])
def createItinerary():
    # put data into list
    # userdata = []
    # for key in request.json:
    #     userdata.append(request.json[key])
    # # hardcode column 10 (point of interest) to 3
    # userdata.insert(9,3)
    # call recommend function in data.py to get activities
    # attractions = recommend(userdata)
    # call show_itinerary function in data.py to get streets
    # itinerary = show_itinerary(attractions, request.json['location'])  # hardcode city
    # return itinerary

    print(request.json)
    itinerary = generate_itinerary(request.json['dates'], request.json['boundingTimes'], request.json['price'], request.json['food'], request.json['attractions'], request.json['location'])
    return "success"

# @app.route('/food_recommend', methods=['POST'])
# def food_recommend():


if __name__ == '__main__':
    app.run()