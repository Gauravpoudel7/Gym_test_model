import streamlit as st
import joblib
import numpy as np
import requests
from streamlit_lottie import st_lottie

# 1. Page Configuration
st.set_page_config(
    page_title="BurnAI - Light Purple Edition",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Load Lottie Animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_workout = load_lottieurl("https://lottie.host/706be1ff-bf76-47b2-bf9e-8c6cfa929780/H8gWv32YJm.json")

# 3. Load ML Model Safely
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

try:
    model = load_model()
except Exception as e:
    st.error("⚠️ 'model.pkl' not found. Please ensure your trained model file is in the root folder.")
    st.stop()

# 4. Custom Light Purple CSS Injection
st.markdown("""
    <style>
    /* Main Background (Soft Lavender) */
    .stApp {
        background-color: #F3E8FF !important;
    }
    
    /* General Text Color (Deep Purple/Indigo for readability) */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #4C1D95 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #E9D5FF !important;
        border-right: 1px solid #C084FC;
    }
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span {
        color: #5B21B6 !important;
    }

    /* Style the Sliders and Inputs to match the theme */
    div[data-baseweb="slider"] {
        background-color: #E9D5FF;
        border-radius: 10px;
        padding: 5px;
    }
    
    /* Premium Purple Result Card */
    .prediction-card {
        background: linear-gradient(135deg, #7C3AED 0%, #5B21B6 100%);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(124, 58, 237, 0.25);
        text-align: center;
        margin-top: 25px;
        transition: transform 0.3s ease;
    }
    .prediction-card:hover {
        transform: translateY(-5px);
    }
    .prediction-card .metric-subtitle {
        color: #DDD6FE !important;
        letter-spacing: 2px;
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
    }
    .prediction-card .kcal-number {
        font-size: 64px !important;
        font-weight: 800;
        color: #FFFFFF !important;
        margin: 10px 0;
    }
    .prediction-card .success-note {
        color: #A7F3D0 !important;
        font-weight: bold;
        margin: 0;
    }
    
    /* Button Customization (INCREASED FONT SIZE) */
    div.stButton > button:first-child {
        background-color: #7C3AED !important;
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 15px 30px !important; /* Made the padding larger to give text breathing room */
        font-size: 24px !important;    /* Pumped font up from default to 24px */
        font-weight: 800 !important;    /* Extra bold weight */
        letter-spacing: 1px;            /* Slight spacing for a premium look */
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #6D28D9 !important;
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.5);
        transform: scale(1.02);         /* Subtle interactive pop animation on hover */
    }
    
    /* Divider lines */
    hr {
        border-color: #C084FC !important;
    }
    </style>
""", unsafe_allow_html=True)

# 5. UI Layout - Sidebar
with st.sidebar:
    st.title("🔮 System Insights")
    st.markdown("""
    This engine leverages machine learning to predict active calorie expenditure.
    
    **Theme Config:** 
    * Palette: Lavender & Deep Amethyst
    * Accessibility: High-contrast text mapping
    """)
    st.info("Adjust the parameters on the right to recalculate.")

# 6. UI Layout - Main App Header
row1_col1, row1_col2 = st.columns([2, 1])

with row1_col1:
    st.title("🔮 BurnAI Predictive Engine")
    st.markdown("### *The precision calorie estimation layout, reimagined.*")
    st.caption("Utilizing complex multi-variable regression mapping to calculate structural metabolic load.")

with row1_col2:
    if lottie_workout:
        st_lottie(lottie_workout, height=160, key="workout_anim")

st.write("---")

# 7. Interactive Inputs Grid
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.markdown("### 👤 Anthropometrics & Profile")
    
    experience_label = st.select_slider(
        "Training Maturity (Experience Level)",
        options=["Beginner", "Intermediate", "Advanced"],
        value="Intermediate"
    )
    experience_mapping = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}
    experience = experience_mapping[experience_label]

    fat_percentage = st.slider(
        "Current Body Fat Composition (%)",
        min_value=3.0,
        max_value=50.0,
        value=18.0,
        step=0.5
    )
    
    water_intake = st.slider(
        "Hydration Volumetric Scale (Liters)",
        min_value=0.0,
        max_value=6.0,
        value=1.5,
        step=0.1
    )

with row2_col2:
    st.markdown("### 🏃‍♂️ Biometrics & Session Metrics")
    
    workout_type_label = st.selectbox(
        "Primary Training Modality",
        ["Cardio (Running/Cycling)", "Strength (Hypertrophy/Power)", "HIIT (Interval Training)", "Yoga/Mobility"]
    )
    workout_mapping = {
        "Cardio (Running/Cycling)": 0, 
        "Strength (Hypertrophy/Power)": 1, 
        "HIIT (Interval Training)": 2, 
        "Yoga/Mobility": 3
    }
    workout_type_encoded = workout_mapping[workout_type_label]

    session_duration = st.slider(
        "Temporal Duration (Hours)",
        min_value=0.25,
        max_value=4.0,
        value=1.0,
        step=0.25
    )

    avg_bpm = st.slider(
        "Mean Heart Rate (BPM)",
        min_value=60,
        max_value=210,
        value=135,
        step=1
    )

st.write("---")

# 8. Interactive Live Execution Block
left_spacer, center_btn, right_spacer = st.columns([1, 1, 1])
with center_btn:
    calculate_clicked = st.button("🔮 GENERATE METABOLIC REPORT", use_container_width=True)

if calculate_clicked:
    if session_duration == 0 or fat_percentage == 0:
        prediction = 0.0
    else:
        features = np.array([[
            experience,
            session_duration,
            fat_percentage,
            workout_type_encoded,
            water_intake,
            avg_bpm
        ]])
        
        prediction = model.predict(features)[0]

    # Render Light-Theme Compliant Result Card (Deep Purple Gradient with White Text)
    st.markdown(f"""
        <div class="prediction-card">
            <div class="metric-subtitle">Calculated Total Energy Expenditure</div>
            <div class="kcal-number">{prediction:.0f} kcal</div>
            <p class="success-note">✓ Computation Complete via Core Predictive Engine</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons()