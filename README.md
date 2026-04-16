# 🏦 Bank Customer Churn Prediction & Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Random Forest](https://img.shields.io/badge/ML%20Model-Random%20Forest-blue?style=for-the-badge)

An end-to-end Machine Learning project that predicts the likelihood of bank customers leaving (churning). This repository features a comprehensive Exploratory Data Analysis (EDA) and a production-ready **Streamlit** web application.

## 🌐 Live Demo
🚀 **Access the interactive app here:** [https://bank-customer-churn-prediction-wirdq5pe6quekseyy2qhzt.streamlit.app/]

---

## 📊 Business Problem
Retaining customers is often cheaper than acquiring new ones. This project provides a tool for banks to identify high-risk customers based on credit scores, geography, gender, age, balance, and activity levels, allowing for proactive retention strategies.

### 🛠 Tech Stack
* **Programming:** Python
* **Data Analysis:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Model Deployment:** Streamlit, Joblib

---

## 🧠 Model Performance
The classification model was trained on the "Churn Modelling" dataset and achieved:
* **Accuracy:** 87%
* **Feature Engineering:** Implemented One-Hot Encoding for categorical variables (`Geography`, `Gender`) and handled feature selection by dropping non-predictive columns (`RowNumber`, `CustomerId`, `Surname`).

---

## 🏗 Project Structure
```text
├── data/
│   └── Churn_Modelling.csv      # Original dataset
├── ChurnPrediction.ipynb        # Data cleaning, EDA, and model training
├── app.py                      # Streamlit web application script
├── bank_churn_model.pkl        # Serialized Random Forest model
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation