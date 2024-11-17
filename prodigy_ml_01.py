# -*- coding: utf-8 -*-
"""Prodigy_ML_01.ipynb
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

#reading files
train_ = pd.read_csv('train.csv')
test_ = pd.read_csv('test.csv')

print(train_.shape)
print(test_.shape)

train_.head(10)

from IPython.display import display #to show all columns

# Set pandas display options globally
pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)

display(train_)
display(test_)

print(train_.dtypes)
print("_________________________")
print(test_.dtypes)

#Summary
train_.describe()

test_.describe()

#show the number of empty values
train_.isna().sum()

test_.isna().sum()

for column in train_.columns:
    if train_[column].dtype == 'object':
        # Replace Nan  with the mode for categorical columns
        train_[column] = train_[column].fillna(train_[column].mode()[0])  # We don't use inplace=True here
        if column in test_.columns:
            test_[column] = test_[column].fillna(test_[column].mode()[0])
    else:
        # Replace Nan with the mean for numeric columns
        train_[column] = train_[column].fillna(train_[column].mean())
        if column in test_.columns:
            test_[column] = test_[column].fillna(test_[column].mean())

train_.head(10)

# Sale price distribution
plt.figure(figsize=(8, 5))
sns.histplot(train_['SalePrice'], color="skyblue" , kde=True) #Kernel Density Estimate (kde=True) adds a smooth curve to the histogram, representing the estimated probability density function of the data.
plt.title('Sale Price Distribution')
plt.show()

#Correlation verification
correlation_matrix = train_.corr(numeric_only=True)
plt.figure(figsize=(18,10))
sns.heatmap(correlation_matrix, annot=True, cmap='gist_heat', fmt=".1f")

"""After EDA now we can Select only features we need for **prediction**"""

col = ['GrLivArea', 'BedroomAbvGr', 'FullBath']
X = train_[col]
y = train_['SalePrice']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""**Train the Linear Regression Model**"""

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Display model coefficients
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)

plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel('Actual Sale Price')
plt.ylabel('Predicted Sale Price')
plt.title('Actual vs Predicted Sale Price')
plt.plot([y.min(), y.max()], [y.min(), y.max()], '#D20103', linestyle='-.', linewidth=3)
plt.show()

plt.figure(figsize=(12, 8))
sns.pairplot(train_[col + ['SalePrice']], hue='SalePrice', palette='coolwarm')
plt.show()

"""Example of a prediction"""

ex = pd.DataFrame({
    'GrLivArea': [1800],
    'BedroomAbvGr': [2],
    'FullBath': [2],
})
test_prediction = model.predict(ex)
print(f'Example Prediction: ${test_prediction[0]:,.2f}')

# Prepare the test data and make predictions
X_test = test_[col]
test_predictions = model.predict(X_test)

# Save predictions
submission = pd.DataFrame({'Id': test_['Id'], 'SalePrice': test_predictions})
submission.to_csv('submission.csv', index=False)