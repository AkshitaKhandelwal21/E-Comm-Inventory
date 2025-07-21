from fastapi import APIRouter
from sqlmodel import select

from App.conn.db import SessionDep
from App.models.users import User, UserUpdate

user = APIRouter()

@user.post("/new_user")
def new_user(user: User,session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@user.get("/users")
def get_users(session: SessionDep):
    users = session.exec(select(User)).all()
    return users

@user.patch("/update_user")
def update_user(id: int, data: UserUpdate, session: SessionDep):
    user = session.get(User, id)
    new_data = data.model_dump(exclude_unset=True)

    for key, value in new_data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@user.delete("/delete_user")
def delete_user(id: int, session: SessionDep):
    user = session.get(User, id)
    session.delete(user)
    session. commit()
    return f"User {user.id} deleted successfully"