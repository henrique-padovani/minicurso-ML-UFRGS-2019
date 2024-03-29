# -*- coding: utf-8 -*-
"""KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K0JKj9O3yqeukFyYNe3o4hBm29GVdKC5
"""

# K Nearest Neighbors

# You've been given a classified data set from a company!
# They've hidden the feature column names but have given you the data
# and the target classes. 

# We'll try to use KNN to create a model that directly predicts a class
# for a new data point based off of the features.

# Import libraries

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

# Read the dataset

url = 'https://raw.githubusercontent.com/henrique-padovani/minicurso-ML-UFRGS-2019/master/KNN/Classified%20Data'

# Set index_col=0 to use the first column as the index.
df = pd.read_csv(url,index_col=0)

df.head()

sns.pairplot(df, hue='TARGET CLASS')



# Standardize the Variables

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler_fit = scaler.fit(df.drop('TARGET CLASS',axis=1))

scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))

df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1])
df_feat.head()



# Split into train and test

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(scaled_features,df['TARGET CLASS'],
                                                    test_size=0.30)

# Use KNN

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)

knn_fit = knn.fit(X_train,y_train)

pred = knn.predict(X_test)

# Evaluate how good it is

from sklearn.metrics import classification_report,confusion_matrix

print(confusion_matrix(y_test,pred))

print(classification_report(y_test,pred))

# How can we improve this?

error_rate = []

# Will take some time
for i in range(1,40):
    
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

# NOW WITH K=35
knn = KNeighborsClassifier(n_neighbors=23)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=35')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))



















