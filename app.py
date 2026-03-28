import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Calories Burnt Prediction", page_icon="🔥", layout="centered")

# Load model safely
try:
    with open("calories_model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Model load error: {e}")
    st.stop()

# Title
st.title("🔥 Calories Burnt Prediction")
st.write("AI-based fitness prediction system")
st.markdown("### 👨‍💻 Developed by R.Rajesh Kumar")

# Sidebar
st.sidebar.title("Developer Info")
st.sidebar.write("Name: Rajesh Kumar")
st.sidebar.write("Department:BSC AI&ML")

# Inputs
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=10.0, max_value=100.0, value=25.0)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=175.0)

with col2:
    weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=70.0)
    duration = st.number_input("Duration (minutes)", min_value=1.0, max_value=300.0, value=30.0)
    heart_rate = st.number_input("Heart Rate", min_value=50.0, max_value=220.0, value=120.0)

gender_val = 0 if gender == "Male" else 1

if st.button("🔥 Predict Calories"):
    try:
        input_data = np.array([[1, gender_val, age, height, weight, duration, heart_rate]], dtype=float)
        result = model.predict(input_data)[0]
        st.success(f"🔥 Estimated Calories Burnt: {result:.2f}")
    except Exception as e:
        st.error(f"Prediction error: {e}")