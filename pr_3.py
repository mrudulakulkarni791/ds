3
Descriptive Statistics - Measures of
Central Tendency and variability: Using
the Iris dataset. We will: a) Perform
operations on the Iris dataset to calculate
basic statistical details (percentile, mean,
standard deviation, etc.) for different
species ('Iris-setosa', 'Iris-versicolor', 'Irisvirginica'). b) Use Python to extract and
analyze these statistics for each species
and understand their distributions.
  
#3rd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('iris_dataset.csv')

print("First 5 rows:\n", df.head())
setosa = df[df['Species'] == 'setosa']
versicolor = df[df['Species'] == 'versicolor']
virginica = df[df['Species'] == 'virginica']
print("\nIris-setosa Statistics:\n", setosa.describe())

print("\nIris-versicolor Statistics:\n", versicolor.describe())

print("\nIris-virginica Statistics:\n", virginica.describe())

sns.histplot(setosa['SepalLength'], kde=True)
plt.title('Distribution of Sepal Length (Iris-setosa)')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

