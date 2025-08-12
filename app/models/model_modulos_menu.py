from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ModuloMenu(Base):
    __tablename__ = 'modulos_menu'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    icono = Column(String(255))
    orden = Column(Integer)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_modificacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    creado_por = Column(Integer)
    modificado_por = Column(Integer)