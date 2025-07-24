from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    hashed_password: str
    role: str


class UserCreate(SQLModel):
    name: str
    email: str
    password: str
    role: str


class UserLogin(SQLModel):
    email: str
    password: str


class UserRead(SQLModel):
    id: int
    name: str
    email: str


class UserUpdate(SQLModel):
    name: Optional[str]

