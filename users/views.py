from django.shortcuts import render
import joblib
import os
from django.conf import settings
import numpy as np

# Load trained model once
model_path = os.path.join(settings.BASE_DIR, 'firstproject', 'model.pkl')
model = joblib.load(model_path)

def predict(request):
    prediction_result = None
    churn_value = None

    if request.method == "POST":
        age = float(request.POST.get("age"))
        balance = float(request.POST.get("balance"))

        input_data = np.array([[age, balance]])
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            prediction_result = "Customer is likely to Churn ❌"
            churn_value = 1
        else:
            prediction_result = "Customer is likely to Stay ✅"
            churn_value = 0

    context = {
        "prediction": prediction_result,
        "churn_value": churn_value,
    }

    return render(request, "users/predict.html", context)