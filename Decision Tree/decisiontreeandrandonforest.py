# -*- coding: utf-8 -*-
"""DecisionTreeANDRandonForest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pc-VHlc7vDaulL7mAWmQzebMvFuedeeJ

# Random Forest Project

For this project we will be exploring publicly available data from LendingClub.com.

**Lending Club connects people who need money (borrowers) with people who have money (investors). Hopefully, as an investor you would want to invest in people who showed a profile of having a high probability of paying you back. We will try to create a model that will help predict this.**

Lending club had a very interesting year in 2016, so let's check out some of their data and keep the context in mind. This data is from before they even went public.

We will use lending data from 2007-2010 and be trying to classify and predict whether or not the borrower paid back their loan in full. You can download the data from here or just use the csv already provided. It's recommended you use the csv provided as it has been cleaned of NA values.

Here are what the columns represent:

- credit.policy: 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise.
- purpose: The purpose of the loan (takes values "credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", and "all_other").
- int.rate: The interest rate of the loan, as a proportion (a rate of 11% would be stored as 0.11). Borrowers judged by LendingClub.com to be more risky are assigned higher interest rates.
- installment: The monthly installments owed by the borrower if the loan is funded.
- log.annual.inc: The natural log of the self-reported annual income of the borrower.
- dti: The debt-to-income ratio of the borrower (amount of debt divided by annual income).
- fico: The FICO credit score of the borrower.
- days.with.cr.line: The number of days the borrower has had a credit line.
- revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).
- revol.util: The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available).
- inq.last.6mths: The borrower's number of inquiries by creditors in the last 6 months.
- delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in the past 2 years.
- pub.rec: The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments).
"""

# Import Libraries

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# Import data

# loans = pd.read_csv('loan_data.csv')
url = 'https://raw.githubusercontent.com/henrique-padovani/minicurso-ML-UFRGS-2019/master/Decision%20Tree/loan_data.csv'
loans = pd.read_csv(url)

# See some info about the data set

loans.info()

# Let's see some basic statisc information about the data set

loans.describe()

# Let's see some data

loans.head()



# What is FICO?

# FICO (legal name: Fair Isaac Corporation), originally Fair, Isaac and Company,
# is a data analytics company based in San Jose,
# California focused on credit scoring services.

# Let's see if there is a correlation between FICO and 'not.fully.paid'
# How can we do that?

plt.figure(figsize=(10,6))
loans[loans['not.fully.paid']==0]['fico'].hist(alpha=0.5,color='red',
                                              bins=30,label='Credit.Policy=0')
loans[loans['not.fully.paid']==1]['fico'].hist(alpha=0.8,color='blue',
                                              bins=30,label='Credit.Policy=1')


plt.legend()
3plt.xlabel('FICO')

# Improve the dataset

# Remove words columns i.e., create dummy variables

# Check head

loans.head()

categorical_features = ['purpose']

final_data = pd.get_dummies(loans, columns = categorical_features, drop_first=True)

final_data.head()



# Slipt the data

from sklearn.model_selection import train_test_split

X = final_data.drop('not.fully.paid',axis=1)
y = final_data['not.fully.paid']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

# Train the model

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier()

dttree_fit = dtree.fit(X_train,y_train)

# Predict the data

predictions = dtree.predict(X_test)

# Check how good is your model

from sklearn.metrics import classification_report,confusion_matrix

print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))

# Print your tree :D

from sklearn import tree

tree.plot_tree(dttree_fit)

from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus

dot_data = StringIO()
export_graphviz(dttree_fit, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())



# Randon forest

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=600)

rf_fit = rfc.fit(X_train,y_train)

predictions = rfc.predict(X_test)

print(classification_report(y_test,predictions))

print(confusion_matrix(y_test,predictions))

































