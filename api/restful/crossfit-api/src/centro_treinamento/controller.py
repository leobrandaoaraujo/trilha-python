from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from centro_treinamento.models import CentroTreinamentoModel
from centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from contrib.repository.dependencies import DatabaseDependency

router = APIRouter()

@router.post("/", summary="Criar um novo centro de treinamento", status_code=status.HTTP_201_CREATED, response_model=CentroTreinamentoOut)
async def post(db_session: DatabaseDependency, new_centro_treinamento: CentroTreinamentoIn = Body("")) -> CentroTreinamentoOut:
    centro_treinamento = CentroTreinamentoOut(id=uuid4(), **new_centro_treinamento.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento.model_dump())
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    return centro_treinamento

@router.get("/", summary="Listar centros de treinamento", status_code=status.HTTP_200_OK, response_model=list[CentroTreinamentoOut])
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    centros_treinamento: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    return [CentroTreinamentoOut.model_validate(centro_treinamento) for centro_treinamento in centros_treinamento]

@router.get("/{id}", summary="Consultar um centro de treinamento pelo ID", status_code=status.HTTP_200_OK, response_model=CentroTreinamentoOut)
async def get(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento: CentroTreinamentoOut = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"O centro de treinamento com o id {id} não foi encontrado!")
    else:
        return centro_treinamento