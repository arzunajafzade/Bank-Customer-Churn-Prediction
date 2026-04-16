import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(page_title="Bank Churn AI", page_icon="🏦")

# 1. Load the model
# Ensure this file was dumped AFTER training in your notebook
model = joblib.load('bank_churn_model.pkl')

# Title
st.title("🏦 Customer Churn Intelligence")
st.markdown("---")

# 2. User Inputs
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", 300, 850, 600)
    age = st.slider("Age", 18, 100, 35)
    tenure = st.slider("Tenure (Years)", 0, 10, 5)
    balance = st.number_input("Balance ($)", 0.0, 250000.0, 50000.0)
    num_products = st.selectbox("Number of Products", [1, 2, 3, 4])

with col2:
    has_card = st.selectbox("Has Credit Card?", [1, 0])
    is_active = st.selectbox("Is Active Member?", [1, 0])
    salary = st.number_input("Estimated Salary ($)", 0.0, 200000.0, 50000.0)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])

# 3. CRITICAL: Match the exact column order from your Notebook
if st.button("Analyze Risk", use_container_width=True):
    # This order must match X_train.columns exactly!
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
    
    # 4. Prediction
    prediction = model.predict(input_df)[0]
    # Get probability to see how "sure" the model is
    probability = model.predict_proba(input_df)[0][1] 
    
    st.markdown("---")
    if prediction == 1:
        st.error(f"⚠️ **High Risk:** The model predicts this customer is likely to EXIT (Risk Score: {probability:.2%})")
    else:
        st.success(f"✅ **Low Risk:** The model predicts this customer is likely to STAY (Exit Probability: {probability:.2%})")