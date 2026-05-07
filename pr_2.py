Data Wrangling-II: Create a synthetic
"Academic Performance" dataset for
students, and then perform various data
wrangling operations in Python. The tasks
will involve:
1. Scanning the dataset for missing
values and inconsistencies, and
handling them.
2. Identifying and dealing with outliers
in numeric variables.
3. Applying data transformations on
at least one variable for better
understanding or to improve
distribution

#2nd
import pandas as pd
import numpy as np
data = {
    'Student ID': range(1, 101),
    'Age': np.random.randint(18, 25, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Subject 1': np.random.exponential(scale=30, size=100) + 40,
    'Subject 2': np.random.randint(60, 90, 100),
    'Subject 3': np.random.randint(55, 95, 100),
    'Attendance': np.random.uniform(70, 100, 100),
    'Final Grade': np.random.choice(['A', 'B', 'C'], 100)
}

df = pd.DataFrame(data)
df.loc[5, 'Subject 1'] = np.nan
df.loc[20, 'Subject 2'] = np.nan
df.loc[35, 'Attendance'] = np.nan
print("Missing Values:\n", df.isnull().sum())
df['Subject 1'] = df['Subject 1'].fillna(df['Subject 1'].mean())
df['Subject 2'] = df['Subject 2'].fillna(df['Subject 2'].median())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())
df['Attendance'] = df['Attendance'].clip(0, 100)

df['Final Grade'] = df['Final Grade'].apply(
    lambda x: x if x in ['A', 'B', 'C'] else 'C'
)

# Add an outlier manually
df.loc[10, 'Subject 1'] = 250

# Detect and remove outliers using IQR

Q1 = df['Subject 1'].quantile(0.25)
Q3 = df['Subject 1'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("Shape before removing outliers:", df.shape)

df = df[(df['Subject 1'] >= lower) &
        (df['Subject 1'] <= upper)]

print("Shape after removing outliers:", df.shape)

print("\nMissing Values After Cleaning:\n", df.isnull().sum())
print("\nSkewness before:", df['Subject 1'].skew())
df['Subject 1'] = np.log(df['Subject 1'] + 1)
print("Skewness after:", df['Subject 1'].skew())
print("\nFinal Dataset:\n", df.head())
