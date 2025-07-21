from typing import Optional
from sqlmodel import Field, SQLModel


class Supplier(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    contact: str
    address: str

class SupplierUpdate(SQLModel):
    name: Optional[str]
    address: Optional[str]

