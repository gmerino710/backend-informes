from fastapi import APIRouter,Depends,status;
from fastapi.responses import JSONResponse;
from app.models.proyectos import Proyecto;
from sqlalchemy.orm import Session 
from app.core.database import get_db  # Asegúrate de que esta función esté definida para obtener la sesión de la base de datos
from app.schemas.proyecto_schema import ProyectoBase, ProyectoCreate

router = APIRouter()

@router.get("/", response_model=list[ProyectoBase])
async def get(db:Session= Depends(get_db)):
    proyectos = db.query(Proyecto).all()
    if not proyectos:
        return JSONResponse(
            status_code=404,
            content={"message": "No se encontraron proyectos"}
        )
    return proyectos