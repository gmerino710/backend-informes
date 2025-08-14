from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,Date
from datetime import datetime
from sqlalchemy.orm import relationship
from app.core.database import Base  # MISMO Base que en Usuario

class Informe(Base):
    __tablename__ = 'informes'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(String(255))
    fecha_generacion = Column(DateTime, nullable=False, default=datetime.utcnow)
    estado = Column(String(50), nullable=False)
    encargado_id = Column(Integer, ForeignKey('usuarios.id'))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_modificacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    creado_por = Column(Integer)
    modificado_por = Column(Integer)
    id_proyecto = Column(Integer, ForeignKey('proyectos.id'))

    proyecto = relationship("Proyecto", back_populates="informes")
    encargado = relationship("Usuario", back_populates="informes")