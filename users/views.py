from django.shortcuts import render
from algorithms.ProcessAlgorithm import predict_churn

def predict_view(request):
    result = None

    if request.method == "POST":
        age = int(request.POST.get("age"))
        balance = float(request.POST.get("balance"))

        result = predict_churn(age, balance)

    return render(request, "users/predict.html", {"result": result})
