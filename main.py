from fastapi import FastAPI
from pydantic import BaseModel
import joblib

from features import extract_features


app = FastAPI(
    title="Phishing URL Detection API",
    version="1.0"
)

model = joblib.load("model/phishing_model.pkl")


class URLRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {
        "message": "Phishing URL Detection API is running"
    }


@app.post("/predict")
def predict(request: URLRequest):

    features = extract_features(request.url)

    prediction = model.predict([features])[0]
    probabilities = model.predict_proba([features])[0]

    phishing_probability = float(probabilities[0])
    legitimate_probability = float(probabilities[1])

    result = (
        "phishing"
        if prediction == 0
        else "legitimate"
    )

    return {
        "url": request.url,
        "prediction": result,
        "phishing_probability": round(
            phishing_probability * 100,
            2
        ),
        "legitimate_probability": round(
            legitimate_probability * 100,
            2
        )
    }