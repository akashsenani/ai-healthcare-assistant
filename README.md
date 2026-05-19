# 🏥 AI Healthcare Assistant 🤖

An advanced AI-powered Healthcare Assistant built using **Django**, **Machine Learning**, and **Google Gemini AI**.  
The platform provides intelligent disease prediction, AI medical chatbot assistance, voice healthcare interaction, health analytics dashboard, and user health tracking — all inside a futuristic dark-themed medical interface.

---

# 🚀 Live Demo

🔗 https://ai-healthcare-assistant-ur74.onrender.com

---

# ✨ Features

## 🔐 Authentication System
- User Signup/Login
- Secure Password Authentication
- Personalized User Dashboard

---

## 🩺 Disease Prediction System
- Predicts possible diseases based on symptoms
- Uses Machine Learning models:
  - XGBoost
  - Random Forest
  - Scikit-Learn
- Displays:
  - Most probable disease
  - Confidence scores
  - Prediction probabilities

---

## 🤖 AI Medical Chatbot
- Powered by **Google Gemini 2.5 Flash**
- Provides:
  - Medical guidance
  - Health suggestions
  - Diet recommendations
  - Symptom explanations
- Structured point-wise AI responses

---

## 🎙️ Voice AI Assistant
- Browser microphone integration
- Voice-to-text healthcare queries
- Conversational AI medical responses
- Text-to-speech AI interaction

---

## 📊 Health Analytics Dashboard
- BMI Monitoring
- Health Tracking
- Dynamic BMI Graphs
- User Health Statistics
- Disease Prediction History

---

## 🌙 Modern Futuristic UI
- Dark Medical Theme
- Animated UI Components
- Responsive Design
- Neon Glow Effects
- Glassmorphism Cards
- Smooth Transitions

---

# 🛠️ Tech Stack

## Backend
- Django
- SQLite
- Gunicorn
- Whitenoise

## Machine Learning
- Scikit-Learn
- XGBoost
- Pandas
- NumPy
- Joblib

## AI Integration
- Google Gemini API
- Google GenAI SDK

## Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Chart.js

## Deployment
- Render
- GitHub

---

# 📂 Project Structure

```bash
AI_Healthcare_Assistant/
│
├── chatbot/
├── prediction/
├── users/
├── templates/
├── static/
├── model/
├── healthcare_ai/
│
├── manage.py
├── requirements.txt
├── runtime.txt
├── build.sh
└── render.yaml
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/akashsenani/ai-healthcare-assistant.git

cd ai-healthcare-assistant
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows
```bash
venv\Scripts\activate
```

#### Linux/Mac
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Setup Environment Variables

Create `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 5️⃣ Run Migrations

```bash
python manage.py migrate
```

---

## 6️⃣ Start Server

```bash
python manage.py runserver
```

---

# 🌍 Deployment

This project is deployed on:

- Render
- GitHub

---

# 📈 Future Improvements

- Doctor Recommendation System
- Nearby Hospitals Integration
- Medical PDF Report Generator
- Email Health Alerts
- NLP Symptom Understanding
- AI Follow-up Question System
- PostgreSQL Database
- Mobile App Version
- ECG/Image-based Diagnosis AI

---

# 🧠 Machine Learning Workflow

- Dataset Preprocessing
- Symptom Encoding
- Model Training
- Probability Prediction
- Health Analytics Generation

---

# 🔒 Security Features

- Environment Variable Protection
- API Key Security
- User Authentication
- Session Management

---

# 👨‍💻 Author

## Akash Senani

Electronics and Computer Engineering Student  
Vellore Institute of Technology

### GitHub
https://github.com/akashsenani

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub!
