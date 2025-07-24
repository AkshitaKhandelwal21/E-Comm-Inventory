from fastapi import APIRouter, Request

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

hc = APIRouter()

@hc.get('/', response_class=HTMLResponse)
def healthcheck(request: Request):
    return "Healthcheck successful: 200 OK"