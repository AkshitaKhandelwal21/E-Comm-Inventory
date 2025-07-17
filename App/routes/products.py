from fastapi import APIRouter
from sqlmodel import select
from App.conn.db import SessionDep
from App.models.products import Product, ProductUpdate

prod = APIRouter()

@prod.get("/products")
def get_products(session: SessionDep):
    products = session.exec(select(Product)).all()
    return products


@prod.get("/products/{id}")
def update_product(id: int, session: SessionDep):
    product = session.get(Product, id)
    return product


@prod.post("/post_product")
def post_product(product: Product, session: SessionDep):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@prod.patch("/update_product")
def update_product(id: int, data:ProductUpdate, session: SessionDep):
    product = session.get(Product, id)
    prod_data = data.model_dump(exclude_unset=True)

    for key, value in prod_data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()
    session.refresh(product)

    return product


@prod.delete("/delete_product")
def delete_product(id: int, session: SessionDep):
    product = session.get(Product, id)
    session.delete(product)
    session.commit()
    return f"Product {id} deleted successfully"