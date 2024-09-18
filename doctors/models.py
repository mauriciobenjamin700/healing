"""
- Tables:
    - Category
    - Doctor

"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Doctor(models.Model):
    """
    - crm: CharField
    - name: CharField
    - cep: CharField
    - street: CharField
    - neiborhood: CharField
    - house_number: CharField
    - rg_image: ImageField
    - medical_identity - ImageField
    - profile_image: ImageField
    - description: TextField
    - consultation_price: FloatField
    - user: ForeignKey User
    - category: ForeignKey Category
    
    """
    crm = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    street = models.CharField(max_length=100)
    neiborhood = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    rg_image = models.ImageField(upload_to='doctors/rgs')
    medical_identity = models.ImageField(upload_to='doctors/medical_identity')
    profile_image = models.ImageField(upload_to='doctors/profiles')
    description = models.TextField()
    consultation_price = models.FloatField()
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    
    
    def __str__(self) -> str:
        return self.user.username
    
    
def is_doctor(request):
    return Doctor.objects.filter(user=request.user).exists()