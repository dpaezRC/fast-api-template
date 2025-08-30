from beanie import Document
from typing import Optional
from pydantic import BaseModel


class Category(BaseModel):
    name: str
    description: str


class Product(Document):
    name: str
    description: Optional[str] = None
    price: float
    category: Category

    class Settings:
        name = "products"
        indexes = [
            "price",
            "name",
        ]
