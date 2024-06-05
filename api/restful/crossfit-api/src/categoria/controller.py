from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from categoria.models import CategoriaModel
from categoria.schemas import CategoriaIn, CategoriaOut
from contrib.repository.dependencies import DatabaseDependency

router = APIRouter()

@router.post("/", summary="Criar uma nova categoria", status_code=status.HTTP_201_CREATED, response_model=CategoriaOut)
async def post(db_session: DatabaseDependency, new_categoria: CategoriaIn = Body("")) -> CategoriaOut:
    categoria = CategoriaOut(id=uuid4(), **new_categoria.model_dump())
    categoria_model = CategoriaModel(**categoria.model_dump())
    db_session.add(categoria_model)
    await db_session.commit()
    return categoria

@router.get("/", summary="Listar categorias", status_code=status.HTTP_200_OK, response_model=list[CategoriaOut])
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    return [CategoriaOut.model_validate(categoria) for categoria in categorias]

@router.get("/{id}", summary="Consultar uma categoria pelo ID", status_code=status.HTTP_200_OK, response_model=CategoriaOut)
async def get(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria: CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()
    
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"A categoria com o id {id} não foi encontrada!")
    else:
        return categoria