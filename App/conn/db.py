from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, SQLModel, Session
from App.models.products import Product, Category
from App.models.users import User

sqlite_file_name = "inventory.db"

DATABASE_URL = f"sqlite:///{sqlite_file_name}"

engine = create_engine(DATABASE_URL, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)
    print("DB tables created successfully")

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]