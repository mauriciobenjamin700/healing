from django.urls import path

from doctors import views

urlpatterns = [
    path("doctor_register/", views.doctor_register, name="doctor_register"),
]