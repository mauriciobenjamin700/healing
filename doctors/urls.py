from django.urls import path

from doctors import views

urlpatterns = [
    path("doctor_register/", views.register, name="doctor_register"),
]