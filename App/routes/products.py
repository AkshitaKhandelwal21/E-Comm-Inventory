from fastapi import APIRouter, Body, Depends
from sqlmodel import Session, select
from App.conn.db import SessionDep, get_session
from App.models.category import Category
from App.models.products import Product, ProductCreate, ProductUpdate
from App.models.users import User
from App.routes.product_admin import prod
from App.utils.jwt import require_seller


@prod.get("/products")
def get_products(name: str, session: SessionDep):
    products = session.exec(select(Product).where(Product.name==name)).all()
    return products


@prod.get("/products/{id}")
def get_product_by_id(id: int, session: SessionDep):
    product = session.get(Product, id)
    return product


@prod.post("/post_product")
def post_product(user:User=Depends(require_seller), data:ProductCreate=Body(...), session: Session=Depends(get_session)):
    category = session.exec(select(Category).where(Category.name==data.category_name)).first()
    product = Product(
        name=data.name,
        desc=data.desc,
        quantity=data.quantity,
        price=data.price,
        category_id=category.id
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@prod.patch("/update_product")
def update_product(id: int, user:User=Depends(require_seller), data:ProductUpdate=Body(...), session:Session=Depends(get_session)):
    product = session.get(Product, id)
    prod_data = data.model_dump(exclude_unset=True)

    for key, value in prod_data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()
    session.refresh(product)

    return product


@prod.delete("/delete_product")
def delete_product(id: int, user:User=Depends(require_seller), session:Session=Depends(get_session)):
    product = session.get(Product, id)
    session.delete(product)
    session.commit()
    return f"Product {id} deleted successfully"