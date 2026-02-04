import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "churn_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict_churn(age, balance):
    result = model.predict([[age, balance]])[0]
    return "Low Chance of Churn ✅" if result == 0 else "High Chance of Churn ❌"
