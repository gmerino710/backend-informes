from fastapi import APIRouter,status,Depends, HTTPException
from fastapi.responses import JSONResponse;
from app.schemas.usuario_schema import  UsuarioResponse
from app.models.model_usuarios import Usuario
from sqlalchemy.orm import Session    
from app.core.database import get_db   
router = APIRouter();

@router.get("/usuarios-list", response_model=list[UsuarioResponse], status_code=status.HTTP_200_OK)
async def get_usuarios(db:Session= Depends(get_db)):
    usuarios = db.query(Usuario).all()
    if not usuarios:
        return JSONResponse(
            status_code=404,
            content={"message": "No se encontraron usuarios"}
        )
    return usuarios 
@router.get("/usuarios-paginated", response_model=UsuarioResponse, status_code=status.HTTP_200_OK)
async def get_usuarios_paginated(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).offset(skip).limit(limit).all()
    try:
        if not usuarios:
            return JSONResponse(
                status_code=404,
                content={"message": "No se encontraron usuarios"}
            )
        return usuarios
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener los usuarios: {str(e)}"
        )
