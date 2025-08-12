from sqlalchemy import Column, Integer, ForeignKey,table
from sqlalchemy.ext.declarative import declarative_base     
from sqlalchemy.orm import relationship

Base = declarative_base();

class RolItemsMenu(Base):
    __tablename__ = 'rol_items_menu'
    item_menu_id = Column(Integer, ForeignKey('items_menu.id'),primary_key=True)
    rol_id = Column(Integer, ForeignKey('roles.id'),primary_key=True)
    ## aqui se arman las relaciones
    item_menu = relationship("ItemMenu", back_populates="roles")
    rol = relationship( "Roles", back_populates="items_menu")