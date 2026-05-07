1
Data Wrangling-I: Importing libraries,
loading a dataset, preprocessing it,
checking for missing values, exploring the
dataset, and performing necessary
transformations and normalizations to
clean the data.
#1st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('titanic.csv')
print("First 5 rows:\n", df.head())
print("\nShape of dataset:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nStatistical Summary:\n", df.describe())
missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values)
# Fill Age with mean
df['Age']=df['Age'].fillna(df['Age'].mean())
# Convert Age to numeric
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Convert Survived to categorical
df['Survived'] = df['Survived'].astype('category')
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
# Convert 'Sex' column to numerical (0 = male, 1 = female)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Convert 'Embarked' column to numerical (using one-hot encoding)
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

print("\nFinal Data Types:\n", df.dtypes)

print("\nFinal Dataset Preview:\n", df.head())


