import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# ---------- Project base directory ----------
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

# ---------- Dataset path ----------
data_path = os.path.join(BASE_DIR, "data", "full_data.csv")

print("Loading data from:", data_path)

# ---------- Load dataset ----------
df = pd.read_csv(data_path)

# ---------- Prepare data ----------
y = df["P_HABITABLE"]

X = df.select_dtypes(include=["number"]).drop(columns=["P_HABITABLE"])
X = X.fillna(0)

# ---------- Train model ----------
model = RandomForestClassifier()
model.fit(X, y)

print("Model trained successfully")

# ---------- Save model ----------
model_dir = os.path.join(BASE_DIR, "Models")
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, "Aniketkumar2004_model.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("Model saved at:", model_path)
