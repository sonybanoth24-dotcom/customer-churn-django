import os
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import joblib


# Load ML model
model_path = os.path.join(settings.BASE_DIR, 'algorithms', 'churn_model.pkl')
model = joblib.load(model_path)


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, "users/register.html", {"error": "Username already exists!"})

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, "users/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('predict')
        else:
            return render(request, "users/login.html", {"error": "Invalid credentials"})

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def predict(request):
    prediction_result = None

    if request.method == "POST":
        age = float(request.POST.get("age"))
        balance = float(request.POST.get("balance"))

        input_data = np.array([[age, balance]])
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            prediction_result = "Customer is likely to Churn ❌"
        else:
            prediction_result = "Customer is likely to Stay ✅"

        ages = [20, 25, 30, 35, 40, 45, 50]
        churn_percent = []

        for a in ages:
            sample_input = np.array([[a, balance]])
            pred = model.predict(sample_input)[0]
            churn_percent.append(100 if pred == 1 else 0)

        plt.figure()
        plt.plot(ages, churn_percent, marker='o')
        plt.title("Predicted Churn vs Age")
        plt.xlabel("Age")
        plt.ylabel("Prediction (0=Stay,100=Churn)")
        plt.grid(True)

        graph_path = os.path.join(settings.BASE_DIR, 'static', 'churn_graph.png')
        plt.savefig(graph_path)
        plt.close()

    context = {
        "prediction": prediction_result,
        "timestamp": int(time.time())
    }

    return render(request, "users/predict.html", context)