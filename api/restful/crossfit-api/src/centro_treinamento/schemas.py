from typing import Annotated
from pydantic import UUID4, Field
from contrib.repository.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento", example="King", max_length=20
        ),
    ]
    endereco: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="Rua A, 123, São José",
            max_length=60,
        ),
    ]
    proprietario: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="Marcus Silva",
            max_length=30,
        ),
    ]

class CentroTreinamentoIn(CentroTreinamento):
    pass
    
class CentroTreinamentoOut(CentroTreinamento):
    pk_id: Annotated[UUID4, Field(description="Identificador único")]