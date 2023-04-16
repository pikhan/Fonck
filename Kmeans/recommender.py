# install and import googlemaps api
#pip install googlemaps
import googlemaps
import pickle
import numpy as np
# ignore warnings
import warnings
warnings.filterwarnings("ignore")
# For silhouette score

gmaps = googlemaps.Client(key='AIzaSyDCLemo-47gI1JBA36-_YxMMRtc6ZG1qME')

# reload saved kmeans data from file
file = open('C:/Users/Johanson Onyegbula/Documents/Masters in NRES/Spring 2023/Hackathon/Fonck/Kmeans/important', 'rb')
kmeans, Y = pickle.load(file)
file.close()

# assess cluster groups
clust_data = Y.groupby('cluster').mean()

# function to return ranked location types for user
def recommend(userdata):
    test_user = Y.loc[0:1,]
    test_user.drop(1, inplace = True)
    test_user.drop('cluster', axis=1, inplace = True)
    test_user.loc[0] = userdata
    clust = kmeans.predict(test_user)
    clust = clust_data.loc[clust[0], ].sort_values(ascending=False)
    return clust.index

# ['movie_theater', 'art_gallery', 'clothing_store', 'university', 'bar', 'shopping_mall', 'museum', 'stadium', 'zoo', 'point_of_interest', 'tourist_attraction', 'park']

#recommend for a user rating  who rates park as 4, and shopping mall as 5
recommend([3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 4])
#recommend for a user rating  who rates movie theater, stadium and art gallery as 5 each
rankings = [5, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3]
suggestions = recommend(rankings)

# function to plan itinerary of specific places within 25 miles radius of choice city from ranked location types
# default is 3 places for a 1-day vacation (give input for places as 3*vacation_length)
def show_itinerary(suggestions, city, places=3, radius = 40000):
    coords = gmaps.places(query=city)['results'][0]['geometry']['location']
    location = str(coords['lat']) + "," + str(coords['lng'])
    
    # the choices (for top 6 place types) return multiple places for each below
    choices = []
    addresses = []
    ratedChoices = dict()
    for i in range(6):
        choices.append(gmaps.places_nearby(location, radius, type=suggestions[i]))
    
    # populate addresses of top destinations according to rating and recommended type
    j = 0
    while j < places:
        for i in range(len(choices)):
            if 'results' in choices[i] and len(choices[i]['results']) > 0:
                choice = choices[i]['results']
                rateKey = 'choice' + str(i)
                if rateKey not in ratedChoices:
                    ratings = [choice[i]['rating'] for i in range(len(choice)) if 'rating' in choice[i]]
                    ratedChoices[rateKey] = np.argsort(np.array(ratings))
                if len(ratedChoices[rateKey]) > 0:
                    addresses.append([choice[ratedChoices[rateKey][0]]['vicinity'], choice[ratedChoices[rateKey][0]]['name']])
                    ratedChoices[rateKey] = ratedChoices[rateKey][1:]
        j += 1
    addresses = addresses[0:places]
    
    return addresses

city = 'San Francisco, CA'
itinerary = show_itinerary(suggestions, city, 9)    #3-day vacation
print(itinerary)
