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

# Elbow method to find optimal number of clusters
wcss = [] # creating an empty list
for i in range(2,20): # for every value from 2 to 19:
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(Y)
    prediction=kmeans.predict(Y)
    wcss.append(kmeans.inertia_)
wcss

# Plot the elbow graph
plt.figure(figsize=(12,6))
plt.plot(range(2, 20), wcss, marker='o', c='orchid')
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Silhouette score
from sklearn import metrics
s_score = [] # create empty list
for i in range(2, 15): # for each value from 25 to 49:
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(Y)
    pred=kmeans.predict(Y)
    s_score.append(metrics.silhouette_score(Y, pred))
s_score

# Plot the silhouette score with our cluster value k = 6
kmeans = KMeans(n_clusters = 6, init = 'k-means++', random_state = 42)
ourFit = kmeans.fit(Y)
clusterCenters = ourFit.cluster_centers_

# Plot the silhouette score
plt.plot(range(2, 15), s_score, marker='o', c='coral')
plt.title('The Silhouette Score')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()