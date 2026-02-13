import os
import numpy as np
import joblib
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Load trained model once
model_path = os.path.join(settings.BASE_DIR, 'model.pkl')
model = joblib.load(model_path)


@login_required
def predict(request):
    prediction_result = None

    if request.method == "POST":
        try:
            age = float(request.POST.get("age"))
            balance = float(request.POST.get("balance"))

            # Prepare input
            input_data = np.array([[age, balance]])

            # Make prediction
            prediction = model.predict(input_data)

            if prediction[0] == 1:
                prediction_result = "Customer is likely to Churn ❌"
            else:
                prediction_result = "Customer is likely to Stay ✅"

        except:
            prediction_result = "Invalid input. Please enter valid numbers."

    return render(request, "users/predict.html", {
        "prediction": prediction_result
    })