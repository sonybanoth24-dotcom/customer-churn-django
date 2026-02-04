from django.shortcuts import render

def predict_churn(request):
    result = None

    if request.method == "POST":
        age = int(request.POST.get("age"))
        balance = float(request.POST.get("balance"))
        credit_score = int(request.POST.get("credit_score"))

        # SIMPLE LOGIC (for demo & viva)
        if credit_score < 600 and balance > 50000:
            result = "Customer WILL EXIT"
        else:
            result = "Customer will NOT Exit"

    return render(request, "predict.html", {"result": result})
