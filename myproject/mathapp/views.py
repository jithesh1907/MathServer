from django.shortcuts import render

def power_calculator(request):
    result = None
    if request.method == "POST":
        current = float(request.POST.get("current"))
        resistance = float(request.POST.get("resistance"))
        result = (current ** 2) * resistance

    return render(request, "power_calculator.html", {"result": result})
