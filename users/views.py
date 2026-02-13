from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("predict")
        else:
            return render(request, "users/login.html", {"error": "Invalid credentials"})

    return render(request, "users/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "users/register.html", {"error": "Username already exists"})

        User.objects.create_user(username=username, password=password)
        return redirect("login")

    return render(request, "users/register.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def predict(request):
    prediction_result = None

    if request.method == "POST":
        age = request.POST.get("age")
        balance = request.POST.get("balance")

        if age and balance:
            age = float(age)
            balance = float(balance)

            if age > 40 and balance < 5000:
                prediction_result = "Customer is likely to Churn ❌"
            else:
                prediction_result = "Customer is likely to Stay ✅"

    return render(request, "users/predict.html", {
        "prediction": prediction_result
    })