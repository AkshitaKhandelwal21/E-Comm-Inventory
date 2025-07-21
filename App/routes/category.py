from fastapi import APIRouter
from sqlmodel import select

from App.conn.db import SessionDep
from App.models.category import Category, CategoryUpdate

cat = APIRouter()

@cat.get("/categories")
def get_categories(session: SessionDep):
    categories = session.exec(select(Category)).all()
    return categories

@cat.get("/category")
def get_category_by_id(id: int, session: SessionDep):
    category = session.get(Category, id)
    return category

@cat.post("/post_category")
def add_category(category: Category, session: SessionDep):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

@cat.patch("/update_category")
def update_category(id: int, session: SessionDep, data: CategoryUpdate):
    category = session.get(Category, id)
    updated_data = data.model_dump(exclude_unset=True)

    for key, value in updated_data.items():
        setattr(category, key, value)

    session.add(category)
    session.commit()
    session.refresh(category)

    return category


@cat.delete("/delete_category")
def delete_category(id: int, session: SessionDep):
    category = session.get(Category, id)
    session.delete(category)
    session.commit()

    return f"Category {category} deleted successfully"