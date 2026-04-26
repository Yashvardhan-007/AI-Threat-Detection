from fastapi import FastAPI
import pandas as pd
from models.anomaly_model import model_instance

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Threat Detection API Running"}

@app.get("/logs")
def get_logs():
    df = pd.read_csv("data/logs.csv")
    return df.tail(50).to_dict(orient="records")

@app.post("/predict")
def predict(data: dict):
    result = model_instance.predict(data)
    return result

@app.get("/alerts")
def get_alerts():
    df = pd.read_csv("data/logs.csv")
    alerts = []
    for _, row in df.iterrows():
        pred = model_instance.predict(row.to_dict())
        if pred["label"] == "anomaly":
            alerts.append(row.to_dict())
    return alerts
