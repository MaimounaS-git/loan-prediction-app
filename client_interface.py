import streamlit as st
import joblib
import numpy as np
from database.insert_prediction import insert_prediction

def run_client_interface(username="Anonymous"):
    st.header("Loan Eligibility Form")

    # Champs de formulaire (exemple)
    limit_bal = st.number_input("Limit Balance", 0, 1000000, 20000)
    education = st.selectbox("Education", [1, 2, 3, 4])
    age = st.slider("Age", 18, 100, 30)
    bill_amt1 = st.number_input("Last Bill Amount", 0, 1000000, 5000)
    pay_amt1 = st.number_input("Last Payment Amount", 0, 1000000, 2000)

    # Charger modèle et scaler
    model = joblib.load("model/predict_model.pkl")
    scaler = joblib.load("model/scaler.pkl")

    # Prédiction
    if st.button("Predict Loan Eligibility"):
        input_data = np.array([[limit_bal, education, age, bill_amt1, pay_amt1]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]

        result = "✅ Loan Approved" if prediction == 0 else "❌ Loan Rejected"
        st.success(result)

        # Sauvegarde en base
        insert_prediction(
            name=username,
            features={"limit_bal": limit_bal, "education": education, "age": age,
                      "bill_amt1": bill_amt1, "pay_amt1": pay_amt1},
            result=result
        )
