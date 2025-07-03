from fastapi import FastAPI
from pydantic import BaseModel
import torch
import torch.nn as nn
import joblib

app = FastAPI()

mlb = joblib.load("symptom_encoder.pkl")
le = joblib.load("label_encoder.pkl")

class SimpleNet(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, output_size)
        )
    def forward(self, x):
        return self.fc(x)

model = SimpleNet(len(mlb.classes_), len(le.classes_))
model.load_state_dict(torch.load("model.pth"))
model.eval()

class SymptomRequest(BaseModel):
    symptoms: list[str]

@app.post("/predict")
def predict(req: SymptomRequest):
    x = mlb.transform([req.symptoms])
    input_tensor = torch.FloatTensor(x)
    with torch.no_grad():
        outputs = model(input_tensor)
        _, predicted = torch.max(outputs, 1)
        disease = le.inverse_transform(predicted.numpy())[0]
    return {"predicted_disease": disease}
