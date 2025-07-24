from fastapi import APIRouter, Body, Depends
from sqlmodel import Session
from App.conn.db import get_session
from App.models.products import Product, ProductUpdate

from App.models.users import User
from App.utils.jwt import require_admin


prod = APIRouter()


@prod.patch("/update_product/admin")
def update_product(id: int, user:User=Depends(require_admin), data:ProductUpdate=Body(...), session:Session=Depends(get_session)):
    product = session.get(Product, id)
    prod_data = data.model_dump(exclude_unset=True)

    for key, value in prod_data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()
    session.refresh(product)

    return product


@prod.delete("/delete_product/admin")
def delete_product(id: int, user:User=Depends(require_admin), session:Session=Depends(get_session)):
    product = session.get(Product, id)
    session.delete(product)
    session.commit()
    return f"Product {id} deleted successfully"