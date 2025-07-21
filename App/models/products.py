from sqlmodel import SQLModel, Field
from typing import Optional
from App.models.category import Category


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    desc: str
    quantity: int
    price: float
    category_id: str = Field(foreign_key="category.id")


class ProductUpdate(SQLModel):
    name: Optional[str]
    quantity: Optional[int]
    price: Optional[float]
    category_id: Optional[int]



