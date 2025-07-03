import torch
import torch.nn as nn
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder
import joblib

df = pd.read_csv("dataset.csv")
df["symptoms"] = df["symptoms"].apply(lambda x: x.lower().split())

mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df["symptoms"])

le = LabelEncoder()
y = le.fit_transform(df["disease"])

# Save encoders
joblib.dump(mlb, "symptom_encoder.pkl")
joblib.dump(le, "label_encoder.pkl")

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

model = SimpleNet(X.shape[1], len(set(y)))
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

X_tensor = torch.FloatTensor(X)
y_tensor = torch.LongTensor(y)

# Train
for epoch in range(100):
    optimizer.zero_grad()
    out = model(X_tensor)
    loss = loss_fn(out, y_tensor)
    loss.backward()
    optimizer.step()

torch.save(model.state_dict(), "model.pth")
print("✅ Model trained & saved!")
