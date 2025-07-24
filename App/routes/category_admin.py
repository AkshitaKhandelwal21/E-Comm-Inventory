from fastapi import APIRouter, Body, Depends
from sqlmodel import Session
from App.conn.db import get_session
from App.models.category import Category, CategoryCreate, CategoryUpdate

from App.models.users import User
from App.utils.jwt import require_admin


cat = APIRouter()

@cat.post("/post_category")
def add_category(admin:User=Depends(require_admin), category: CategoryCreate = Body(...), session:Session=Depends(get_session)):
    new_cat = Category(**category.model_dump()) 
    session.add(new_cat)
    session.commit()
    session.refresh(new_cat)
    return new_cat

@cat.patch("/update_category")
def update_category(id: int, admin:User=Depends(require_admin), session:Session=Depends(get_session), data:CategoryUpdate=Body(...)):
    category = session.get(Category, id)
    updated_data = data.model_dump(exclude_unset=True)

    for key, value in updated_data.items():
        setattr(category, key, value)

    session.add(category)
    session.commit()
    session.refresh(category)

    return category


@cat.delete("/delete_category")
def delete_category(id: int, user:User=Depends(require_admin), session: Session=Depends(get_session)):
    category = session.get(Category, id)
    session.delete(category)
    session.commit()

    return f"Category {category} deleted successfully"