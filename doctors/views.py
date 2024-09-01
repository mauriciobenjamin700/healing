from django.shortcuts import render


def register(request):
    if request.method == "GET":
        return render(request, "doctor_register.html")