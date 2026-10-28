from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


# Locate and load the trained model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.joblib"

model = joblib.load(MODEL_PATH)


# Create the FastAPI application
app = FastAPI(
    title="Titanic Survival Prediction API",
    description="Predict whether a Titanic passenger survived.",
    version="1.0.0",
)


# Define the input format
class PassengerInput(BaseModel):
    Pclass: int = Field(ge=1, le=3)
    Sex: str
    Age: float | None = Field(default=None, ge=0, le=100)
    SibSp: int = Field(ge=0, le=10)
    Parch: int = Field(ge=0, le=10)
    Fare: float = Field(ge=0)
    Embarked: str | None = None


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Titanic Survival API is running"
    }


# Health-check endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }


# Prediction endpoint

@app.post("/predict")
def predict(passenger: PassengerInput):
    data = passenger.model_dump()

    # Convert text values to the same numeric encoding used during training
    data["Sex"] = data["Sex"].lower()

    if data["Sex"] not in ["male", "female"]:
        raise HTTPException(
            status_code=422,
            detail="Sex must be male or female"
        )

    data["Sex"] = {"male": 0, "female": 1}[data["Sex"]]

    if data["Embarked"] is not None:
        data["Embarked"] = data["Embarked"].upper()

        if data["Embarked"] not in ["S", "C", "Q"]:
            raise HTTPException(
                status_code=422,
                detail="Embarked must be S, C, Q, or null"
            )

        data["Embarked"] = {"S": 0, "C": 1, "Q": 2}[data["Embarked"]]

    input_df = pd.DataFrame([data])

    prediction = int(model.predict(input_df)[0])

    probability = float(model.predict_proba(input_df)[0][1])

    return {
        "survived": prediction,
        "result": "Survived" if prediction == 1 else "Did not survive",
        "survival_probability": round(probability, 4)
    }

    # Convert input into a DataFrame
    input_df = pd.DataFrame([data])

    # Generate the prediction
    prediction = int(model.predict(input_df)[0])

    # Calculate the estimated survival probability
    probability = float(model.predict_proba(input_df)[0][1])

    # Return the result as JSON
    return {
        "survived": prediction,
        "result": (
            "Survived" if prediction == 1
            else "Did not survive"
        ),
        "survival_probability": round(probability, 4)
    }