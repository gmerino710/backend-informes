from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship
from app.core.database import Base  # Usa SIEMPRE el mismo Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    correo_electronico = Column(String(255), unique=True, nullable=False)
    contrasena_hash = Column(String(255), nullable=False)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_modificacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    creado_por = Column(Integer, nullable=False)
    modificado_por = Column(Integer, nullable=False)

    informes = relationship("Informe", back_populates="encargado")
