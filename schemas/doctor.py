from django.core.files.uploadedfile import (
    InMemoryUploadedFile,
    TemporaryUploadedFile
)
from pydantic import (
    field_validator,
    model_validator
)


from schemas.base import CustomBaseModel


class DoctorRequest(CustomBaseModel):
    """
    - crm: str
    - name: str
    - cep: str
    - street: str
    - neiborhood: str
    - house_number: str
    - rg_image: str
    - medical_identity: str
    - profile_image: str
    - description: str
    - consultation_price: float
    """
    crm: str
    name: str
    cep: str
    street: str
    neiborhood: str
    house_number: str
    rg_image: InMemoryUploadedFile | TemporaryUploadedFile
    medical_identity: InMemoryUploadedFile | TemporaryUploadedFile
    profile_image: InMemoryUploadedFile | TemporaryUploadedFile
    description: str
    consultation_price: float
    category: str
    
    class Config: # Permitindo tipos de dados diferentes dos primitivos como as classes do django
        arbitrary_types_allowed = True
    

    @field_validator("crm")
    def validate_crm(cls, value):
        #if len(value) != 10:
        if not value or value.strip() == "":
            raise ValueError("CRM inválido")
        return value
    
    @field_validator("name")
    def validate_name(cls, value):
        if not value or value.strip() == "":
            raise ValueError("Nome inválido")
        return value
    
    @field_validator("cep")
    def validate_cep(cls, value):
        if len(value) != 8:
            raise ValueError("CEP inválido")
        return value
    
    @field_validator("street")
    def validate_street(cls, value):
        if not value or value.strip() == "":
            raise ValueError("Rua inválida")
        return value
    
    @field_validator("neiborhood")
    def validate_neiborhood(cls, value):
        if not value or value.strip() == "":
            raise ValueError("Bairro inválido")
        return value
    
    @field_validator("house_number")
    def validate_house_number(cls, value):
        if not value or value.strip() == "":
            raise ValueError("Número inválido")
        return value
    
    @model_validator(mode="before")
    def validade_files(cls, value):
        images = [value.get("rg_image"), value.get("medical_identity"), value.get("profile_image")]
        
        for image in images:
            if image is None:
                raise ValueError("Imagem obrigatória")
            if value is not None and not isinstance(image, (InMemoryUploadedFile, TemporaryUploadedFile)):
                raise TypeError(f"Tipo de image invalido: {type(value)}")
        
        return value 
    
    @field_validator("description")
    def validate_description(cls, value):
        if not value or value.strip() == "":
            raise ValueError("Descrição inválida")
        return value
    
    @field_validator("consultation_price")
    def validate_consultation_price(cls, value):
        if value < 0:
            raise ValueError("Preço da consulta inválido")
        return value