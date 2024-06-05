from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from categoria.schemas import Categoria
from centro_treinamento.schemas import CentroTreinamento
from contrib.repository.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do atleta", example="João", max_length=50)
    ]
    cpf: Annotated[
        str, Field(description="CPF do atleta", example="12345678911", max_length=11)
    ]
    idade: Annotated[int, Field(description="Idade do atleta", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=75.5)]
    altura: Annotated[
        PositiveFloat, Field(description="Altura do atleta", example=1.70)
    ]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
    categoria: Annotated[Categoria, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamento, Field(description="Centro de treinamento do atleta")]

class AtletaIn(Atleta):
    pass
    
class AtletaOut(Atleta, OutMixin):
    nome: Annotated[
        str, Field(description="Nome do atleta", example="João", max_length=50)
    ]
    centro_treinamento: Annotated[CentroTreinamento, Field(description="Centro de treinamento do atleta")]
    categoria: Annotated[Categoria, Field(description="Categoria do atleta")]

class AtletaUpdate(BaseSchema):
    nome: Annotated[
        Optional[str], Field(None, description="Nome do atleta", example="João", max_length=50)
    ]
    cpf: Annotated[
        Optional[str], Field(None, description="CPF do atleta", example="12345678911", max_length=11)
    ]
    idade: Annotated[Optional[int], Field(None, description="Idade do atleta", example=25)]
    peso: Annotated[Optional[PositiveFloat], Field(None, description="Peso do atleta", example=75.5)]
    altura: Annotated[
        Optional[PositiveFloat], Field(None, description="Altura do atleta", example=1.70)
    ]
    sexo: Annotated[Optional[str], Field(None, description="Sexo do atleta", example="M", max_length=1)]