import googlemaps
import requests
import json

api_key = 'AIzaSyDCLemo-47gI1JBA36-_YxMMRtc6ZG1qME'
gmaps = googlemaps.Client(key=api_key)
address = '1600 Amphitheatre Parkway, Mountain View, CA'
geocode_result = gmaps.geocode(address)
# Extract latitude and longitude
lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']

location = str(lat) + "," + str(lng) 
radius = 1000
places_result = gmaps.places_nearby(location=location, radius=radius, type='restaurant')
print(places_result['results'][0])

radius = 1000
places_result = gmaps.places_nearby(location=location, radius=radius, type='restaurant')
print(places_result['results'][0])

#%%
import requests
import lxml.html as lh
import pandas as pd
import re

#%%
base_page = "https://tripadvisor.ca"
def get_tours(tour_category):
    html = open("htmlpages/"+tour_category+".txt",'r',encoding='utf-8').read()
    tree = lh.fromstring(html)
    
    attractions = tree.xpath('//div[@class="listing attraction_element"]//div[@class="listing_title"]/a/@onclick')    
    attractions = [base_page+attraction.split(';')[-2].split(',')[2][2:-1] for attraction in attractions]
   
    next_attractions = list()
    if tree.xpath("//div[@class='unified pagination ']"):
        next_page_container = tree.xpath("//div[@class='unified pagination ']")[0]
        if next_page_container.xpath("./span/@class") != ["nav next disabled"]:
            next_page = base_page+next_page_container.xpath("./a[@class='nav next rndBtn ui_button primary taLnk']/@href")[0]
            page_no = next_page_container.xpath("./a[@class='nav next rndBtn ui_button primary taLnk']/@data-page-number")[0]
            page = requests.get(next_page)
            if bool(re.search(r'\d',tour_category)):
                file_name = re.sub(r'\d+','',tour_category)+str(page_no)
            else:
                file_name = tour_category+str(page_no)
            open("htmlpages/"+file_name+".txt",'wb').write(page.content)
            next_attractions = get_tours(file_name)
    
    if len(next_attractions) != 0:
        attractions += next_attractions
    
    return attractions
#%%
# get categories of tours and corresponding links
def categories():
    html = open('htmlpages/city_tours.txt','r').read()
    tree = lh.fromstring(html)
    cat = tree.xpath('//div[@class="filter_list_0"]')[0]
    tour_categories = cat.xpath('./div/label/a/text()')
    category_links = cat.xpath('./div/label/a/@href')
    if cat.xpath('./div[@class="collapse hidden"]'):
        tour_categories += cat.xpath('./div[@class="collapse hidden"]/div/label/a/text()')
        category_links += cat.xpath('./div[@class="collapse hidden"]/div/label/a/@href')
    category_links = [base_page+x for x in category_links]
    tour_categories = ['_'.join(x.split(' ')[:-1]).lower() for x in tour_categories]
    attraction = list()
    attraction_category = list()
    for i in range(len(tour_categories)):
        print(tour_categories[i])
        print(category_links[i])
        page = requests.get(category_links[i])
        open("htmlpages/"+tour_categories[i]+".txt",'wb').write(page.content)
        output = get_tours(tour_categories[i])
        print(len(output))
        attraction += output
        attraction_category += [tour_categories[i] for x in range(len(output))]
    df = pd.DataFrame({'attraction': attraction,'category': attraction_category})
    df.to_json('outputs/attractions_cat.json',orient='records',index=True)

#%%
# downloading and saving city tours and tickets page
def scrape(url):
    page = requests.get(url)
    html = page.content
    open('htmlpages/city_tours.txt','wb').write(html)
    categories()
#%%
scrape('https://www.tripadvisor.ca/Attraction_Products-g153339-zfd1,60-zfm0,10-a_hsf.21946-Canada.html')

#%%
import numpy as np, pandas as pd, seaborn as sns, matplotlib.pyplot as plt

# Load data
ratings_data = pd.read_csv("C:/Users/ibrah/Downloads/google_review_ratings.csv")
ratings_data.head()

# Data preprocessing
ratings_data.info()
ratings_data.describe()

# build model
from sklearn.cluster import KMeans
X = ratings_data.drop('User', axis=1)
X.dropna(inplace=True, how='all', axis=1)
#%%
X['Category 11'] = X['Category 11'].astype(float)
#%%
X.dropna(inplace=True, how='all', axis=1)
X.info()
#kmeans = KMeans(n_clusters=2, init='k-means++', random_state=42)
#kmeans.fit(X)

#%%
import json

business_mapping = {}

# Process businesses.json line by line
with open("C:/Users/ibrah/Downloads/yelp_dataset/yelp_dataset/yelp_academic_dataset_business.json", "r", encoding="utf-8") as businesses_file:
    for line in businesses_file:
        business = json.loads(line)
        business_mapping[business["business_id"]] = business

# Process reviews.json and create output_data.json
with open("C:/Users/ibrah/Downloads/yelp_dataset/yelp_dataset/yelp_academic_dataset_review.json", "r", encoding="utf-8") as reviews_file, open("output_data.json", "w") as jsonfile:
    jsonfile.write("[")
    first_row = True

    for line in reviews_file:
        review = json.loads(line)
        user_id = review["user_id"]
        stars = review["stars"]
        business_id = review["business_id"]

        if business_id in business_mapping:
            business = business_mapping[business_id]
            name = business["name"]
            address = business["address"]
            city = business["city"]
            state = business["state"]
            category = business["categories"]

            row = {
                "user_id": user_id,
                "stars": stars,
                "business_id": business_id,
                "name": name,
                "address": address,
                "city": city,
                "state": state,
                "categories": category,
            }

            if not first_row:
                jsonfile.write(",")

            json.dump(row, jsonfile)
            first_row = False

    jsonfile.write("]")

#%%
import pandas as pd
df= pd.read_json("output_data.json")
df.to_csv("output_data.csv")

#%%
# Read the .csv file
data = pd.read_csv('output_data.csv')

# Filter the rows based on the conditions
filtered_data = data[data['categories'].str.contains('Restaurants') & data['categories'].str.contains('Food') & data['categories'].str.contains('Nightlife')]

# Save the filtered data into a new .csv file
filtered_data.to_csv('filtered_data.csv', index=False)

#%%
# Read the .csv file
data = pd.read_csv('filtered_data.csv')


# Define the category groups
american_categories = ['American','Southern', 'Australian', 'Barbecue', 'Brasseries', 'Breakfast & Brunch', 'Pancakes', 'Pizza', 'Burgers', 'Cafes', 'Cafeteria', 'Cheesesteaks', 'Chicken', 'Comfort', 'Delis', 'Dinner Theater', 'Fast Food', 'Gastropubs', 'Hot Dogs', 'Poutineries', 'Salad', 'Sandwiches', 'Tex-Mex','Waffles', 'Wraps', 'Food']
asian_categories = ['Asian', 'Taiwanese','Vietnamese', 'Thai', 'Uzbek', 'Sri Lankan', 'Bubble Tea', 'Poke', 'Bangladeshi', 'Indian', 'Asian', 'Burmese','Cambodian','Chinese','Cantonese', 'Dim Sum','Hainan','Shanghainese','Szechuan', 'Filipino','Polynesian', 'Guamanaian','Hawaiian','Himalayan','Nepalese', 'Hong Kong Style', 'Hot Pot', 'Indonesian', 'Malaysian','Sushi','Japanese','Korean','Ramen','Curry','Laotian','Mongolian', 'Noodles', 'Pan Asia']  # Add other Asian categories here
mediterranean_categories = ['Mediterranean', 'Syrian', 'Afghan', 'African', 'Senegalese', 'Arabian','Armenian', 'Eritrean','Ethiopian','Halal','Middle Eastern','Kebab', 'Pakistani','Somali']  # Add other Mediterranean categories here
latin_categories = ['Latin', 'Argentine','Brazilian','Cajun','Creole','Caribbean','Dominican','Haitian','Puerto Rican','Trinidadian','Cuban','Honduran','Latin', 'Colombian','Salvadoran','Venezuelan','Peruvian', 'Mexican', 'Nicaraguan']  # Add other Latin categories here
european_categories = ['European', 'Armenian','Ukrainian', 'Austrian', 'Basque', 'Belgian','British','Bulgarian','Catalan','Czech', 'French', 'Georgian','German', 'Greek', 'Iberian', 'Italian','Portuguese','Russian','Scandinavian','Slovakian']  # Add other European categories here
#nightlife_categories = ['Nightlife', 'Bars', 'Nightclubs']


# Define a function to calculate the mean stars for each category group
def mean_stars_by_category(data, categories):
    filtered_data = data[data['categories'].apply(lambda x: any(keyword in x for keyword in categories))]
    return filtered_data.groupby('user_id')['stars'].mean()

# Calculate the mean stars for each category group
american_stars = mean_stars_by_category(data, american_categories)
asian_stars = mean_stars_by_category(data, asian_categories)
mediterranean_stars = mean_stars_by_category(data, mediterranean_categories)
latin_stars = mean_stars_by_category(data, latin_categories)
european_stars = mean_stars_by_category(data, european_categories)
#nightlife_stars = mean_stars_by_category(data, nightlife_categories)

# Combine the results into a single DataFrame
grouped_data = pd.concat(
    [american_stars, asian_stars, mediterranean_stars, latin_stars, european_stars],#, nightlife_stars],
    axis=1,
    keys=['american', 'asian', 'mediterranean', 'latin', 'european']#, 'nightlife']
)

# Calculate the overall mean stars for each category group
overall_mean_stars = {
    'american': american_stars.mean(),
    'asian': asian_stars.mean(),
    'mediterranean': mediterranean_stars.mean(),
    'latin': latin_stars.mean(),
    'european': european_stars.mean(),
    #'nightlife': nightlife_stars.mean(),
}

# Replace NaN values with the overall mean stars for each category group
for category, mean_stars in overall_mean_stars.items():
    grouped_data[category].fillna(mean_stars, inplace=True)

# Reset the index
grouped_data.reset_index(inplace=True)

# Save the grouped data into a new .csv file
grouped_data.to_csv('yelp_food.csv', index=False)

#%%
import numpy as np, pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Load data
path = 'yelp_food.csv'
data = pd.read_csv(path)

# Data preprocessing
X = data.drop(data.columns[0], axis=1) # drop columns 0
Y = X.dropna(axis=1, how='all') # drop empty columns
Y.info()
Y.describe()

# For silhouette score
from sklearn import metrics

kmeans = KMeans(n_clusters=20, init='k-means++', random_state=42)
ourFit=kmeans.fit(Y)
#prediction=kmeans.predict(Y)
#print(metrics.silhouette_score(Y, prediction))

#%%
print(ourFit.cluster_centers_)

#%%
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import BallTree

# Load the data
data = pd.read_csv('yelp_food.csv')
# Load the filtered_data.csv
filtered_data = pd.read_csv('filtered_data.csv')

# Extract user location data by grouping by user_id and selecting the first city for each user
user_location_data = filtered_data.groupby('user_id')['city'].first().reset_index()

# Merge user location data with the grouped data
merged_data = data.merge(user_location_data, on='user_id')
# Save the merged data into a new .csv file
merged_data.to_csv('merged_data.csv', index=False)

#%%
data = pd.read_csv('merged_data.csv')
# Extract the feature columns (ratings for each category group)
feature_columns = ['american', 'asian', 'mediterranean', 'latin', 'european']
X = data[feature_columns]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the Ball Tree model
ball_tree = BallTree(X_scaled, metric='euclidean')

# Save the Ball Tree, the data, and the scaler for future use
import pickle
pickle.dump(ball_tree, open('ball_tree.pkl', 'wb'))
data.to_pickle('data.pkl')
pickle.dump(scaler, open('scaler.pkl', 'wb'))

#%%
import pandas as pd
import pickle
import numpy as np

def recommend_user(city, target_user_ratings):
    # Load the data and the scaler
    data = pd.read_pickle('data.pkl')
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
    
    # Compute the Euclidean distances between the target user and the filtered data
    distances = np.sqrt(np.sum((X_scaled - target_user_scaled)**2, axis=1))
    
    # Find the index of the nearest neighbor
    nearest_neighbor_index = np.argmin(distances)
    
    # Get the nearest neighbor's user_id
    nearest_neighbor_user_id = filtered_data.iloc[nearest_neighbor_index]['user_id']
    
    return nearest_neighbor_user_id


def find_top_3_places(user_id, data):
    # Filter the dataset to only include rows with the given user_id
    user_data = data[data['user_id'] == user_id]
    
    # Find the top 3 highest-rated places using nlargest()
    top_3_places = user_data.nlargest(3, 'stars')
    
    return top_3_places

# Load the filtered_data.csv
filtered_data = pd.read_csv('filtered_data.csv')






city = 'Reno'
target_user_ratings = [2,4,3,3,2]  # Replace with the actual ratings of the target user
nearest_neighbor_user_id = recommend_user(city, target_user_ratings)
# Define the target user_id
target_user_id = nearest_neighbor_user_id

# Find the top 3 highest-rated places for the given user_id at runtime
top_3_places = find_top_3_places(target_user_id, filtered_data)
print("The user_id with the closest preference in", city, "is:", nearest_neighbor_user_id)
print("They recommend: ", top_3_places)