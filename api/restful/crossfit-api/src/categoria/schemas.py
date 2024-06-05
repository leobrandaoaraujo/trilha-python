from typing import Annotated
from pydantic import UUID4, Field, PositiveFloat
from contrib.repository.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome da categoria", example="Scale", max_length=10)
    ]

class CategoriaIn(Categoria):
    pass
    
class CategoriaOut(Categoria):
    pk_id: Annotated[UUID4, Field(description="Identificador único")]