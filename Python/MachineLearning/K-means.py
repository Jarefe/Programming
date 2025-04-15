# k means is an unsupervised learning method for clustering data points
# the algorithm iteratively divides data points into k clusters by 
# minimizing the variance in each cluster

# each data point is randomly assigned to one of the k clusters, then the 
# centroid (the center) of each cluster is computed, and each data point is assigned
# to the cluster with the closest centroid. this process repeats until data
# assignments no longer change

import matplotlib.pyplot as plt

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

plt.scatter(x, y)
plt.show()

from sklearn.cluster import KMeans

data = list(zip(x,y))
inertias = []

# elbow method graphs the inertia and visualizes the point where data starts
# decreasing linearly; this point is the elbow and is a good estimate for k
for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# result shows that 2 is a good value for K, so retrain and visualize result
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x,y, c=kmeans.labels_)
plt.show()