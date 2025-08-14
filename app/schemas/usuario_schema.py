from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    correo_electronico: str
    activo: bool = True
    
class UsuarioCreate(UsuarioBase):
    contrasena: str         
    
 
class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    correo_electronico: Optional[str] = None
    contrasena: Optional[str] = None
    activo: Optional[bool] = None   
    
              
class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        orm_mode = True             