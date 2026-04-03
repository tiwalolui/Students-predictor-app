import streamlit as st
import numpy as np
import pickle
import os

# Load the model
model_path = os.path.join("models", "student_model.pkl")
model = pickle.load(open(model_path, "rb"))

# App title
st.title("Students Exam Score Predictor 🎓")

st.markdown(
    """
    Enter the student's study details below, and the model will predict their final exam score (G3).
    """
)

# Input widgets with validation
studytime = st.number_input(
    "Enter study time (hours per week):",
    min_value=0,
    max_value=5,
    step=1
)
G1 = st.number_input(
    "Enter G1 score:",
    min_value=0,
    max_value=20,
    step=1
)
G2 = st.number_input(
    "Enter G2 score:",
    min_value=0,
    max_value=20,
    step=1
)

# Prediction button
if st.button("Predict G3 Score"):
    # Make prediction
    pred = model.predict([[studytime, G1, G2]])[0]

    # Clip prediction to be between 0 and 100
    pred = np.clip(pred, 0, 100)

    # Display result
    st.success(f"Predicted final exam score (G3): {pred:.2f}")