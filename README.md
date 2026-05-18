
---

## 📌 Project Overview

This project predicts calories burned based on:

- Experience Level
- Session Duration
- Fat Percentage
- Workout Type
- Water Intake
- Average BPM (Heart Rate)

The final model uses an **ensemble learning approach** to achieve high accuracy and reduce overfitting.

---

## 🧠 Machine Learning Approach

### Models Used:
- 🌲 Random Forest Regressor
- ⚡ XGBoost Regressor
- 🔗 Stacking Regressor (Meta-model: Linear Regression)
- 📊 Cross Validation (CV = 5)

### Final Architecture:
Random Forest ─┐
├──→ Stacking Regressor → Final Prediction
XGBoost


---

## 📊 Performance Metrics

| Metric | Value |
|--------|------|
| Train R² Score | 0.981 |
| Test R² Score | 0.955 |
| Mean Absolute Error (MAE) | ~51.7 |

✔ Indicates strong predictive performance with minimal overfitting.

---

## 📂 Dataset Features

| Feature | Description |
|--------|-------------|
| Experience_Level | User fitness level (1–3) |
| Session_Duration (hours) | Workout duration |
| Fat_Percentage | Body fat percentage |
| Workout_Type | Type of workout (Encoded: Cardio, Strength, HIIT, Yoga) |
| Water_Intake (liters) | Water consumed during workout |
| Avg_BPM | Average heart rate during workout |
| Calories_Burned | Target variable |

---

## ⚙️ Tech Stack

- Python 🐍
- Scikit-learn
- XGBoost
- Pandas, NumPy
- Streamlit (for UI)
- Joblib (model saving)

---

## 📈 Workflow

1. Data Cleaning & Preprocessing
2. Feature Selection
3. Train-Test Split
4. Model Training:
   - Random Forest
   - XGBoost
5. Stacking Ensemble with CV
6. Evaluation using R² & MAE
7. Deployment using Streamlit

---

## 🖥️ Streamlit App Features

- User-friendly UI
- Input sliders for real-time prediction
- Instant calorie estimation
- Interactive form-based input system

---

## 📌 How to Run Locally

Clone repository

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py


Future Improvements
Add real-time wearable device integration
Hyperparameter tuning using Optuna
Deploy using cloud (AWS / Render / HuggingFace)
Add BMI and intensity score features
Improve MAE further using feature engineering



Gaurav Poudel

Machine Learning & AI Enthusiast
Focus: Predictive Modeling, Deep Learning, and AI Applications
