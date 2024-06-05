from typing import Annotated
from pydantic import BaseModel, UUID4, Field
from datetime import datetime


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True
        
class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description="Identificador único")]
    created_at: Annotated[datetime, Field(description="Data de criação")]