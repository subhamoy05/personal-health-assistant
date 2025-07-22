# 🧠 AI-Powered Personal Health Assistant

A full-stack intelligent health assistant that predicts potential diseases based on symptoms using a deep learning model. Built with **React**, **Node.js**, **FastAPI**, **PyTorch**, and **MongoDB**.

---

## 🚀 Features

- 🔎 Predict illness from symptoms using a trained PyTorch model
- 📜 View history of predictions (stored in MongoDB)
- 🧬 Multi-class classification model
- 🌐 Clean React UI with form validation
- ⚡ FastAPI-based ML service
- 🧱 Modular architecture with separate services

---

## 🧰 Tech Stack

| Layer       | Tech                             |
|-------------|----------------------------------|
| Frontend    | React, TypeScript, Axios         |
| Backend API | Node.js, Express.js, Mongoose    |
| ML Model    | PyTorch, FastAPI, Python         |
| Database    | MongoDB                          |
| Dataset     | Symptom-Disease dataset (Kaggle) |

---

## 📁 Folder Structure

```bash
├── health-assistant-backend # Node.js Backend API
│ ├── server.js # Express server
│ ├── models/
│ │ └── History.js # MongoDB Schema
│
├── health-assistant-ml # ML Microservice (FastAPI + PyTorch)
│ ├── app.py # FastAPI app
│ ├── train_model.py # PyTorch training script
│ ├── dataset.csv # Dataset used
│ ├── model.pth # Trained model
│ ├── symptom_encoder.pkl # Encoder for symptoms
│ ├── label_encoder.pkl # Encoder for labels
│
├── health-assistant-frontend # React Frontend
│ ├── src/
│ │ ├── components/
│ │ │ └── HealthForm.tsx # Form for symptoms
│ │ ├── App.tsx
│ │ └── index.tsx
│
└── README.md # This file
```

---

## 🛠️ How to Run the Project Locally

Ensure the following are installed:

- 🐍 Python 3.8+
- 🔧 Node.js 18+
- 🍃 MongoDB

---

### 🔹 Step 1: Start ML Microservice

```bash
cd health-assistant-ml
# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Start the API
uvicorn app:app --reload --port 8000
```
🔹 Step 2: Start Node.js Backend 
```bash
cd health-assistant-backend
npm install
node server.js
```
Express server runs at: http://localhost:5000

🔹 Step 3: Start React Frontend
```bash
cd health-assistant-frontend
npm install
npm start
```
Frontend runs at: http://localhost:3000


## 🙋‍♂️ Author

**Subhamoy Saha**  
[GitHub Profile](https://github.com/subhamoy05)
