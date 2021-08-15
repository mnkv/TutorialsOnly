import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans 

from sklearn import metrics

digits = load_digits()
data = scale(digits.data) #scaling all of the features down

y = digits.target
sample_size = 300
k = len(np.unique(y)) #number of unique numbers in an array (not the repeats) dynamic ways

samples, features = data.shape 

#https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html
#scoring unsupervised learning algorithms
#don't need test and train data as this is unsupervised learning 
def bench_k_means(estimator, name, data):
    estimator.fit(data) 
    print( (name, estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_, metric='euclidean')))

clf = KMeans(n_clusters = k, init = 'k-means++', n_init = 10) #classifier settings
bench_k_means(clf, "1", data)
