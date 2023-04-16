
#%%
# install and import googlemaps api
#pip install googlemaps
import googlemaps
import requests
import datetime
from collections import defaultdict

#%%
api_key = 'AIzaSyDCLemo-47gI1JBA36-_YxMMRtc6ZG1qME'
# Base URL for Google Maps API
base_url = 'https://maps.googleapis.com/maps/api/place'

#%%
gmaps = googlemaps.Client(key=api_key)

#%%
# geocode an address
address = '1520 Valley Road, Reno, NV'
geocode_result = gmaps.geocode(address)
# Extract latitude and longitude
lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']

#%%
# search for restaurants 1km about address
location = str(lat) + "," + str(lng) 
radius = 1000
places_result = gmaps.places_nearby(location=location, radius=radius, type='restaurant')
places_result['results'][0] #found 20 results
address2 = places_result['results'][0]['vicinity']

#%%
# calculates distance between 2 addresses
directions_result = gmaps.directions(address, address2, mode="transit", departure_time=datetime.datetime.now())
directions_result[0]['legs'][0]['duration']['text']

#%%
address3 = "1664 North Virginia Street, Reno, NV"
addresses = [address, address2, address3]

#%%
def show_itinerary(locations):
    naddress = len(addresses) - 1
    for i in range(naddress):
        print(addresses[i], ':\t', end=' ')
        dirxn = gmaps.directions(addresses[i], addresses[i+1], mode="driving", departure_time=datetime.datetime.now())
        print(dirxn[0]['legs'][0]['duration']['text'], "drive:\t", end=' ')
    print(addresses[naddress])

#%%
show_itinerary(addresses)

all_users = dict()
def check_user_types(location, type):
    places_result = gmaps.places_nearby(location=location, type=type)
    for place in places_result['results']:
        reviews = place['reviews']
        for review in reviews:
            username = review['author_name']
            if all_users[username]:
                all_users[username].append()
            print(user_name)

# %%
def search_places(query, location=None, radius=None, types=None):
    url = f'{base_url}/textsearch/json'
    params = {
        'query': query,
        'key': api_key,
    }
    if location:
        params['location'] = f'{location[0]},{location[1]}'
    if radius:
        params['radius'] = radius
    if types:
        params['types'] = types

    response = requests.get(url, params=params)
    return response.json()


#%%
# Example usage
location = (37.4219999, -122.0840575)  # Coordinates for Googleplex
radius = 5000  # 5 km

#%%
# Nightlife locations
nightlife = search_places('nightlife', location, radius)
print(nightlife)

#%%
# Nature locations
parks = search_places('park', location, radius)
print(parks)

#%%
# Food places
restaurants = search_places('restaurant', location, radius)

#%%
# Historic sites
historic_sites = search_places('historic site', location, radius)

#%%
# Museums
museums = search_places('museum', location, radius)

#%%
# Zoos and aquariums
zoos_and_aquariums = search_places('zoo OR aquarium', location, radius)

#%%
# Universities
universities = search_places('university', location, radius)

#%%
# Shopping centers and markets
shopping_centers = search_places('shopping center OR market', location, radius)

#%%
# Tourist attractions
tourist_attractions = search_places('tourist attraction', location, radius)

#%%
# Heritage sites
heritage_sites = search_places('heritage site', location, radius)

#%%
# Entertainment parks
entertainment_parks = search_places('entertainment park', location, radius)

#%%
# Sports arenas
sports_arenas = search_places('sports arena', location, radius)

#%%
def get_directions(origin, destination, waypoints=None, mode='driving'):
    base_url = 'https://maps.googleapis.com/maps/api/directions/json'
    params = {
        'origin': f'{origin[0]},{origin[1]}',
        'destination': f'{destination[0]},{destination[1]}',
        'mode': mode,
        'key': api_key,
    }

    if waypoints:
        waypoints_str = '|'.join([f'via:{w[0]},{w[1]}' for w in waypoints])
        params['waypoints'] = waypoints_str

    response = requests.get(base_url, params=params)
    return response.json()

#%%
# Example usage
origin = (37.4219999, -122.0840575)  # Coordinates for Googleplex
destination = (37.7749, -122.4194)  # Coordinates for San Francisco
waypoints = [(37.4419, -122.1430), (37.4275, -122.1710)]  # Palo Alto, Menlo Park

directions = get_directions(origin, destination,waypoints)
print(directions)

#%%
yelp_api_key = "uKHpX0mEOm-8TaM_bYUQhQa-HkB1ykoQyg-EBYYuUlGevqUfLwcMdQIv-dILKX5m6gjtHLHR6uzHewgzuUwMnkYuyafA64caLJKgzerYdeBS5RjAgU8Po9bTFF46ZHYx"
# Base URL for Yelp Fusion API
yelp_base_url = "https://api.yelp.com/v3"


def search_yelp_businesses(term, location, categories=None,limit=50, offset=0):
    url = f"{yelp_base_url}/businesses/search"
    headers = {
        "Authorization": f"Bearer {yelp_api_key}"
    }
    params = {
        "term": term,
        "location": location,
        "limit": limit,
        "offset": offset,
    }
    if categories:
        params["categories"] = categories

    response = requests.get(url, headers=headers, params=params)
    return response.json()


def get_yelp_business_reviews(business_id):
    url = f"{yelp_base_url}/businesses/{business_id}/reviews"
    headers = {
        "Authorization": f"Bearer {yelp_api_key}"
    }
    response = requests.get(url, headers=headers)
    return response.json()


# List of the top 50 major cities in America
cities = [
    "New York, NY",
    # "Los Angeles, CA",
    # "Chicago, IL",
    # "Houston, TX",
    # "Phoenix, AZ",
    # "Philadelphia, PA",
    # "San Antonio, TX",
    # "San Diego, CA",
    # "Dallas, TX",
    # "San Jose, CA",
    # "Austin, TX",
    # "Jacksonville, FL",
    # "Fort Worth, TX",
    # "Columbus, OH",
    # "Charlotte, NC",
    # "San Francisco, CA",
    # "Indianapolis, IN",
    # "Seattle, WA",
    # "Denver, CO",
    # "Washington, DC",
    # "Boston, MA",
    # "El Paso, TX",
    # "Nashville, TN",
    # "Detroit, MI",
    # "Oklahoma City, OK",
    # "Portland, OR",
    # "Las Vegas, NV",
    # "Memphis, TN",
    # "Louisville, KY",
    # "Baltimore, MD",
    # "Milwaukee, WI",
    # "Albuquerque, NM",
    # "Tucson, AZ",
    # "Fresno, CA",
    # "Sacramento, CA",
    # "Mesa, AZ",
    # "Atlanta, GA",
    # "Kansas City, MO",
    # "Colorado Springs, CO",
    # "Omaha, NE",
    # "Raleigh, NC",
    # "Miami, FL",
    # "Long Beach, CA",
    # "Virginia Beach, VA",
    # "Oakland, CA",
    # "Minneapolis, MN",
    # "Tulsa, OK",
    # "Arlington, TX",
    # "Tampa, FL",
]

# Collect Yelp reviews for different types of places
yelp_place_types = {
    "restaurant": "restaurants"
}
reviews_by_type = defaultdict(list)

for city in cities:
    for place_type, category in yelp_place_types.items():
        businesses = search_yelp_businesses(term=place_type, location=city, categories=category, limit=50, offset=0)
        businessesTwo = search_yelp_businesses(term=place_type, location=city, categories=category, limit=50, offset=50)
        businessesThree = search_yelp_businesses(term=place_type, location=city, categories=category, limit=50, offset=100)
        businessesFour = search_yelp_businesses(term=place_type, location=city, categories=category, limit=50, offset=150)
        businessesFive = search_yelp_businesses(term=place_type, location=city, categories=category, limit=50, offset=200)
        businessesSix = search_yelp_businesses(term=place_type, location=city, categories=category, limit=50, offset=250)
        businesses.update(businessesTwo)
        businesses.update(businessesThree)
        businesses.update(businessesFour)
        businesses.update(businessesFive)
        businesses.update(businessesSix)

        # Add this check to ensure the "businesses" key is present
        if "businesses" in businesses:
            for business in businesses["businesses"]:
                business_id = business["id"]
                reviews = get_yelp_business_reviews(business_id)
                if "reviews" in reviews:  # Add this line to check for the "reviews" key
                    reviews_by_type[place_type].extend(reviews["reviews"])
                else:
                    print(reviews)
        else:
            print(businesses)


# Analyze reviews to find users who meet the criteria
users = defaultdict(lambda: defaultdict(list))
qualified_users = set()

for place_type, reviews in reviews_by_type.items():
    for review in reviews:
        author = review["user"]["name"]
        rating = review["rating"]
        users[author][place_type].append(rating)

        if all(place_type in user_reviews for place_type, user_reviews in users[author].items()):
            qualified_users.add(author)

# Compute the average review and total reviews for each qualified user
user_stats = {}

for user in qualified_users:
    user_stats[user] = {
        "average_rating": {},
        "total_reviews": {},
    }
    for place_type in yelp_place_types.keys():
        user_reviews = users[user][place_type]
        user_stats[user]["average_rating"][place_type] = sum(user_reviews) / len(user_reviews)
        user_stats[user]["total_reviews"][place_type] = len(user_reviews)

# Print the results
for user, stats in user_stats.items():
    print(f"User: {user}")
    for place_type in yelp_place_types:
        print(f"  {place_type.capitalize()}:")
        print(f"    Average rating: {stats['average_rating'][place_type]:.2f}")
        print(f"    Total reviews: {stats['total_reviews'][place_type]}")
    print()

#%%
type(businesses)