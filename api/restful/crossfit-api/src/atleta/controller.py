import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from pydantic import UUID4
import sqlalchemy
from sqlalchemy.future import select
from atleta.models import AtletaModel
from atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from categoria.models import CategoriaModel
from categoria.schemas import CategoriaOut
from centro_treinamento.models import CentroTreinamentoModel
from centro_treinamento.schemas import CentroTreinamentoOut
from contrib.repository.dependencies import DatabaseDependency

router = APIRouter()

@router.post("/", summary="Criar um novo atleta", status_code=status.HTTP_201_CREATED, response_model=AtletaOut)
async def post(db_session: DatabaseDependency, new_atleta: AtletaIn = Body("")) -> AtletaOut:
    categoria: CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(nome=new_atleta.categoria.nome))).scalars().first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"A categoria {new_atleta.categoria.nome} não foi encontrada!")
    
    centro_treinamento: CentroTreinamentoOut = (await db_session.execute(select(CentroTreinamentoModel).filter_by(nome=new_atleta.centro_treinamento.nome))).scalars().first()
    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"O centro de treinamento {new_atleta.centro_treinamento.nome} não foi encontrada!")
    
    try:
        atleta = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **new_atleta.model_dump())
        atleta_model = AtletaModel(**atleta.model_dump(exclude={"categoria", "centro_treinamento"}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id
        db_session.add(atleta_model)
        await db_session.commit()
    except Exception:
        raise sqlalchemy.exc.IntegrityError(status_code=status.HTTP_303_SEE_OTHER, detail=f"O CPF {new_atleta.cpf} já existe na base de dados!")
    return atleta

@router.get("/", summary="Listar atletas", status_code=status.HTTP_200_OK, response_model=list[AtletaOut])
async def query(db_session: DatabaseDependency) -> list[AtletaOut]:
    atletas: list[AtletaOut] = (await db_session.execute(select(AtletaModel))).scalars().all()
    
    return paginate([AtletaOut.model_validate(atleta) for atleta in atletas])

@router.get("/{id}", summary="Consultar um atleta pelo ID", status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def get(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"O atleta com o id {id} não foi encontrado!")
    else:
        return atleta

@router.get("/{nome}", summary="Consultar um atleta pelo NOME", status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def get(nome: str, db_session: DatabaseDependency) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(nome=nome))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"O atleta {nome} não foi encontrado!")
    else:
        return atleta

@router.get("/{cpf}", summary="Consultar um atleta pelo CPF", status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def get(cpf: str, db_session: DatabaseDependency) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(cpf=cpf))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"O atleta com o CPF {cpf} não foi encontrado!")
    else:
        return atleta
    
@router.patch("/{id}", summary="Editar um atleta pelo ID", status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def get(id: UUID4, db_session: DatabaseDependency, chg_atleta: AtletaUpdate = Body("")) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"O atleta com o id {id} não foi encontrado!")
    else:
        atleta_update = chg_atleta.model_dump(exclude_unset=True)
        for key, value in atleta_update.items():
            setattr(atleta, key, value)
        await db_session.commit()
        await db_session.refresh(atleta)
        return atleta
    
@router.delete("/{id}", summary="Excluir um atleta pelo ID", status_code=status.HTTP_204_NO_CONTENT)
async def get(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"O atleta com o id {id} não foi encontrado!")
    else:
        db_session.delete(atleta)
        await db_session.commit()