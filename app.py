import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =========================
# Load Model
# =========================
@st.cache_resource
def load_model():
    model = joblib.load('model_rf.pkl')   # Path ke model Random Forest
    return model

model = load_model()

# =========================
# Glass Type Labels
# =========================
glass_labels = {
    1: "Building Windows (Float Processed)",
    2: "Building Windows (Non Float Processed)",
    3: "Vehicle Windows (Float Processed)",
    4: "Vehicle Windows (Non Float Processed) - none in dataset",
    5: "Containers",
    6: "Tableware",
    7: "Headlamps"
}

# =========================
# Streamlit UI
# =========================
st.title("🔮 Glass Type Prediction App")
st.write("Masukkan nilai fitur kimia kaca untuk memprediksi **Type of Glass (1–7)**")

# Sidebar Inputs
st.sidebar.header("Input Features")
def user_input_features():
    RI = st.sidebar.number_input('RI (Refractive Index)', 1.50, 1.55, 1.517)
    Na = st.sidebar.number_input('Na (Sodium)', 10.0, 17.0, 13.0)
    Mg = st.sidebar.number_input('Mg (Magnesium)', 0.0, 5.0, 2.0)
    Al = st.sidebar.number_input('Al (Aluminium)', 0.0, 4.0, 1.0)
    Si = st.sidebar.number_input('Si (Silicon)', 70.0, 75.0, 72.0)
    K  = st.sidebar.number_input('K (Potassium)', 0.0, 1.5, 0.5)
    Ca = st.sidebar.number_input('Ca (Calcium)', 5.0, 15.0, 8.0)
    Ba = st.sidebar.number_input('Ba (Barium)', 0.0, 3.5, 0.0)
    Fe = st.sidebar.number_input('Fe (Iron)', 0.0, 1.0, 0.0)

    features = {
        'RI': RI,
        'Na': Na,
        'Mg': Mg,
        'Al': Al,
        'Si': Si,
        'K': K,
        'Ca': Ca,
        'Ba': Ba,
        'Fe': Fe
    }
    return pd.DataFrame([features])

input_df = user_input_features()

# Prediction
if st.button('🔍 Predict Type of Glass'):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    glass_type = prediction[0]
    glass_name = glass_labels.get(glass_type, "Unknown")

    st.subheader('📌 Predicted Glass Type:')
    st.success(f"Type {glass_type}: {glass_name}")


# =========================
# About
# =========================
st.markdown("""
---
**Type of Glass Labels:**
1 = Building Windows (Float Processed)  
2 = Building Windows (Non Float Processed)  
3 = Vehicle Windows (Float Processed)  
4 = Vehicle Windows (Non Float Processed) – none in dataset  
5 = Containers  
6 = Tableware  
7 = Headlamps
""")
