import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('bank_churn_model.pkl')

st.title("🏦 Bank Customer Churn Predictor")
st.markdown("---")

# User Input Layout
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", 300, 850, 600)
    age = st.slider("Age", 18, 100, 35)
    tenure = st.slider("Tenure (Years)", 0, 10, 5)
    balance = st.number_input("Account Balance", 0.0, 250000.0, 50000.0)

with col2:
    num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
    has_card = st.selectbox("Has Credit Card?", [1, 0])
    is_active = st.selectbox("Is Active Member?", [1, 0])
    salary = st.number_input("Estimated Salary", 0.0, 200000.0, 75000.0)

geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])

if st.button("Predict Churn Risk"):
    # Match the column names exactly from your Notebook's X_train
    data = {
        'CreditScore': credit_score,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_products,
        'HasCrCard': has_card,
        'IsActiveMember': is_active,
        'EstimatedSalary': salary,
        'Geography_Germany': 1 if geography == "Germany" else 0,
        'Geography_Spain': 1 if geography == "Spain" else 0,
        'Gender_Male': 1 if gender == "Male" else 0
    }
    
    input_df = pd.DataFrame([data])
    
    # Prediction
    prediction = model.predict(input_df)[0]
    # Pro touch: show probability
    probability = model.predict_proba(input_df)[0][1]
    
    if prediction == 1:
        st.error(f"High Risk: Customer is likely to Exit ({probability:.1%} probability)")
    else:
        st.success(f"Low Risk: Customer is likely to Stay ({1-probability:.1%} probability)")