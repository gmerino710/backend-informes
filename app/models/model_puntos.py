from sqlalchemy import Column, Integer, String, DateTime, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Puntos(Base):
    __tablename__ = 'puntos'

    id = Column(Integer, primary_key=True)
    escenario_id = Column(Integer, ForeignKey('escenarios.id'))  # Clave foránea que enlaza con la tabla de escenarios
    descripcion = Column(String(255), nullable=False)
    estado = Column(Integer)
    comentario = Column(String(255))
    captura_pantalla = Column(String(255))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_modificacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    creado_por = Column(Integer)
    modificado_por = Column(Integer)