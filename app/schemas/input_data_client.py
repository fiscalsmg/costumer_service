from pydantic import BaseModel, validator

class Costumer(BaseModel):
    nombre: str
    apellido: str

class InputDataClient(BaseModel):
    nombreClient: Costumer
    telefono: int
    edad: int

    # Se debe validar telefono a 10 digitos, de lo contrario regresar un error
    @validator("telefono", always=True)
    def in_case_incomplete_phone_number(cls, telefono):
        telefono_str: str = str(telefono)
        if len(telefono_str) == 10:
            return telefono
        else:
            raise ValueError("Phone Number Invalid")

    #Se debe validar edad mayor de 18 años, de lo contrario regresar un error
    @validator("edad", always=True)
    def in_case_age_not_allowed(cls, edad):
        if edad > 18:
            return edad
        else:
            raise ValueError("Age Invalid")
        
        
class UpdateInputDataClient(BaseModel):
    nombreClient: Costumer
    edad: int

    @validator("edad", always=True)
    def in_case_age_not_allowed(cls, edad):
        if edad > 18:
            return edad
        else:
            raise ValueError("Age Invalid")