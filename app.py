from fastapi import FastAPI
from App.routes.healthcheck import hc

app = FastAPI()

app.include_router(hc)