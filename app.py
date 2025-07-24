from fastapi import FastAPI
from App.routes.healthcheck import hc
from App.routes.products import prod
from App.routes.category import cat
from App.routes.user import user
from App.conn.db import create_db

app = FastAPI(title="Main API", docs_url="/docs")

# Include all routers with prefixes
app.include_router(hc)
app.include_router(prod, tags=["Products"])
app.include_router(user, tags=["Users"])
app.include_router(cat, tags=["Categories"])

@app.on_event("startup")
def on_startup():
    create_db()
