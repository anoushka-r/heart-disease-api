import streamlit as st
import requests

st.title("Heart Disease Risk Predictor")
st.write("Fill in the patient details below to predict heart disease risk.")

age = st.slider("Age", 1, 100, 52)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3], format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"][x])
trestbps = st.slider("Resting Blood Pressure", 80, 200, 125)
chol = st.slider("Cholesterol", 100, 600, 212)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
restecg = st.selectbox("Resting ECG", options=[0, 1, 2], format_func=lambda x: ["Normal", "ST-T Abnormality", "Left Ventricular Hypertrophy"][x])
thalach = st.slider("Max Heart Rate", 60, 220, 168)
exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of ST Segment", options=[0, 1, 2], format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x])
ca = st.selectbox("Number of Major Vessels", options=[0, 1, 2, 3])
thal = st.selectbox("Thalium Stress Result", options=[1, 2, 3], format_func=lambda x: {1: "Normal", 2: "Fixed Defect", 3: "Reversable Defect"}[x])

if st.button("Predict"):
    data = {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps,
        "chol": chol, "fbs": fbs, "restecg": restecg, "thalach": thalach,
        "exang": exang, "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
    }
    
    response = requests.post("https://heart-disease-api.onrender.com/predict", json=data)
    result = response.json()
    
    if result["prediction"] == "High Risk":
        st.error(f"High Risk of Heart Disease (Probability: {result['probability_of_disease']})")
    else:
        st.success(f"Low Risk of Heart Disease (Probability: {result['probability_of_disease']})")