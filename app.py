import streamlit as st
import pickle
import numpy as np

# Load model and columns
with open("models/student_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

st.title("🎓 Student Exam Score Predictor")

# Create input widgets for each feature
input_data = []
for col in model_columns:
    val = st.number_input(f"Enter {col}", value=0)
    input_data.append(val)

# Predict button
if st.button("Predict"):
    prediction = model.predict([input_data])
    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")