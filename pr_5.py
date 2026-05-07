5
Data Analytics-II 1. Implement logistic
regression using Python/R to perform
classification on Social_Network_Ads.csv
dataset.
2. Compute Confusion matrix to find TP,
FP, TN, FN, Accuracy, Error rate,
Precision, Recall on the given dataset.

#5th
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
dataset = pd.read_csv('Social_Network_Ads.csv')
print("First 5 rows:\n", dataset.head())
print("\nMissing Values:\n", dataset.isnull().sum())
# Features (Age, EstimatedSalary)
X = dataset.iloc[:, 2:-1].values

# Target (Purchased)
y = dataset.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
TN, FP, FN, TP = cm.ravel()
print("\nConfusion Matrix:\n", cm)
print(f"\nTP: {TP}, TN: {TN}, FP: {FP}, FN: {FN}")
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
error_rate = 1 - accuracy
print("\nAccuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("Error Rate:", error_rate)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
