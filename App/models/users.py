from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str
    role: str

class UserUpdate(SQLModel):
    name: Optional[str]