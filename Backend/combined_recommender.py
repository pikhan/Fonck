import pandas as pd
import pickle
import numpy as np
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import BallTree
import googlemaps
import json
import warnings
warnings.filterwarnings("ignore")

gmaps = googlemaps.Client(key='AIzaSyDCLemo-47gI1JBA36-_YxMMRtc6ZG1qME')

# Load the data, scaler, and the pre-trained KMeans models
merged_columns = ['user_id','american', 'asian', 'mediterranean', 'latin', 'european','city']
data = pd.read_pickle('data.pkl')
data.columns = merged_columns
scaler = pickle.load(open('scaler.pkl', 'rb'))
kmeans = pickle.load(open("kmeansyelp.pkl", "rb"))
clust_data = pd.read_pickle('clust_data.pkl')
filtered_data = pd.read_csv('merged_filtered_data.csv')
feature_columns = ['american', 'asian', 'mediterranean', 'latin', 'european']

# reload saved kmeans data from file
fileAttractions = open('../Kmeans/important', 'rb')
kmeansAttractions, Y = pickle.load(fileAttractions)
fileAttractions.close()

# assess cluster groups
clust_data_Attractions = Y.groupby('cluster').mean()

def round_to_nearest_half_hour(time):
    minutes = (time.minute // 30) * 30
    rounded_time = time.replace(minute=minutes, second=0, microsecond=0)
    if time.minute % 30 >= 15:
        rounded_time += timedelta(minutes=30)
    return rounded_time

def compute_evenly_distributed_times(start_time_str, end_time_str, num_times=6):
    start_time = datetime.strptime(start_time_str, '%I:%M%p')
    end_time = datetime.strptime(end_time_str, '%I:%M%p')
    start_time += timedelta(hours=1)
    end_time -= timedelta(hours=1)
    total_duration = end_time - start_time
    time_step = total_duration / (num_times - 1)
    times = [start_time + (i * time_step) for i in range(num_times)]
    rounded_times = [round_to_nearest_half_hour(t) for t in times]
    formatted_times = [t.strftime('%I:%M%p') for t in rounded_times]
    return formatted_times


# function to return ranked location types for user
def recommendAttractions(userdata):
    test_user = Y.loc[0:1,]
    test_user.drop(1, inplace = True)
    test_user.drop('cluster', axis=1, inplace = True)
    test_user.loc[0] = userdata
    clust = kmeansAttractions.predict(test_user)
    clust = clust_data.loc[clust[0], ].sort_values(ascending=False)
    return list(clust.index)

# function to plan itinerary of specific places within 25 miles radius of choice city from ranked location types
# default is 3 places for a 1-day vacation (give input for places as 3*vacation_length)
def show_itineraryAttractions(suggestions, city, places=3, radius = 40000, recommended_places=None):
    coords = gmaps.places(query=city)['results'][0]['geometry']['location']
    location = str(coords['lat']) + "," + str(coords['lng'])
    
    # the choices (for top 5 place types) return multiple places for each below
    choices = []
    addresses = []
    ratedChoices = dict()
    for i in range(5):
        choices.append(gmaps.places_nearby(location, radius, type=suggestions[i]))
    
    # populate addresses of top destinations according to rating and recommended type
    j = 0
    while j < places:
        for i in range(len(choices)):
            if 'results' in choices[i] and len(choices[i]['results']) > 0:
                choice = choices[i]['results']
                k=0
                while k < places:
                    if choice[k]['place_id'] in recommended_places:
                        continue
                    rateKey = 'choice' + str(i)
                    if rateKey not in ratedChoices:
                        ratings = [choice[l]['rating'] for l in range(len(choice)) if 'rating' in choice[k]]
                        ratedChoices[rateKey] = np.argsort(np.array(ratings))
                    if len(ratedChoices[rateKey]) > 0:
                        recommended_places.add(choice[k]['place_id'])
                        addresses.append([choice[ratedChoices[rateKey][0]]['vicinity'], choice[ratedChoices[rateKey][0]]['name']])
                        ratedChoices[rateKey] = ratedChoices[rateKey][1:]
                        k += 1
        j += 1
    addresses = addresses[0:places]    

    return addresses

def formatAttractions(addresses, attraction_times, timeIndex):
    results = []
    for address in addresses:
        results.append({
            'name': address[1],
            'address': address[0],
            'time': attraction_times[timeIndex]
        })
        timeIndex +=1
        if timeIndex == 2:
            timeIndex=0
    return results, timeIndex

def get_price_level(place_id):
    place_details = gmaps.place(place_id)
    price_level = place_details.get('result', {}).get('price_level', None)
    return price_level


def get_restaurants_from_google_maps(suggestions, city, price_pref, count=3, recommended_places=None, food_times=None, timeIndex=None):
    if recommended_places is None:
        recommended_places = set()

    coords = gmaps.places(query=city)['results'][0]['geometry']['location']
    location = f"{coords['lat']},{coords['lng']}"
    radius = 40000  # meters

    results = []
    for suggestion in suggestions:
        if len(results) >= count:
            break

        nearby_places = gmaps.places_nearby(location, radius, type='restaurant', keyword=suggestion)

        for place in nearby_places['results']:
            if len(results) >= count:
                break

            place_id = place['place_id']
            if place_id in recommended_places:  # Check if the place_id is already in the recommended_places set
                continue

            price_level = get_price_level(place_id)


            if price_level == price_pref:
                results.append({
                    'name': place['name'],
                    'address': place['vicinity'],
                    'time': food_times[timeIndex]
                })
                recommended_places.add(place_id)  # Add the place_id to the recommended_places set
                timeIndex +=1
                if timeIndex == 2:
                    timeIndex=0

    return results, timeIndex

def get_attractions_from_google_maps(suggestions, city, count=3, recommended_places=None, attraction_times=None, timeIndex=None):
    if recommended_places is None:
        recommended_places = set()

    coords = gmaps.places(query=city)['results'][0]['geometry']['location']
    location = f"{coords['lat']},{coords['lng']}"
    radius = 40000  # meters

    results = []
    for suggestion in suggestions:
        if len(results) >= count:
            break

        nearby_places = gmaps.places_nearby(location, radius, type=suggestion)

        for place in nearby_places['results']:
            if len(results) >= count:
                break

            place_id = place['place_id']
            if place_id in recommended_places:  # Check if the place_id is already in the recommended_places set
                continue
            
            results.append({
                'name': place['name'],
                'address': place['vicinity'],
                'time': attraction_times[timeIndex]
            })
            recommended_places.add(place_id)  # Add the place_id to the recommended_places set
            timeIndex +=1
            if timeIndex == 2:
                timeIndex=0

    return results, timeIndex



def recommend_users(city, target_user_ratings, n_neighbors=6):
    # Load the data and the scaler
    data = pd.read_pickle('data.pkl')
    data.columns = merged_columns
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    
    # Filter the data to only include users from the desired city
    filtered_data = data[data['city'] == city]
    
    # Check if there are any samples in the filtered data
    if filtered_data.empty:
        return "No users found in the specified city."
    
    X_filtered = filtered_data[feature_columns].to_numpy()
    
    # Scale the filtered data and the target user's ratings
    X_scaled = scaler.transform(X_filtered)
    target_user_scaled = scaler.transform([target_user_ratings])

    # Build the BallTree and query it for the n nearest neighbors
    ball_tree = BallTree(X_scaled)
    _, indices = ball_tree.query(target_user_scaled, k=n_neighbors)

    # Get the nearest neighbors' user_ids using the index mapping from the filtered_data
    nearest_neighbor_user_ids = [filtered_data.iloc[index].user_id for index in indices[0]]

    return nearest_neighbor_user_ids



def find_top_n_places(user_id, data, n, price_pref,recommended_places):
    user_data = data[data['user_id'] == user_id]
    user_data = user_data[(user_data['price'] == price_pref) & (~user_data['business_id'].isin(recommended_places))]
    top_n_places = user_data.nlargest(n, 'stars')
    recommended_places.update(top_n_places['business_id'])
    return top_n_places


def generate_itinerary(dates, bounding_times, price_pref, user_food_prefs, user_attraction_prefs, city):
    timeIndex=0
    start_times = compute_evenly_distributed_times(bounding_times[0],bounding_times[1],6)
    food_times = [start_times[0],start_times[2],start_times[5]]
    attraction_times = [start_times[1],start_times[3],start_times[4]]

    recommended_places = set()
    itinerary = {}
    nearest_neighbor_user_ids = recommend_users(city, user_food_prefs)

    for date in dates:
        itinerary[date] = []
        n_restaurants = 3

        # Iterate through the nearest neighbors
        for user_id in nearest_neighbor_user_ids:
            top_n_places = find_top_n_places(user_id, filtered_data, n_restaurants, price_pref, recommended_places)

            if top_n_places.empty or top_n_places[top_n_places['stars'] >= 3].empty:
                continue

            for _, place in top_n_places.iterrows():
                itinerary[date].append({
                    'name': place['name'],
                    'address': place['address'],
                    'time': food_times[timeIndex]
                })
                timeIndex += 1
                if timeIndex == 2:
                    timeIndex = 0

                n_restaurants -= 1
                if n_restaurants <= 0:
                    break

            if n_restaurants <= 0:
                break

        # If there are not enough restaurants, use the K-means/Google Maps method
        if n_restaurants > 0:
            test_user = pd.Series(user_food_prefs, index=clust_data.columns)
            clust = kmeans.predict(test_user.values.reshape(1, -1))
            top_3_categories = clust_data.loc[clust[0], :].sort_values(ascending=False)[0:3].index
            additional_restaurants, timeIndex = get_restaurants_from_google_maps(top_3_categories, city, price_pref, n_restaurants,recommended_places, food_times, timeIndex)
            itinerary[date].extend(additional_restaurants)
        
        ourSuggestions=recommendAttractions(user_attraction_prefs)
        #ourAttractions=show_itineraryAttractions(ourSuggestions,city,3,40000,recommended_places)
        #ourFormattedAttractions=formatAttractions(ourAttractions,attraction_times,timeIndex)
        ourLameAttractions, timeIndex=get_attractions_from_google_maps(ourSuggestions,city,3,recommended_places,attraction_times,timeIndex)
        itinerary[date].extend(ourLameAttractions)

    return itinerary


# Main function to generate the itinerary
def main():
    start_date = datetime.strptime("2023-05-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-05-05", "%Y-%m-%d")
    bounding_times = ["7:00AM", "9:00PM"]
    price_pref = 2
    user_food_prefs = [1, 4, 3, 5, 1]
    user_attraction_prefs = [2, 3, 4, 1, 3, 3, 5, 2, 1, 3, 2, 2]
    city = "Reno"

    # Generate dates list
    dates = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end_date - start_date).days + 1)]

    itinerary = generate_itinerary(dates, bounding_times, price_pref, user_food_prefs, user_attraction_prefs, city)

    # Save itinerary to a JSON file
    with open("itinerary.json", "w", encoding='utf-8') as f:
        json.dump(itinerary, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()

