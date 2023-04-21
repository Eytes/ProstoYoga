from fastapi.responses import HTMLResponse

from backend.config import app
from backend.models import Client
from backend.database.interfaces import clients


@app.get("/")
def root():
    return HTMLResponse(content="<b>Hello</b>")


@app.get('/users')
def get_users(limit: int = 10, offset: int = 0):
    return clients(limit, offset)


@app.post("/register")
def user_registration(client: Client):
    ...
