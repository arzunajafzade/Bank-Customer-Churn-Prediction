import streamlit as st
import pandas as pd
import joblib

# Page configuration - Brauzer tabında görünən ad
st.set_page_config(page_title="Bank Churn AI", page_icon="🏦")

# 1. Load the model
model = joblib.load('bank_churn_model.pkl')

# Title and Description
st.title("🏦 Customer Churn Intelligence")
st.markdown("""
    Predict customer retention with **Machine Learning**. 
    Fill in the details below to see the risk analysis.
    ---
""")

# 2. User Inputs organized in a better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Financial Profile")
    credit_score = st.number_input("Credit Score", 300, 850, 600)
    balance = st.number_input("Account Balance ($)", 0.0, 250000.0, 50000.0)
    salary = st.number_input("Estimated Salary ($)", 0.0, 200000.0, 75000.0)
    has_card = st.radio("Has Credit Card?", ["Yes", "No"])

with col2:
    st.subheader("Demographics & Status")
    age = st.slider("Age", 18, 100, 35)
    tenure = st.slider("Tenure (Years)", 0, 10, 5)
    num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
    is_active = st.radio("Is Active Member?", ["Yes", "No"])

st.markdown("---")
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])

# 3. Processing Inputs
if st.button("🔍 Analyze Retention Risk", use_container_width=True):
    data = {
        'CreditScore': credit_score,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_products,
        'HasCrCard': 1 if has_card == "Yes" else 0,
        'IsActiveMember': 1 if is_active == "Yes" else 0,
        'EstimatedSalary': salary,
        'Geography_Germany': 1 if geography == "Germany" else 0,
        'Geography_Spain': 1 if geography == "Spain" else 0,
        'Gender_Male': 1 if gender == "Male" else 0
    }
    
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]
    
    # 4. Result Display
    st.subheader("Analysis Result:")
    if prediction == 1:
        st.error("⚠️ **High Risk:** This customer is likely to churn (leave).")
    else:
        st.success("✅ **Low Risk:** This customer is likely to stay loyal.")