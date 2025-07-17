from fastapi import FastAPI
from App.routes.healthcheck import hc
from App.conn.db import create_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()

app.include_router(hc)