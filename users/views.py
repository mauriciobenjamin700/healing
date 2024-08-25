from django.shortcuts import render, redirect
from django.http import HttpResponse
from schemas.user import UserRequest
# Create your views here.
def register(request) -> HttpResponse:
    
    if request.method == "GET":
    
        return render(request, "register.html")
    
    elif request.method == "POST":
        try:
        #print(request.POST)
            user = UserRequest(
                name=request.POST.get("username"),
                email=request.POST.get("email"),
                password=request.POST.get("password"),
                confirm_password=request.POST.get("confirm_password")
            )
            return HttpResponse(f"Cadastro Realizado co Sucesso: {user.name}") 
        except:
            return redirect("/users/register/")
        
        #return render(request, "register.html")