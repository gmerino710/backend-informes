from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base     
from sqlalchemy.orm import relationship

Base = declarative_base();

class UsuarioRoles(Base):
    __tablename__ = 'usuario_roles'
    usuario_id = Column(Integer, ForeignKey('usuarios.id'),primary_key=True)
    rol_id = Column(Integer, ForeignKey('roles.id'),primary_key=True)
    ## aqui se arman las relaciones
    usuario = relationship("Usuarios", back_populates="roles")
    rol = relationship("Roles", back_populates="usuarios")