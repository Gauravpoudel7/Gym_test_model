<<<<<<< HEAD

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
=======

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
>>>>>>> 4f9bf52a66ceab1642078fd17f71493ea68d1796

⚖️ Previous Approach — Stacking Ensemble
The initial model stacked two base learners (RF + XGB) with a Linear Regression meta-model using 5-fold cross-validation inside the stacker.
Problems with that approach for this dataset:

Redundant complexity — RF and XGB are both decision-tree ensembles. They learn similar patterns, so stacking them yields diminishing returns.
Slow training — Stacking trains each base model cv times internally, then again on the full set. For a small tabular dataset this is unnecessary overhead.
Leaky evaluation — Train R² on a stacking model is inflated by design, making it harder to interpret overfitting.
Hard to tune — Two separate hyperparameter spaces (RF + XGB) are difficult to optimize coherently.


✅ Current Approach — LightGBM + Optuna
What is LightGBM?
LightGBM is a gradient boosting framework by Microsoft that uses leaf-wise tree growth instead of level-wise, making it faster and more accurate on structured/tabular data.
What is Optuna?
Optuna is an automatic hyperparameter optimization framework using Bayesian optimization (TPE sampler) — far more efficient than grid search or random search.

🔍 Why This Works Better Here
1. Purpose-Built for Tabular Data
Low-dimensional structured features like Session_Duration, Avg_BPM, and Fat_Percentage are exactly the regime where gradient boosting dominates. No need for model ensembling.
2. Faster Training
LightGBM is 5–10× faster than XGBoost and trains in a single pass rather than the multiple rounds required by stacking.
3. Smarter Hyperparameter Tuning
Optuna runs 50 Bayesian trials to find the optimal combination of:
ParameterRolenum_leavesControls model complexitylearning_rateStep size per boosting roundmin_child_samplesPrevents overfitting on small splitssubsample + colsample_bytreeRow/column sampling for regularizationreg_alpha + reg_lambdaL1/L2 regularization
4. Early Stopping
Training halts automatically when validation RMSE stops improving (patience = 50 rounds), eliminating manual guesswork on n_estimators.
5. Interpretable Feature Importance
Gain-based feature importance reveals which features drive predictions, not just which ones are used most often — useful for understanding the biology behind calorie burn.

📊 Performance Comparison
MetricStacking (RF + XGB + LR)LightGBM + OptunaTrain R²Inflated (data leakage)ReliableTest R²ModerateHigherTraining TimeSlow (3× CV passes)Fast (single model)Tuning EffortManual, two separate spacesAutomated, unifiedOverfitting RiskHigher (meta-model layer)Controlled via early stopping

🛠️ Dependencies
bashpip install lightgbm optuna scikit-learn