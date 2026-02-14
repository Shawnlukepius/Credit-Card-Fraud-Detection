import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details below:")

# Example input fields (simplified)
amount = st.number_input("Transaction Amount", min_value=0.0)
time = st.number_input("Transaction Time", min_value=0.0)

# For demo, we'll create dummy V1-V28 values
features = []
for i in range(1, 29):
    val = st.number_input(f"V{i}", value=0.0)
    features.append(val)

if st.button("Predict"):

    input_data = np.array([[time, amount] + features])
    
    # Scale time & amount
    input_data[:,0:2] = scaler.transform(input_data[:,0:2])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")
