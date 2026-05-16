import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("Calories Burned Predictor")

# -----------------------------
# Inputs
# -----------------------------

experience = st.selectbox("Experience Level", [1, 2, 3])

session_duration = st.number_input(
    "Session Duration (hours)",
    min_value=0.0,
    max_value=6.0,
    step=0.1
)

fat_percentage = st.number_input(
    "Fat Percentage",
    min_value=1.0,
    max_value=100.0,
    step=0.5
)

workout_type_encoded = st.selectbox(
    "Workout Type (0=Cardio, 1=Strength, 2=HIIT, 3=Yoga)",
    [0, 1, 2, 3]
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Calories Burned"):

    # ---------------- RULES FIRST ----------------
    if session_duration == 0 or fat_percentage == 0:
        prediction = 0

    else:
        features = np.array([[
             experience,
            session_duration,
            fat_percentage,
            workout_type_encoded
        ]])

        prediction = model.predict(features)[0]

    st.success(f"Estimated Calories Burned: {prediction:.2f}")