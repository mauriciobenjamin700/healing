from pydantic import model_validator

from schemas.base import CustomBaseModel

class UserRequest(CustomBaseModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None
    confirm_password: str | None = None
    
    @model_validator(mode='before')
    def check_passwords_match(cls, values):
        password = values.get('password')
        confirm_password = values.get('confirm_password')
        
        if not password or not confirm_password:
            raise ValueError('Informe as duas senha corretamente')
        
        if password != confirm_password:
            raise ValueError('As senhas não coincidem')
        
        return values

class UserLogin(CustomBaseModel):
    email: str | None = None
    password: str | None = None
    
    @model_validator(mode='before')
    def check_passwords_match(cls, values):
        email = values.get('email')
        password = values.get('password')
        
        if not email or not password:
            raise ValueError('Informe o usuário e senha corretamente')
        
        return values