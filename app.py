from fastapi import Depends, FastAPI
from App.routes.healthcheck import hc
from App.routes.products import prod
from App.routes.category import cat
from App.routes.user import user
from App.conn.db import create_db, get_session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()

app.include_router(hc)
app.include_router(prod)
app.include_router(cat)
app.include_router(user)
