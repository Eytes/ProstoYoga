from fastapi.responses import HTMLResponse

from config import app


@app.get("/")
def root():
    return HTMLResponse(content="<b>Hello</b>")


