8
Data Visualization I: 1. Use the inbuilt
dataset 'titanic'. The dataset contains 891
rows and contains information about
the passengers who boarded the
unfortunate Titanic ship. Use the Seaborn
library to see if we can find any patterns in
the data.
2. Write a code to check how the price of
the ticket (column name: 'fare') for each
passenger is distributed by plotting a
histogram.

#8th
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
titanic_data = sns.load_dataset('titanic')
print("\nFirst 5 Rows:\n", titanic_data.head())
print("\nDataset Info:\n")
print(titanic_data.info())
print("\nStatistical Summary:\n", titanic_data.describe())
titanic_data = titanic_data.dropna(subset=['fare'])
plt.figure(figsize=(10, 6))
sns.histplot(titanic_data['fare'], kde=True, bins=30)
#customize plot
plt.title('Distribution of Ticket Prices (Fare) for Titanic Passengers')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.grid(True)

plt.show()
