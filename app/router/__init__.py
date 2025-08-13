from .proyectos import router as proyectos_router
from .usuarios import router as usuarios_router;
from .gemini_api import router as gemini_api_router
from fastapi import APIRouter
router = APIRouter()
router.include_router(proyectos_router, prefix="/proyectos", tags=["proyectos"])
router.include_router(usuarios_router, prefix="/usuarios", tags=["usuarios"])  

router.include_router(gemini_api_router, prefix="/generative", tags=["generative_ai"])