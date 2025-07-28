#  Accident Survival Prediction using Random Forest

This project applies a classical machine learning approach using the **Random Forest** algorithm to predict accident survival outcomes. The analysis is based on demographic and accident-specific attributes, and aims to demonstrate both practical ML skills and portfolio readiness.

---

##  Overview

This notebook walks through a complete machine learning pipeline including:

  **Data Preprocessing**  
   Label Encoding for categorical features  
   Feature Scaling using `StandardScaler`  
   Handling missing values (if any)

 **Model Building**  
   Train-Test Split  
   Training using `RandomForestClassifier`  
   Hyperparameters can be tuned for future improvement

 **Evaluation Metrics**  
  - Accuracy Score  
  - Confusion Matrix  
  - Classification Report

 **Visualization**  
  - Heatmap of Confusion Matrix  
  - Feature Importances using Bar Plot

---

##  Features Used

| Feature           | Description                         |
|------------------|-------------------------------------|
| Age            | Age of the individual               |
| Gender         | Coded using LabelEncoder            |
| Speed_of_Impact| Collision intensity (numeric)       |
| Helmet_Used    | Helmet usage (Yes/No - encoded)     |
| Seatbelt_Used  | Seatbelt usage (Yes/No - encoded)   |

---

##  Results

 **Accuracy:** ~52.5% on the test set  
 **Top Predictive Features:**  
  Speed_of_Impact  
   Age

Despite being a basic implementation, this model demonstrates how feature importance can be leveraged in accident analysis scenarios.

---

##  Dataset

The dataset is a realistic, synthetic dataset simulating survival outcomes based on behavioral and contextual factors in accidents. (Stored locally for this demo.)

---

##  Tech Stack

 Programming: **Python**
 Libraries:  
  pandas, numpy  
 scikit-learn  
 matplotlib, seaborn

---

##  Learning Objective

This project is part of my AI learning roadmap and is designed to:
 Reinforce foundational ML skills
 Build a structured and clean codebase for classical ML models
 Prepare for deployment, tuning, and portfolio demonstration

> 📁 Part of my **AI Research Portfolio** aimed at developing research-level proficiency in machine learning.

---

##  Future Enhancements

 Hyperparameter tuning using GridSearchCV  
 Comparison with other models like XGBoost or SVM  
 Deployment via Streamlit for public demonstration

---

## Contribution

Contributions, suggestions, or forks are welcome! Feel free to open an issue or submit a pull request if you'd like to improve the model or add new analysis.


