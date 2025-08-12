from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse;
from app.models.proyectos import Proyecto;
from sqlalchemy.orm import Session 
from app.core.database import get_db  # Asegúrate de que esta función esté definida para obtener la sesión de la base de datos
from app.schemas.proyecto_schema import ProyectoBase, ProyectoCreate,ProyectoResponse

router = APIRouter()

@router.get("/", response_model=list[ProyectoResponse], status_code=status.HTTP_200_OK)
async def get(db:Session= Depends(get_db)):
    proyectos = db.query(Proyecto).all()
    if not proyectos:
        return JSONResponse(
            status_code=404,
            content={"message": "No se encontraron proyectos"}
        )
    return proyectos

@router.post("/", response_model=ProyectoResponse, status_code=status.HTTP_201_CREATED)
async def create_proyecto(proyecto: ProyectoCreate, db: Session = Depends(get_db)):
    try :
        nuevo_proyecto = Proyecto(**proyecto.dict())
        # Aquí puedes agregar lógica adicional si es necesario, como validaciones o transformaciones
        db.add(nuevo_proyecto)
        db.commit()
        db.refresh(nuevo_proyecto)
        return nuevo_proyecto 
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear el proyecto: {str(e)}"
        )        
@router.put("/{proyecto_id}", response_model=ProyectoResponse)
async def update_proyecto(proyecto_id: int, proyecto: ProyectoCreate, db: Session = Depends(get_db)):
   try: 
        existing_proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()
        print(existing_proyecto)
        
        if not existing_proyecto:
            raise HTTPException(status_code=404, detail="Proyecto no encontrado")
        
        for key, value in proyecto.dict().items():
            setattr(existing_proyecto, key, value)
        
        db.commit()
        db.refresh(existing_proyecto)
        return existing_proyecto  
   except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar el proyecto: {str(e)}"
        )                  

@router.put("/{proyecto_id}/estado", response_model=ProyectoResponse)
async def update_estado_proyecto(proyecto_id: int, db: Session = Depends(get_db)):
    try:
        existing_proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()
        
        if not existing_proyecto:
            raise HTTPException(status_code=404, detail="Proyecto no encontrado")
        print(existing_proyecto.estado)
        existing_proyecto.estado = not existing_proyecto.estado 
        print(existing_proyecto.estado,'cambio')
        db.commit()
        db.refresh(existing_proyecto)
        return existing_proyecto
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar el estado del proyecto: {str(e)}"
        )              