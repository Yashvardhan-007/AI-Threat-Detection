# 🔐 AI-Powered Threat Detection System

🚀 **Building Intelligent, Secure, and Resilient Systems using AI & Cybersecurity Principles**

---

## 🌟 Overview

This project is an **AI-driven threat detection system** that simulates a real-world **Security Operations Center (SOC)**.

It analyzes system activity logs, detects anomalies using machine learning, and visualizes threats through an interactive dashboard.

---

## 🎯 Key Features

* 🔍 **Anomaly Detection (AI/ML)**
  Uses Isolation Forest to detect suspicious behavior in system logs

* 📊 **Interactive Dashboard**
  Built with Streamlit to visualize logs, alerts, and risk scores

* ⚡ **FastAPI Backend**
  High-performance API for real-time threat detection

* 🔐 **Security Architecture**
  Includes authentication concepts, logging, and secure design

* 🚨 **Threat Alerts System**
  Flags abnormal activities with risk scoring

---

## 🧠 Tech Stack

| Layer     | Technology                      |
| --------- | ------------------------------- |
| AI/ML     | Scikit-learn (Isolation Forest) |
| Backend   | FastAPI                         |
| Dashboard | Streamlit, Plotly               |
| Data      | Pandas, NumPy                   |
| Security  | JWT, Bcrypt                     |
| Language  | Python                          |

---

## 🏗️ System Architecture

```
User Activity Logs → Data Processing → ML Model → Threat Detection  
                                     ↓  
                              Risk Scoring  
                                     ↓  
                           API + Dashboard  
```

---

## 📂 Project Structure

```
energy-threat-detection/
│
├── data/              # Data generation & logs  
├── models/            # ML model (Anomaly Detection)  
├── api/               # FastAPI backend  
├── dashboard/         # Streamlit dashboard  
├── utils/             # Authentication & helpers  
├── config/            # Configuration files  
├── requirements.txt  
└── README.md  
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/Yashvardhan-007/AI-Threat-Detection
cd energy-threat-detection
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Generate Sample Data

```
python data/generate_data.py
```

---

## 🚀 Run the Application

### ▶️ Start Backend

```
uvicorn api.main:app --reload
```

### ▶️ Start Dashboard

```
streamlit run dashboard/app.py
```

---

## 📊 Output

* ✅ Real-time system logs
* 🚨 Detected anomalies
* 📈 Activity distribution graphs
* 🔥 Risk score visualization

---

## 💡 Use Cases

* Cybersecurity threat detection
* Network activity monitoring
* Insider threat identification
* AI-based anomaly detection systems

---

## 📸 Demo

> Add screenshots of your dashboard here (important for recruiters)

---

## 🚀 Future Enhancements

* 🔁 Real-time streaming (Kafka)
* 🧠 LSTM-based anomaly detection
* 🔍 Explainable AI (SHAP)
* 🔐 Full authentication system
* ☁️ Cloud deployment (AWS / Docker)

---

## 🎯 Why This Project Matters

This project demonstrates:

* ✅ AI + Cybersecurity integration
* ✅ End-to-end system design
* ✅ Real-world problem solving
* ✅ Backend + ML + Visualization skills

---

## 👨‍💻 Author

**Yashvardhan Singh**
AI & Cybersecurity Engineer (in progress)

---

## ⭐ If you found this useful

Give this repo a ⭐ and connect with me!

<img width="1257" height="634" alt="Screenshot 2026-04-26 121647" src="https://github.com/user-attachments/assets/9f647387-a24d-4f31-9ad7-8aac7b4f898d" />

<img width="939" height="551" alt="Screenshot 2026-04-26 121620" src="https://github.com/user-attachments/assets/f8984e88-3662-40d8-8525-107a60c742e9" />

