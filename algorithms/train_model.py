import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "..", "dataset", "bank_churn.csv")
MODEL_PATH = os.path.join(BASE_DIR, "churn_model.pkl")

data = pd.read_csv(DATASET_PATH)

X = data[["age", "balance"]]
y = data["churn"]

model = LogisticRegression()
model.fit(X, y)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("MODEL CREATED SUCCESSFULLY")
