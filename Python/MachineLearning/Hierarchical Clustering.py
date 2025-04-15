# an unsupervised (doesnt need training or target value) method for clustering
# data points. the algorithm builds clusters by measuring the dissimilarities between data.

# can be used on any data to visualize and interpret the relationship between
# individual data points

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# works for any number of variables
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# compute the ward linkage using euclidean distance, and visualize it using a dendrogram:
data = list(zip(x,y))

# use simple euclidean distance measure and ward's linkage which seeks to minimize
# the variance between clusters
linkage_data = linkage(data, method='ward', metric='euclidean')
dendrogram(linkage_data)

plt.show()

hierarchical_cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels = hierarchical_cluster.fit_predict(data)
print(labels)

plt.scatter(x,y,c=labels)
plt.show()

# how to read dendrogram:
# height of branch (clades aka the points that split into leaves) points
# indicates similarities between leaves; greater height = greater difference

# arrangement of clades indicates which leaves are most similar to each other
# horizontal orientation is irrelevant; whats important is which leaves are
# branched together and how tall they are
