import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import joblib
import sqlite3
import base64

from app.predict import predict_disease
from app.chatbot import medical_chatbot
from app.auth import signup, login

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Healthcare Assistant",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# BACKGROUND IMAGE FUNCTION
# =====================================================

def set_bg_image(image_url):

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('{image_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# MEDICAL AI BACKGROUND
# =====================================================

set_bg_image(
    "https://images.unsplash.com/photo-1576091160550-2173dba999ef?q=80&w=2070&auto=format&fit=crop"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    /* MAIN APP */

    .stApp {
        color: white;
        font-family: 'Segoe UI';
    }

    /* HERO TITLE */

    .hero-title {
        font-size: 60px;
        font-weight: 800;
        text-align: center;
        color: #8B0000;
        text-shadow: 0px 0px 20px rgba(0,229,255,0.8);
        animation: glow 2s infinite alternate;
        margin-top: 20px;
    }

    @keyframes glow {
        from {
            text-shadow: 0px 0px 10px #00E5FF;
        }
        to {
            text-shadow: 0px 0px 30px #00E5FF;
        }
    }

    /* SUBTITLE */

    .subtitle {
        text-align: center;
        font-size: 22px;
        color: #000000;
        margin-bottom: 40px;
    }

    /* GLASS CARD */

    .glass-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        transition: transform 0.3s ease;
    }

    .glass-card:hover {
        transform: scale(1.02);
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"] {
        background: rgba(5, 10, 25, 0.95);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* BUTTONS */

    .stButton > button {
        background: linear-gradient(90deg,#00E5FF,#00FFA3);
        color: black;
        border-radius: 12px;
        height: 50px;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0px 0px 20px rgba(0,229,255,0.7);
    }

    /* INPUTS */

    .stTextInput > div > div > input {
        background-color: rgba(255,255,255,0.08);
        color: white;
        border-radius: 12px;
    }

    /* METRICS */

    [data-testid="metric-container"] {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 15px;
        padding: 15px;
        border: 1px solid rgba(255,255,255,0.08);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# SESSION STATE
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2785/2785819.png",
    width=100
)

st.sidebar.title("🧬 MedAI Assistant")

st.sidebar.markdown("---")

st.sidebar.info(
    "AI-powered futuristic healthcare platform with disease prediction and intelligent medical chatbot."
)

st.sidebar.markdown("### 🚀 Features")

st.sidebar.markdown(
    """
    - 🤖 AI Medical Chatbot
    - 🩺 Disease Prediction
    - 📊 Health Dashboard
    - 📈 BMI Analytics
    - 🔐 User Authentication
    - 🧬 Smart Health Tracking
    """
)

st.sidebar.markdown("---")

st.sidebar.success("AI Healthcare System Online")

# =====================================================
# HERO SECTION
# =====================================================

st.markdown(
    '<div class="hero-title">🧬 AI HEALTHCARE ASSISTANT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Futuristic AI-Powered Disease Detection & Medical Guidance Platform</div>',
    unsafe_allow_html=True
)

# =====================================================
# LOGIN / SIGNUP SCREEN
# =====================================================

if not st.session_state.logged_in:

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown(
            '<div class="glass-card">',
            unsafe_allow_html=True
        )

        login_tab, signup_tab = st.tabs([
            "🔐 Login",
            "📝 Signup"
        ])

        # LOGIN
        with login_tab:

            st.subheader("Welcome Back")

            username = st.text_input("Username")
            password = st.text_input(
                "Password",
                type="password"
            )

            if st.button("Login to Dashboard"):

                if login(username, password):

                    st.session_state.logged_in = True
                    st.session_state.username = username

                    st.success("Login Successful")
                    st.rerun()

                else:
                    st.error("Invalid Username or Password")

        # SIGNUP
        with signup_tab:

            st.subheader("Create AI Healthcare Account")

            new_user = st.text_input("Create Username")

            new_password = st.text_input(
                "Create Password",
                type="password"
            )

            if st.button("Create Account"):

                if signup(new_user, new_password):
                    st.success("Account Created Successfully")
                else:
                    st.error("Username already exists")

        st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# MAIN DASHBOARD
# =====================================================

else:

    st.sidebar.success(
        f"Logged in as {st.session_state.username}"
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()

    # ---------------- TABS ----------------

    tab1, tab2, tab3, tab4 = st.tabs([
        "🩺 Disease Prediction",
        "💬 AI Chatbot",
        "📊 Health Dashboard",
        "👤 Profile"
    ])

    # =====================================================
    # PREDICTION TAB
    # =====================================================

    with tab1:

        st.markdown(
            '<div class="glass-card">',
            unsafe_allow_html=True
        )

        st.subheader("AI Disease Prediction")

        symptom_columns = joblib.load(
            "models/symptom_columns.pkl"
        )

        selected_symptoms = st.multiselect(
            "Select Symptoms",
            symptom_columns
        )

        if st.button("Predict Disease"):

            if selected_symptoms:

                results = predict_disease(selected_symptoms)

                st.success("Prediction Completed")

                for item in results:

                    disease = item["disease"]
                    probability = item["probability"]

                    st.markdown(
                        f"""
                        <div class="glass-card">
                        <h2>{disease}</h2>
                        <h4>Confidence: {probability}%</h4>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.progress(int(probability))

        st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # CHATBOT TAB
    # =====================================================

    with tab2:

        st.markdown(
            '<div class="glass-card">',
            unsafe_allow_html=True
        )

        st.subheader("🤖 AI Medical Chatbot")

        user_question = st.text_area(
            "Ask any healthcare question"
        )

        if st.button("Ask AI"):

            with st.spinner("AI Thinking..."):

                response = medical_chatbot(user_question)

                st.markdown(
                    f"""
                    <div class="glass-card">
                    {response}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # HEALTH DASHBOARD
    # =====================================================

    with tab3:

        st.subheader("📊 Smart Health Dashboard")

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input("Age", 1, 100)

        with col2:
            height = st.number_input("Height (m)", 1.0, 2.5)

        with col3:
            weight = st.number_input("Weight (kg)", 20.0, 200.0)

        bmi = weight / (height ** 2)

        st.metric("BMI", round(bmi, 2))

        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Healthy"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        st.success(f"Health Status: {status}")

        health_data = pd.DataFrame({
            "Day": [1,2,3,4,5,6,7],
            "Health Score": [55,60,65,70,72,78,85]
        })

        fig = px.area(
            health_data,
            x="Day",
            y="Health Score",
            title="Weekly Health Analytics"
        )

        st.plotly_chart(fig, use_container_width=True)

    # =====================================================
    # PROFILE TAB
    # =====================================================

    with tab4:

        st.markdown(
            f"""
            <div class="glass-card">
            <h2>👤 {st.session_state.username}</h2>
            <p>AI Healthcare Platform User</p>
            <p>Status: Active</p>
            <p>Access Level: Premium AI Diagnostics</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# =====================================================
# DISCLAIMER
# =====================================================

st.warning(
    "This AI healthcare system provides informational guidance only and is not a substitute for professional medical advice."
)
