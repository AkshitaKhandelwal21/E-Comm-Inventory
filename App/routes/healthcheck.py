from fastapi import APIRouter

hc = APIRouter()

@hc.get('/')
def healthcheck():
    return "Healthcheck successful: 200 OK"