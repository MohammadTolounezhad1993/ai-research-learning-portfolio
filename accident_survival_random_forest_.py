# -*- coding: utf-8 -*-
"""Accident Survival-Random Forest .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D68Ab7Tri1ufhDoi1UAX2xWkBjRCfVr5

Accident Survival Prediction using Random Forest

This project implements a step-by-step machine learning pipeline using the Random Forest algorithm to predict accident survival outcomes. The dataset includes demographic and accident-related features such as age, gender, speed of impact, helmet usage, and seatbelt usage.

 Key Steps:
- Data preprocessing (label encoding, missing value handling)
- Train-test split and feature scaling
- Model training using RandomForestClassifier
- Evaluation using accuracy, confusion matrix, and classification report
- Visualization of results and feature importances

This notebook is designed for both learning and professional portfolio purposes. The code is clean, modular, and ready for deployment or further experimentation.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("/content/drive/MyDrive/python for machine learning/accident.csv")
data = df.copy()
label_cols = ['Gender', 'Helmet_Used', 'Seatbelt_Used']
le = LabelEncoder()
for col in label_cols:
    data[col] = le.fit_transform(data[col])
X = data.drop("Survived", axis=1)
y = data["Survived"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Heatmap')
plt.show()

importances = model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(8, 5))
sns.barplot(x=importances, y=feature_names)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title('Feature Importances in Random Forest')
plt.show()

"""The model achieved an accuracy of approximately 52.5% on the test set.  
Feature importance analysis showed that speed of impact and age were the most influential factors in predicting survival.

"""