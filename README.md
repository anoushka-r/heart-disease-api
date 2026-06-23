# Heart Disease Prediction API

A production-ready machine learning system that predicts heart disease risk from clinical patient data.

## Live Demo
Try it here: [heart-disease-predictor-api.streamlit.app](https://heart-disease-predictor-api.streamlit.app)

## API
REST API endpoint: [heart-disease-api-exzj.onrender.com](https://heart-disease-api-exzj.onrender.com)  
API Docs: [heart-disease-api-exzj.onrender.com/docs](https://heart-disease-api-exzj.onrender.com/docs)

## What It Does
Input 13 clinical features (age, cholesterol, ECG readings, ST slope, etc.) and get a real-time heart disease risk prediction with probability score. No code required via the Streamlit front end.

## Model Performance
- Accuracy: 95.8%
- ROC-AUC: 0.97
- Recall: 0.97
- F1 Score: 0.96
- Test set: 238 samples (100 TN, 128 TP, 7 FP, 3 FN)

## Tech Stack
- **Model:** Logistic Regression (GridSearchCV tuned) via scikit-learn
- **API:** FastAPI
- **Containerisation:** Docker
- **Deployment:** Render
- **Front End:** Streamlit

## Project Structure
- `main.py` — FastAPI application
- `app.py` — Streamlit front end
- `heart_model.pkl` — Trained model
- `requirements.txt` — Dependencies
- `Dockerfile` — Container configuration

## Run Locally
```bash
git clone https://github.com/anoushka-r/heart-disease-api.git
cd heart-disease-api
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `http://localhost:8000/docs` to test the API.

## Author
Anoushka Rakheja  
[LinkedIn](https://linkedin.com/in/anoushka-rakheja) | [GitHub](https://github.com/anoushka-r)
