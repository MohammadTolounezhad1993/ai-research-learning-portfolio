#  Accident Survival Prediction using Random Forest

> 📁 *Example data science portfolio project using scikit-learn, pandas, matplotlib*

## Table of Contents

- [📌 Project Overview](#-project-overview)
- [📂 Dataset](#-dataset)
- [🧠 ML Pipeline](#-ml-pipeline)
- [📊 Results](#-results)
- [📁 File Structure](#-file-structure)
- [🚀 Future Improvements](#-future-improvements)
- [✅ Requirements](#-requirements)
- [📌 License](#-license)


## Project Overview

This project builds a predictive model to estimate **accident survival outcomes** using a Random Forest classifier.  
It analyzes data on age, gender, safety behavior (helmet and seatbelt usage), and accident impact speed.

---

## Dataset

- `accident.csv` — a CSV file containing:https:- [`accident.csv`](https://drive.google.com/file/d/1hBHKedDSkdV_HparhKtSUxUOay6AyuQi/view?usp=sharing) – a CSV file containing:

  - `Age`
  - `Gender`
  - `Helmet_Used`
  - `Seatbelt_Used`
  - `Speed_of_Impact`
  - `Survived` (Target: 0 = Not Survived, 1 = Survived)

---

##  ML Pipeline

### ✅ Step 1: Data Preprocessing
- Label Encoding of categorical features
- Feature scaling using `StandardScaler`

### ✅ Step 2: Train-Test Split
- 80% training / 20% testing using `train_test_split`

### ✅ Step 3: Model Training
- `RandomForestClassifier` with:
  - `n_estimators = 100`
  - `random_state = 42`

### ✅ Step 4: Model Evaluation
- `accuracy_score`
- `confusion_matrix`
- `classification_report`

### ✅ Step 5: Visualization
- Heatmap of Confusion Matrix
- Bar chart for Feature Importances

---

##  Results

- **Accuracy:** ~50% on test data
- **Most important features:**
  - `Speed_of_Impact`
  - `Age`

> *The current model is a baseline. With tuning and advanced techniques, performance can be significantly improved.*

