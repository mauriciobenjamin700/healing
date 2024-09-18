from django.shortcuts import (
    render,
    redirect
)
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants


from doctors.models import (
    Category, 
    Doctor,
    is_doctor
    
)
from schemas.doctor import DoctorRequest


def doctor_register(request):
    try:
        if request.method == "GET":
            
            
            
            if not is_doctor(request):
            
                categories = Category.objects.all()
                return render(request, "doctor_register.html", context={"categories": categories})
            
            else:
                messages.add_message(request, constants.ERROR, "Você já possui um médico cadastrado")
                return redirect("/doctor/calendar")
        
        elif request.method == "POST":
            # TODO: Implementar validações e salvar dados do médico no banco de dados.
            doctor_request = DoctorRequest(
                crm=request.POST.get("crm"),
                name=request.POST.get("name"),
                cep=request.POST.get("cep"),
                street=request.POST.get("street"),
                neiborhood=request.POST.get("neiborhood"),
                house_number=request.POST.get("house_number"),
                rg_image=request.FILES.get("rg_image"),
                medical_identity=request.FILES.get("medical_identity"),
                profile_image=request.FILES.get("profile_image"),
                description=request.POST.get("description"),
                consultation_price=request.POST.get("consultation_price"),
                category=request.POST.get("category")   
            )
            
            doctor_model = Doctor(
                crm=doctor_request.crm,
                name=doctor_request.name,
                cep=doctor_request.cep,
                street=doctor_request.street,
                neiborhood=doctor_request.neiborhood,
                house_number=doctor_request.house_number,
                rg_image=doctor_request.rg_image,
                medical_identity=doctor_request.medical_identity,
                profile_image=doctor_request.profile_image,
                description=doctor_request.description,
                consultation_price=doctor_request.consultation_price,
                user=request.user,
                category_id=doctor_request.category#Category.objects.get(pk=doctor_request.category)  # TODO: Implementar busca da categoria pelo ID.
            )
            
            doctor_model.save()
            
            messages.add_message(
                request, 
                constants.SUCCESS, 
                "Cadastro do médico  realizado com sucesso!"
            )
            
            return redirect("/doctor/calendar")
            #return HttpResponse("Médico cadastrado com sucesso!")
            #return HttpResponse(f"Cadastro do médico {doctor_request.category} realizado com sucesso!")
        
    except Exception as e:
        return HttpResponse(f"Erro ao cadastrar médico: {e}")   