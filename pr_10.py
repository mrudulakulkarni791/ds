# 1. Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Load Dataset
iris_data = pd.read_csv('iris_dataset.csv')

# 3. Explore Dataset
print("First 5 rows:\n", iris_data.head())
print("\nDataset Info:")
print(iris_data.info())
print("\nData Types:\n", iris_data.dtypes)
print("\nStatistical Summary:\n", iris_data.describe())

# 4. Histograms (All Features)
iris_data.hist(bins=10, figsize=(10, 8))
plt.suptitle('Histograms of Iris Dataset Features')
plt.tight_layout()
plt.show()

# 5. Box Plot (All Features)
plt.figure(figsize=(10, 8))
sns.boxplot(data=iris_data.drop('Species', axis=1))
plt.title('Box Plot of Features in Iris Dataset')
plt.show()

# 6. Histograms by Species
plt.figure(figsize=(12, 8))
for i, feature in enumerate(iris_data.columns[:-1]):
    plt.subplot(2, 2, i + 1)
    sns.histplot(data=iris_data, x=feature, hue="Species", kde=True)
    plt.title(f'Distribution of {feature}')
plt.tight_layout()
plt.show()

# 7. Boxplots by Species
plt.figure(figsize=(12, 8))
for i, feature in enumerate(iris_data.columns[:-1]):
    plt.subplot(2, 2, i + 1)
    sns.boxplot(x='Species', y=feature, data=iris_data)
    plt.title(f'Box Plot of {feature} by Species')
plt.tight_layout()
plt.show()