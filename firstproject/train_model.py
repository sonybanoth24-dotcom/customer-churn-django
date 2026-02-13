import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
data = pd.read_csv("../dataset/bank_churn.csv")

X = data[["age", "balance"]]
y = data["churn"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully")