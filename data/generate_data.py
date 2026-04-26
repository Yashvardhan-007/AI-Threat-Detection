import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os
def generate_logs(n=500):
    data = []
    base_time = datetime.now()

    for i in range(n):
        timestamp = base_time - timedelta(minutes=i*5)
        ip = f"192.168.1.{random.randint(1,255)}"
        activity = random.choice(["login", "file_access", "download"])
        success = random.choice([0,1])

        if random.random() < 0.05:
            success = 0

        data.append([timestamp, ip, activity, success])

    df = pd.DataFrame(data, columns=["timestamp","ip","activity","success"])
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/logs.csv", index=False)
    print("Data generated!")

if __name__ == "__main__":
    generate_logs()
