from sqlalchemy import Column, Integer, ForeignKey,table
from sqlalchemy.ext.declarative import declarative_base     
from sqlalchemy.orm import relationship

Base = declarative_base();

class UsuarioRoles(Base):
    __tablename__ = 'informe_proyectos'
    informe_id = Column(Integer, ForeignKey('informes.id'),primary_key=True)
    proyecto_id = Column(Integer, ForeignKey('proyectos.id'),primary_key=True)
    ## aqui se arman las relaciones
    usuario = relationship("Informe", back_populates="informes")
    rol = relationship("Proyecto", back_populates="proyectos")