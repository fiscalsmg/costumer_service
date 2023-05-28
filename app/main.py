from fastapi import FastAPI

from app.entrypoint import app_client

app: FastAPI = FastAPI(
    title="Servicio para consultar clientes",
    description="costumer service",
    docs_url="/docs",
)

app.include_router(app_client)
