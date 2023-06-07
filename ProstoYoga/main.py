from fastapi.responses import HTMLResponse

from config import app
from models import Client
from database.interfaces import clients


@app.get("/")
def root():
    return HTMLResponse(content="<b>Hello</b>")


@app.get('/users')
def get_users(limit: int = 10, offset: int = 0):
    return clients(limit, offset)


@app.post("/register")
def user_registration(client: Client):
    ...
