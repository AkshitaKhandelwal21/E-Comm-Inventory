
from typing import Optional

from sqlmodel import Field, SQLModel


class Category(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    desc: Optional[str]


class CategoryUpdate(SQLModel):
    name: Optional[str]
    desc: Optional[str]