import select
from fastapi import APIRouter, Depends
from sqlmodel import Session
from App.conn.db import get_session
from App.models.users import User, UserUpdate
from App.utils.jwt import require_admin

user = APIRouter()

@user.get("/users")
def get_all_users(admin: User = Depends(require_admin), session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users

@user.patch("/update_user")
def update_user(id:int, data: UserUpdate, session: Session = Depends(get_session)):
    user = session.get(User, id)
    new_data = data.model_dump(exclude_unset=True)

    for key, value in new_data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@user.delete("/delete_user")
def delete_user(id: int, session: Session=Depends(get_session)):
    user = session.get(User, id)
    session.delete(user)
    session. commit()
    return f"User {user.id} deleted successfully"