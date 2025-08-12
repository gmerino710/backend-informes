from pydantic import BaseModel

class ProyectoBase(BaseModel):
    nombre: str
    descripcion: str
    estado:bool = True
    

class ProyectoCreate(ProyectoBase):
    nombre: str
    descripcion: str
    estado:bool = True
    
    

class ProyectoResponse(ProyectoBase):
    id: int

    class Config:
        orm_mode = True