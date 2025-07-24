from fastapi import APIRouter, Body, Depends, HTTPException
from sqlmodel import Session, select
from App.conn.db import SessionDep, get_session
from App.models.users import User, UserCreate, UserLogin, UserUpdate
from App.utils.hash import hash_password, verify_password
from App.utils.jwt import create_access_token, get_current_user, require_admin
from fastapi import Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from App.routes.user_admin import user

@user.post("/token")
def login_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    db_user = session.exec(
        select(User).where(User.email == form_data.username)
    ).first()

    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    token = create_access_token(data={"sub": db_user.email, "user_id": db_user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@user.post("/register")
def new_user(user: UserCreate, session: SessionDep):
    hashed_pw = hash_password(user.password)
    new_user = User(name=user.name, email=user.email, hashed_password=hashed_pw, role=user.role)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


@user.post("/login")
def login_user(user: UserLogin, session: SessionDep):
    db_user = session.exec(select(User).where(User.email == user.email)).first()
    token = create_access_token(data={"sub": db_user.email, "user_id": db_user.id})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "name": db_user.name,
            "email": db_user.email
        }
    }

@user.get("/user")
def get_user(current_user: User = Depends(get_current_user)):
    return current_user

@user.patch("/update_user")
def update_user(current_user:User = Depends(get_current_user), data: UserUpdate = Body(...), session: Session = Depends(get_session)):
    user = session.get(User, current_user.id)
    new_data = data.model_dump(exclude_unset=True)

    for key, value in new_data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@user.delete("/delete_user")
def delete_user(current_user: User = Depends(get_current_user), session: Session=Depends(get_session)):
    user = session.get(User, current_user.id)
    session.delete(user)
    session. commit()
    return f"User {user.id} deleted successfully"