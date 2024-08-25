from pydantic import BaseModel

class CustomBaseModel(BaseModel):
    
    def dict(self):
        d = super().model_dump()
        d = {k: v for k, v in d.items() if v is not None}
        return d