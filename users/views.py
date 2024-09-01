from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import (
    constants as messages,
    add_message
)

from schemas import user
from schemas.user import (
    UserRequest,
    UserLogin
)


def register(request) -> HttpResponse:
    if request.method == "GET":
        return render(request, "register.html")
    
    elif request.method == "POST":
        try:
            user = UserRequest(
                name=request.POST.get("username"),
                email=request.POST.get("email"),
                password=request.POST.get("password"),
                confirm_password=request.POST.get("confirm_password")
            )
            
            users = User.objects.filter(username=user.name)
            if users.exists():
                raise ValueError("Usuário já existe")
            
            User.objects.create_user(
                username=user.name,
                email=user.email,
                password=user.password
            )    
            add_message(request, messages.SUCCESS, "Usuário registrado com sucesso")
            return redirect("/users/register/")

        except ValueError as e:
            add_message(request, messages.ERROR, str(e))
            return render(request, "register.html")
        except Exception as e:
            add_message(request, messages.ERROR, "Ocorreu um erro inesperado")
            return render(request, "register.html")


def login(request) -> HttpResponse:
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        try:
            user = UserLogin(
                email=request.POST.get("email"),
                password=request.POST.get("password")
            )
            
            user_on_db = auth.authenticate(
                request,
                username=user.email,  # auth.authenticate espera 'username' e 'password'
                password=user.password
            )
            
            if user_on_db:
                auth.login(request, user_on_db)
                return redirect("/clients/home")
            
            add_message(request, messages.ERROR, "Usuário ou senha incorretos")
            return render(request, "register.html")

        except Exception as e:
            add_message(request, messages.ERROR, "Ocorreu um erro inesperado")
            return render(request, "register.html")