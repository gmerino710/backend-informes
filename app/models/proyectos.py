from sqlalchemy import Column, Integer, String,Boolean 
from sqlalchemy.orm import relationship
from app.core.database import Base # <- Corregido

class Proyecto(Base):
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    estado = Column(Boolean , default=True)  # 1 para activo, 0 para inactivo
    informes = relationship("Informe", back_populates="proyecto")

'''
# También puedes crear un modelo Pydantic para la respuesta de la API
from pydantic import BaseModel

class ProyectoBase(BaseModel):
    nombre: str
    descripcion: str

class ProyectoCreate(ProyectoBase):
    pass

class Proyecto(ProyectoBase):
    id: int

    class Config:
        orm_mode = True
'''
