from pydantic import BaseModel

class ProyectoBase(BaseModel):
    nombre: str
    descripcion: str
    id: int | None = None,
    estado:bool = True
    

class ProyectoCreate(ProyectoBase):
    pass

class Proyecto(ProyectoBase):
    id: int

    class Config:
        orm_mode = True