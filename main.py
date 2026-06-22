from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the saved model
model = joblib.load("heart_model.pkl")

# These are your exact column names from the notebook
class PatientData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

@app.get("/")
def home():
    return {"message": "Heart Disease Prediction API is running!"}

@app.post("/predict")
def predict(data: PatientData):
    # Convert input to dataframe
    input_df = pd.DataFrame([data.dict()])
    # Get prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    result = "High Risk" if prediction == 1 else "Low Risk"
    return {
        "prediction": result,
        "probability_of_disease": round(float(probability), 2)
    }
