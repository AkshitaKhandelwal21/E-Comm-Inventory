from fastapi import APIRouter, Body, Depends
from sqlmodel import Session, select
from App.models.users import User
from App.routes.category_admin import cat
from App.conn.db import SessionDep, get_session
from App.models.category import Category, CategoryCreate, CategoryUpdate
from App.utils.jwt import require_admin


@cat.get("/categories")
def get_categories(session:Session=Depends(get_session)):
    categories = session.exec(select(Category)).all()
    return categories

@cat.get("/category")
def get_category_by_name(name: str, session: SessionDep):
    cat = session.exec(select(Category).where(Category.name==name)).first()
    return cat
