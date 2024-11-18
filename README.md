House Price Prediction Using Linear Regression
This project implements a Linear Regression model to predict house prices based on key features such as square footage, number of bedrooms, and bathrooms. It includes data cleaning, exploratory data analysis (EDA), and predictive modeling using Python and popular machine learning libraries.

Features of the Project
Data Preprocessing:

Handles missing values by replacing them with the column mean (for numerical data) or mode (for categorical data).
Displays statistical summaries and identifies correlations using heatmaps.

Exploratory Data Analysis (EDA):

Visualizes the distribution of house prices.
Uses a heatmap to examine correlations between features and the target variable (SalePrice).
Model Implementation:

Splits the dataset into training and testing sets.
Trains a Linear Regression model using scikit-learn.
Evaluates the model with metrics like Mean Squared Error (MSE) and R-squared (R²).
Custom Predictions:

Allows users to input custom house features (e.g., square footage, bedrooms, bathrooms) and get an estimated price.

Predictions on Test Data:

Generates predictions for a test dataset and saves the results in a submission.csv file.

Visualization:

Includes scatter plots to compare actual vs. predicted prices.
Provides pair plots for deeper insights into feature relationships.

Dataset
The project uses data from Kaggle's House Prices: Advanced Regression Techniques competition:

train.csv: Training dataset for model building.
test.csv: Test dataset for generating predictions.
