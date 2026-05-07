#9th
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
titanic_data = sns.load_dataset('titanic')
titanic_data = titanic_data.dropna(subset=['age'])
plt.figure(figsize=(10, 6))
sns.boxplot(
    data=titanic_data,
    x='sex',
    y='age',
    hue='survived'
)
plt.title('Box Plot of Age Distribution by Gender and Survival Status')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.legend(
    title='Survived',
    labels=['Did Not Survive', 'Survived']
)
plt.grid(True)
plt.show()