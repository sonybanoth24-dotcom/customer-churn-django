from django.shortcuts import render
import random

def predict_view(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        balance = float(request.POST.get('balance'))

        # Simple logic (you can replace with ML model later)
        if balance > 50000:
            stay_prob = 0.85
            churn_prob = 0.15
            prediction = "Customer is likely to Stay ✅"
        else:
            stay_prob = 0.35
            churn_prob = 0.65
            prediction = "Customer is likely to Churn ❌"

        return render(request, 'users/predict.html', {
            'prediction': prediction,
            'stay_prob': stay_prob,
            'churn_prob': churn_prob
        })

    return render(request, 'users/predict.html')