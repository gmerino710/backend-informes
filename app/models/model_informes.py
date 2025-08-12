from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Informe(Base):
    __tablename__ = 'informes'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(String(255))
    fecha_generacion = Column(DateTime, nullable=False, default=datetime.utcnow)
    estado = Column(String(50), nullable=False)
    encargado_id = Column(Integer, ForeignKey('usuarios.id')) # Foreign key to the users table
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_modificacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    creado_por = Column(Integer)
    modificado_por = Column(Integer)