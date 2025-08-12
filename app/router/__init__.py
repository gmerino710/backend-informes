from .proyectos import router as proyectos_router
from .usuarios import router as usuarios_router;

from fastapi import APIRouter
router = APIRouter()
router.include_router(proyectos_router, prefix="/proyectos", tags=["proyectos"])
router.include_router(usuarios_router, prefix="/usuarios", tags=["usuarios"])  