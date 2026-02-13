from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("predict")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "users/login.html")


# ---------------- REGISTER ----------------
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "users/register.html")


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect("login")


# ---------------- PREDICT ----------------
@login_required
def predict_view(request):
    prediction = None

    if request.method == "POST":
        age = int(request.POST.get("age"))
        balance = float(request.POST.get("balance"))

        # Simple logic (no heavy ML, no graph memory issue)
        if age > 40 and balance < 50000:
            prediction = "Customer is likely to Leave ❌"
        else:
            prediction = "Customer is likely to Stay ✅"

    return render(request, "users/predict.html", {"prediction": prediction})