import pandas as pd
from sklearn.cluster import KMeans
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

# assess cluster groups
clust_data = Y.groupby('cluster').mean()

def recommend(userdata):
    test_user = Y.loc[0:1,]
    test_user.drop(1, inplace = True)
    test_user.drop('cluster', axis=1, inplace = True)
    test_user.loc[0] = userdata
    clust = kmeans.predict(test_user)
    clust = clust_data.loc[clust[0], ].sort_values(ascending=False)
    return clust[0:3].index
