# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from KNN import model_knn



# importing test's data 
test_data = pd.read_csv("C:/Users/shalva/Desktop/ben/test.csv")


# deleting the id columns
test_data=test_data.drop('id',axis=1)


# defining price range predicted ny KNN
predicted_price_range = model_knn.predict(test_data)


# adds the predicted price range into the price_range columns
test_data['price_range'] = predicted_price_range


# exports the price range the computer calculated into a new excel file including all the data
df = pd.DataFrame (test_data) 
df.to_excel ("C:/Users/shalva/Desktop/ben/export_datasave.xlsx" )

# done
print ("predicted_price_range is now available in a new excel file named; export_datasave ")



