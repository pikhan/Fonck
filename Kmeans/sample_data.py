# install and import googlemaps api
#pip install googlemaps
import googlemaps
import pickle
import requests
import json
import datetime
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
# ignore warnings
import warnings
warnings.filterwarnings("ignore")
# For silhouette score
from sklearn import metrics

gmaps = googlemaps.Client(key='AIzaSyDCLemo-47gI1JBA36-_YxMMRtc6ZG1qME')

# geocode an address
address = '1520 Valley Road, Reno, NV'
geocode_result = gmaps.geocode(address)
# Extract latitude and longitude
lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']

# search for restaurants 1km about address
location = str(lat) + "," + str(lng) 
radius = 1000
places_result = gmaps.places_nearby(location=location, radius=radius, type='restaurant')
places_result['results'][0] #found 20 results

# calculates distance between 2 addresses
directions_result = gmaps.directions(address, places_result['results'][0]['vicinity'], mode="transit", departure_time=datetime.datetime.now())
directions_result[0]['legs'][0]['duration']['text']

all_places = gmaps.places_nearby(location="San Francisco, CA", type='restaurant')
all_places = gmaps.places()

yelp_api_key = "tVZIbPkyz21fZXG6u2LAh8n7me8NRVNMBf_WcKN2BK18y5phm-p5mARRploxSK-RO3VAo9n9fjnSF6601yJY_AF397eGeuKz4vvAIt6LtVj5HpOToW2DW7STnVE6ZHYx" 

# Base URL for Yelp Fusion API
yelp_base_url = "https://api.yelp.com/v3"

def search_yelp_businesses(location, term=None, categories=None, limit=50, offset=0):
    url = f"{yelp_base_url}/businesses/search"
    headers = {
        "Authorization": f"Bearer {yelp_api_key}"
    }
    params = {
        "location": location,
        "limit": limit,
        "offset": offset,
    }
    if term:
        params['term'] = term
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


# Define the location and search term for the search
location = 'San Francisco, CA'
term = 'restaurants'

# Send an HTTP GET request to the API and get the response
response = search_yelp_businesses(location, term)

# Parse the JSON response and print the names of the businesses
businesses = json.loads(response.text)['businesses']
for business in businesses:
    print(business['name'])

json_data = open("C:/Users/Johanson Onyegbula/Documents/Masters in NRES/Spring 2023/Hackathon/Fonck/all_atl_reviews.json")
data1 = json.load(json_data)
n = len(data1)
myplaces = dict()
df = pd.DataFrame(columns = ['User_ID', 'Username', 'Rating', 'Location_Type'])

# convert json data to dataframe for each user's review
for i in range(n):
    mydata = data1[i]
    pl_name = mydata['activity_name']
    if pl_name not in myplaces:
        place_detail = gmaps.places(query = pl_name)
        myrating, place_type, totalrating = None, None, None
        if 'results' and (len(place_detail['results']) > 0) in place_detail:
            place_detail = place_detail['results'][0]
            if 'rating' in place_detail:
                myrating = place_detail['rating']
            if 'types' in place_detail:
                place_type = place_detail['types']
            if 'user_ratings_total' in place_detail:
                totalrating = place_detail['user_ratings_total']
        myplaces[pl_name] = [myrating, place_type, totalrating]
    else:
        place_type = myplaces[pl_name][1]
    df.loc[i] = [mydata['userid'], mydata['username'], mydata['star_rating'], place_type]

# extract all unique place types from data frame
alltypes = set()
for i in range(n):
    mytype = df.iloc[i, 3]
    if mytype and mytype[0] not in alltypes:
        alltypes.add(mytype[0])

# get the specific types from the location type
df['Type'] = df['Location_Type']
for i in range(n):
    val = df.iloc[i, 4]
    if val:
        val = val[0]
    df.at[i, 'Type'] = val

# remove unwanted types
df.groupby(['Type']).count()
mytypes = alltypes.copy()
mytypes.remove('travel_agency')

df1 = df.copy()

# give an average rating to each place by default
for place in mytypes:
    df[place] = 3

#create categories for each row and assign rating to the relevant type
for i in range(n):
    rate = df.iloc[i, 2]
    mytype = df.iloc[i, 4]
    if rate and mytype in mytypes:
        df.at[i, mytype] = rate

# drop unchosen rows
for i in range(n-1, -1, -1):
    mytype = df.iloc[i, 4]
    if mytype not in mytypes:
        df.drop(i, inplace=True)

df.to_csv("C:/Users/Johanson Onyegbula/Documents/Masters in NRES/Spring 2023/Hackathon/Fonck/processed_reviews.csv", index=False)

# Load data
path = 'C:/Users/Johanson Onyegbula/Documents/Masters in NRES/Spring 2023/Hackathon/Fonck/Kmeans/processed_reviews.csv'
data = pd.read_csv(path)

# Data preprocessing
X = data.drop(data.columns[0:5], axis=1) # drop columns 0 through 5
Y = X.dropna(axis=1, how='all') # drop empty columns
Y.info()
Y.describe()

# Elbow method to find optimal number of clusters
wcss = [] # creating an empty list
s_score = [] # create empty list
for i in range(2,20): # for every value from 2 to 19:
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    prediction=kmeans.predict(X)
    wcss.append(kmeans.inertia_)
    s_score.append(metrics.silhouette_score(X, prediction))
wcss
s_score

# Plot the elbow graph
plt.figure(figsize=(12,6))
plt.plot(range(2, 20), wcss, marker='o', c='orchid')
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Plot the silhouette score
plt.plot(range(2, 20), s_score, marker='o', c='coral')
plt.title('The Silhouette Score')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# choose 6 clusters
kmeans = KMeans(n_clusters=6, init='k-means++', random_state=42)
ourFit = kmeans.fit(Y)
pred = kmeans.predict(Y)
Y['cluster'] = pred

# save kmeans data
file = open('C:/Users/Johanson Onyegbula/Documents/Masters in NRES/Spring 2023/Hackathon/Fonck/Kmeans/important', 'wb')
pickle.dump([kmeans, Y], file)
file.close()

'''
# calculates driving times between consecutive places in the itinerary
orig_dest_pairs = []
naddress = len(addresses)
for i in range(naddress-1):
    orig_dest_pairs.append((addresses[i][0], addresses[i+1][0]))

itinerary = "From "
for i in range(math.ceil(naddress/25)):
    itinerary += addresses[i][0] + " (" + addresses[i][1] + "):\t "
    dirxn = gmaps.directions(addresses[i][0], addresses[i+1][0], mode="driving", departure_time=datetime.datetime.now())
    itinerary += dirxn[0]['legs'][0]['duration']['text'] + " drive to:\t "
itinerary += addresses[naddress][0] + " (" + addresses[naddress][1] + ")"
'''
