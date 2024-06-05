from fastapi import APIRouter
from atleta.controller import router as atleta
from centro_treinamento.controller import router as centro_treinamento
from categoria.controller import router as categoria

api_router = APIRouter()
api_router.include_router(atleta, prefix="/atletas", tags=["atletas"])
api_router.include_router(centro_treinamento, prefix="/centros_treinamento", tags=["centros_treinamento"])
api_router.include_router(categoria, prefix="/categorias", tags=["categorias"])