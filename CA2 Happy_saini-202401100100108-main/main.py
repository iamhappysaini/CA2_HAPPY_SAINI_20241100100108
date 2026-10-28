from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel
from pathlib import Path

app = FastAPI(
    title="Titanic Survival Prediction API",
    description="CA Assignment FastAPI & Docker Pipeline",
    version="1.0",
)


try:
  model = joblib.load(Path(__file__).with_name("model.joblib"))
except Exception as e:
  model = None


# Input data validation ke liye
class TitanicInput(BaseModel):
  Pclass: int
  Sex: int  # 0 for male, 1 for female
  Age: float
  sibsp: int
  Parch: int
  Fare: float


@app.get("/")
def read_root():
  return {"message": "Titanic ML Prediction API is running successfully!"}


@app.post("/predict")
def predict(data: TitanicInput):
  if model is None:
    raise HTTPException(
        status_code=500, detail="model.joblib not found on server."
    )

  features = [[
      data.Pclass,
      data.Sex,
      data.Age,
      data.sibsp,
      data.Parch,
      data.Fare,
  ]]
  prediction = model.predict(features)
  result = "Survived" if prediction[0] == 1 else "Did Not Survive"

  return {"prediction_code": int(prediction[0]), "survival_status": result}