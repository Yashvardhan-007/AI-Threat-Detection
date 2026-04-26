import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:8000"

st.title("AI Threat Detection Dashboard")

logs = requests.get(f"{API_URL}/logs").json()
df = pd.DataFrame(logs)

st.dataframe(df)

fig = px.histogram(df, x="activity")
st.plotly_chart(fig)

alerts = requests.get(f"{API_URL}/alerts").json()
st.write("Alerts:", alerts)
