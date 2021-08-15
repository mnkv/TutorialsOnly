# KNN k-nearest neighbours algorithm
# collecting irregular data 

import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 
import numpy as np 
from sklearn import linear_model, preprocessing

#read data

data = pd.read_csv('car.data')
#print(data.head())

# converge non-numerical data to numerical


le = preprocessing.LabelEncoder() # importing pre-processing object that will re-label strings into numerical values (see below)
buying = le.fit_transform(list(data['buying'])) # takes string labels and encodes them into appropriate integer subject
maint = le.fit_transform(list(data['maint']))
lug_boot = le.fit_transform(list(data['lug_boot']))
safety = le.fit_transform(list(data['safety']))
persons = le.fit_transform(list(data['persons']))
door = le.fit_transform(list(data['door']))
class_ = le.fit_transform(list(data['class']))
# returns numpy array
#print(buying)

predict = 'class'

X = list(zip(buying, maint, door, persons, lug_boot, safety)) #feature, zip - creates a tuple object for all the features
y = list(class_) #label

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1) #taking some values for training and some for test from X and Y, test_size 10% of the data is taken for testing

print(x_train, y_test)

# model limitation: needs to compute distances to a point every time the prediction is made, in contrast to regression which is described as a function

model = KNeighborsClassifier(n_neighbors = 9)
model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

predicted = model.predict(x_test)
names = ['acc', 'good', 'unacc' , 'vgood']

for x in range(len(x_test)):
    print('Predicted: ', names[predicted[x]], 'Data: ', x_test[x], 'Actual: ', y_test[x] , ' ',  names[y_test[x]])
    n = model.kneighbors([x_test[x]], 9, True)
    print('N: ', n)
    
    