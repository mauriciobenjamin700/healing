from django.shortcuts import render


def doctor_register(request):
    if request.method == "GET":
        detail = "1"
        return render(request, "doctor_register.html", context={"detail": detail})