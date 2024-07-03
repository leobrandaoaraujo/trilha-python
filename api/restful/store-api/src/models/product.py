from src.models.base import CreateBaseModel
from src.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    ...