from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from web_app.base import app_router


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )
    app.include_router(app_router)
    app.mount("/static", StaticFiles(directory="web_app/static"), name="static")
    return app

app = start_application()
