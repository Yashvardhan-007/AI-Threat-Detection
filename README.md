# AI Threat Detection Project

## Setup
pip install -r requirements.txt

## Run
python data/generate_data.py
uvicorn api.main:app --reload
streamlit run dashboard/app.py
