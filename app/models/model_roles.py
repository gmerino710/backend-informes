from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from app.core.database import Base # <- Corregido

class Roles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_modificacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    creado_por = Column(Integer, nullable=False)
    modificado_por = Column(Integer, nullable=False)