import numpy as np, pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Load data
path = 'Kmeans/processed_reviews.csv'
data = pd.read_csv(path)

# Data preprocessing
X = data.drop(data.columns[0:5], axis=1) # drop columns 0 through 5
Y = X.dropna(axis=1, how='all') # drop empty columns
Y.info()
Y.describe()

# For silhouette score
from sklearn import metrics

# Elbow method to find optimal number of clusters
wcss = [] # creating an empty list
s_score = [] # create empty list
for i in range(2,20): # for every value from 2 to 19:
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(Y)
    prediction=kmeans.predict(Y)
    wcss.append(kmeans.inertia_)
    s_score.append(metrics.silhouette_score(Y, prediction))
wcss
s_score

# Plot the elbow graph
# plt.figure(figsize=(12,6))
# plt.plot(range(2, 20), wcss, marker='o', c='orchid')
# plt.title('The Elbow Method')
# plt.xlabel('Number of Clusters')
# plt.ylabel('WCSS')
# plt.show()


# Plot the silhouette score
# plt.plot(range(2, 20), s_score, marker='o', c='coral')
# plt.title('The Silhouette Score')
# plt.xlabel('Number of Clusters')
# plt.ylabel('Silhouette Score')
# plt.show()

# choose 6 clusters
kmeans = KMeans(n_clusters=6, init='k-means++', random_state=42)
kmeans.fit(Y)
pred = kmeans.predict(Y)
Y['cluster'] = pred

# assess cluster groups
clust_data = Y.groupby('cluster').mean()

def recommend(userdata):
    test_user = Y.loc[0:1,]
    test_user.drop(1, inplace = True)
    test_user.drop('cluster', axis=1, inplace = True)
    test_user.loc[0] = userdata
    clust = kmeans.predict(test_user)
    clust = clust_data.loc[clust[0], ].sort_values(ascending=False)
    print(clust[0:3].index)
    return clust[0:3].index

# ['movie_theater', 'art_gallery', 'clothing_store', 'university', 'bar', 'shopping_mall', 'museum', 'stadium', 'zoo', 'point_of_interest', 'tourist_attraction', 'park']

#recommend for a user rating  who rates park as 4, and shopping mall as 5
recommend([2.5, 2.5, 2.5, 2.5, 2.5, 5, 2.5, 2.5, 2.5, 2.5, 2.5, 4])
#recommend for a user rating  who rates movie theater, stadium and art gallery as 5 each
recommend([5, 5, 2.5, 2.5, 2.5, 2.5, 2.5, 5, 2.5, 2.5, 2.5, 2.5])[0:2]
