from sqlmodel import SQLModel, Field
from typing import Optional
from App.models.category import Category
from App.models.supplier import Supplier


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    desc: str
    quantity: int
    price: float
    category_id: int = Field(foreign_key="category.id")
    # supplier_id: int = Field(foreign_key="supplier.id")

class ProductUpdate(SQLModel):
    name: Optional[str]
    quantity: Optional[int]
    price: Optional[float]
    category_id: Optional[int]

class ProductCreate(SQLModel):
    name: str
    desc: str
    quantity: int
    price: float
    category_name: str




