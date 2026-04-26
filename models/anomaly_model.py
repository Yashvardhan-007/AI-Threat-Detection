import pandas as pd
from sklearn.ensemble import IsolationForest

class AnomalyModel:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05)

    def preprocess(self, df):
        df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
        df["success"] = df["success"].astype(int)
        return df[["hour", "success"]]

    def train(self):
        df = pd.read_csv("data/logs.csv")
        X = self.preprocess(df)
        self.model.fit(X)

    def predict(self, input_data):
        df = pd.DataFrame([input_data])
        X = self.preprocess(df)
        score = self.model.decision_function(X)[0]
        pred = self.model.predict(X)[0]

        return {
            "anomaly_score": float(score),
            "label": "anomaly" if pred == -1 else "normal"
        }

model_instance = AnomalyModel()
model_instance.train()