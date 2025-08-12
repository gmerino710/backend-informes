from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Se utiliza la base declarativa del modelo
Base = declarative_base()

class ItemMenu(Base):
    __tablename__ = 'items_menu'

    id = Column(Integer, primary_key=True)
    modulo_id = Column(Integer, ForeignKey('modulos_menu.id'))  # Clave foránea que apunta al id de la tabla 'modulos_menu'
    label = Column(String(255), nullable=False)
    icono = Column(String(255))
    router_link = Column(String(255))
    orden = Column(Integer)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_modificacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    creado_por = Column(Integer)
    modificado_por = Column(Integer)

    # Relación con el modelo ModuloMenu (si ya lo creaste)
    # modulo = relationship("ModuloMenu", back_populates="items")