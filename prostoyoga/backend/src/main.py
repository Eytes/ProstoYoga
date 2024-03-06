from fastapi import FastAPI

app = FastAPI(
    title="ProstoYogaAPI",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)
