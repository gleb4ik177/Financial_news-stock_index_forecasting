from logging import config as logging_config

from fastapi import FastAPI

from fastapi_service.api.v1 import model_server
from fastapi_service.settings.logger import LOGGING
from fastapi_service.settings.settings import settings

app = FastAPI(
    title=settings.project.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
)


@app.get("/")
async def root():
    return {"easter_egg": "https://youtu.be/dQw4w9WgXcQ?si=9kGhiJeiE0V_mfcp"}


@app.on_event("startup")
async def startup():
    if settings.project.log_file:
        logging_config.dictConfig(LOGGING)


app.include_router(model_server.router, prefix="/api/v1", tags=["ml/dl"])
