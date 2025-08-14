from pydantic import BaseModel,field_validator
from typing import Optional
from datetime import date

class InformeBase(BaseModel):
    titulo: str
    descripcion: str
    encargado_id: int
    estado: bool = True 
    fecha_generacion: date

class InformeCreate(InformeBase):
    titulo: str
    descripcion: str
    encargado_id: int
    id_proyecto: int
    estado: bool = True 
    fecha_generacion: date

    
class InformeResponse(InformeBase):     
    id: int

    class Config:
        orm_mode = True  
            