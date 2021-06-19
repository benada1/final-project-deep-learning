# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:53:42 2021

@author: shalva
"""


import numpy as np
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.metrics import accuracy_score 
from training import x_train,y_train,x_valid,y_valid


# finds the optimum 'k' 
from sklearn.model_selection import GridSearchCV
parameters = {'n_neighbors':np.arange(1,30)}
knn = KNeighborsClassifier()


# calculating KNN's accuracy 
model = GridSearchCV(knn, parameters, cv=5)
model.fit(x_train, y_train)
print ( "k= " , model.best_params_)


# uses the calculated 'k' to find accuracy and finds predicted price range
model_knn = KNeighborsClassifier(n_neighbors=9)  
model_knn.fit(x_train, y_train)
y_pred_knn = model_knn.predict(x_valid) 
acc_knn = accuracy_score(y_valid, y_pred_knn)
print ("accuracy = " , acc_knn)