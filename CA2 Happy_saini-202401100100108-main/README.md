# Titanic Survival Prediction API

FastAPI service that serves predictions from a trained Random Forest model.

## Project files

- `main.py`: FastAPI application with `/` and `/predict` endpoints.
- `train.py`: trains and evaluates the Random Forest model.
- `model.joblib`: saved trained model used by the API.
- `train_and_test2.csv`: Titanic training dataset.
- `Dockerfile`: container image definition.
- `.github/workflows/ci.yaml`: dependency, Docker build, and startup checks.

## Run locally

```bash
pip install -r requirements.txt
python train.py
uvicorn main:app --reload
```

Open `http://localhost:8000/` to verify the service. Send a prediction request with:

```bash
curl -X POST http://localhost:8000/predict \
	-H "Content-Type: application/json" \
	-d '{"Pclass": 3, "Sex": 0, "Age": 22, "sibsp": 1, "Parch": 0, "Fare": 7.25}'
```

`Sex` uses `0` for male and `1` for female.

## Run with Docker

```bash
docker build -t titanic-api .
docker run --rm -p 8000:8000 titanic-api
```