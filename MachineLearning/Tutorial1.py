#%%
import pandas as pd 
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import matplotlib as mpl
import pickle
from matplotlib import style

data = pd.read_csv('student-mat.csv', sep=';')

data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']] #atributes unique to each student 
#print(data.head())

#creating labels - based on atributes, what you're trying to find 
predict = 'G3' 

X = np.array(data.drop([predict], 1)) #exclude predict (G3) from the array as this is what we're trying to predict
Y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1) #taking some values for training and some for test from X and Y, test_size 10% of the data is taken for testing

# best = 0
# for _ in range(100000):
#     x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1) #taking some values for training and some for test from X and Y, test_size 10% of the data is taken for testing

#     #linear regression model
#     #best fir line

#     linear = linear_model.LinearRegression() #create a model template

#     linear.fit(x_train, y_train) #use model with x_train and y_train to adjust weights according to data values
#     acc = linear.score(x_test, y_test) #rate the accuracy of the model 1 is best 0 is worst
    

#     #save model
#     if acc > best:
#         best = acc
#         with open('studentmodel.pickle', 'wb') as f:
#             pickle.dump(linear, f)
#             print(best)

#import model
pickle_in = open('studentmodel.pickle', 'rb')
#use and test the model

linear = pickle.load(pickle_in)

#print('Co: ', linear.coef_) #prints linear model coefficients
#print('Intercept: ', linear.intercept_)

#predict students grade 

predictions = linear.predict(x_test) #predict new values based on linear.fit(x_train, y_train) results

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

#plot
p = 'G2'
style.use('ggplot')
pyplot.scatter(data[p], data['G3'])
pyplot.xlabel(p)
pyplot.ylabel('Final Grade')
pyplot.show();


# %%

# %%
