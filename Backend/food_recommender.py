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

# Load the data, scaler, and the pre-trained KMeans model
merged_columns = ['user_id','american', 'asian', 'mediterranean', 'latin', 'european','city']
data = pd.read_pickle('data.pkl')
data.columns = merged_columns
scaler = pickle.load(open('scaler.pkl', 'rb'))
kmeans = pickle.load(open("kmeansyelp.pkl", "rb"))
clust_data = pd.read_pickle('clust_data.pkl')
filtered_data = pd.read_csv('merged_filtered_data.csv')
feature_columns = ['american', 'asian', 'mediterranean', 'latin', 'european']


def get_price_level(place_id):
    place_details = gmaps.place(place_id)
    price_level = place_details.get('result', {}).get('price_level', None)
    return price_level


def get_restaurants_from_google_maps(suggestions, city, price_pref, count=3):
    coords = gmaps.places(query=city)['results'][0]['geometry']['location']
    location = f"{coords['lat']},{coords['lng']}"
    radius = 40000  # meters

    results = []
    for suggestion in suggestions:
        nearby_places = gmaps.places_nearby(location, radius, type=suggestion)

        for place in nearby_places['results']:
            if len(results) >= count:
                break

            place_id = place['place_id']
            price_level = get_price_level(place_id)

            if price_level == price_pref:
                results.append({
                    'name': place['name'],
                    'address': place['vicinity'],
                })

    return results


def recommend_users(city, target_user_ratings, n_neighbors=3):
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



def find_top_n_places(user_id, data, n, price_pref):
    user_data = data[data['user_id'] == user_id]
    top_n_places = user_data[user_data['price'] == price_pref].nlargest(n, 'stars')
    return top_n_places


def generate_itinerary(dates, bounding_times, price_pref, user_food_prefs, city):
    itinerary = {}
    nearest_neighbor_user_ids = recommend_users(city, user_food_prefs)

    for date in dates:
        itinerary[date] = []
        n_restaurants = 3

        # Iterate through the nearest neighbors
        for user_id in nearest_neighbor_user_ids:
            top_n_places = find_top_n_places(user_id, filtered_data, n_restaurants, price_pref)

            if top_n_places.empty or top_n_places[top_n_places['stars'] >= 3].empty:
                continue

            for _, place in top_n_places.iterrows():
                itinerary[date].append({
                    'name': place['name'],
                    'address': place['address'],
                })

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

            additional_restaurants = get_restaurants_from_google_maps(top_3_categories, city, price_pref, count=n_restaurants)
            itinerary[date].extend(additional_restaurants)

    return itinerary


# Main function to generate the itinerary
def main():
    start_date = datetime.strptime("2023-05-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-05-05", "%Y-%m-%d")
    bounding_times = ["7AM", "9PM"]
    price_pref = 2
    user_food_prefs = [1, 4, 3, 5, 1]
    city = "Reno"

    # Generate dates list
    dates = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end_date - start_date).days + 1)]

    itinerary = generate_itinerary(dates, bounding_times, price_pref, user_food_prefs, city)

    # Save itinerary to a JSON file
    with open("itinerary.json", "w") as f:
        json.dump(itinerary, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()

