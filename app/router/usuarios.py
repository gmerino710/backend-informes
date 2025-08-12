from fastapi import APIRouter,status
from fastapi.responses import JSONResponse;
from app.schemas.proyecto_schema import ProyectoBase, ProyectoCreate
router = APIRouter();

@router.get("/usuarios-2", response_model=list[ProyectoBase])
async def get_proyectos():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=[{"id": 1, "name": "Proyecto 1"}]
    )   
    

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]