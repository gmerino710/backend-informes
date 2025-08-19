from pydantic import BaseModel,field_validator
from typing import Optional
from datetime import date
from .usuario_schema import UsuarioBase
from .proyecto_schema import ProyectoResponse
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
    proyecto: ProyectoResponse
    encargado: UsuarioBase
    id_proyecto: int


    class Config:
        orm_mode = True  
        from_attributes = True
