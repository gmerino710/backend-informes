from fastapi import status,Depends, HTTPException,APIRouter
from fastapi.responses import JSONResponse;
from app.schemas.informe_schema import  InformeCreate,InformeResponse
from app.models.model_informes import Informe
from sqlalchemy.orm import Session    
from app.core.database import get_db  
router = APIRouter()



@router.get("/", response_model=list[InformeResponse], status_code=status.HTTP_200_OK )
def get_informes(db: Session = Depends(get_db)):
    informes = db.query(Informe).all()
    return informes
    
@router.get("/{informe_id}", response_model=InformeResponse, status_code=status.HTTP_200_OK )
def get_informe(informe_id: int, db: Session = Depends(get_db)):
    informe = db.query(Informe).filter(Informe.id == informe_id).first()
    if not informe:
        return JSONResponse(
            status_code=404,
            content={"message": "Informe no encontrado"}
        )
    return informe             

@router.post("/", response_model=InformeResponse, status_code=status.HTTP_201_CREATED )
def create_informe(informe: InformeCreate, db: Session = Depends(get_db)):
    try:
        nuevo_informe = Informe(**informe.model_dump())
        db.add(nuevo_informe)
        db.commit()
        db.refresh(nuevo_informe)
        return nuevo_informe
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear el informe: {str(e)}"
        )        

