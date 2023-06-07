from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from models import Client
from database.interfaces import clients

app = FastAPI(
    title="ProstoYoga"
)


@app.get("/")
def root():
    return HTMLResponse(content="<b>Hello</b>")


@app.get('/users')
def get_users(limit: int = 10, offset: int = 0):
    return clients(limit, offset)


@app.post("/register")
def user_registration(client: Client):
    ...
