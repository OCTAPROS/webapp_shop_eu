from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.base import api_router
from webfrontend.base import app_router


def include_router(app):
    app.include_router(api_router)
    app.include_router(app_router)

def configure_staticfiles(app):
    app.mount("/static", StaticFiles(directory="webfrontend/static"), name="static")

def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )
    include_router(app)
    configure_staticfiles(app)
    return app

app = start_application()
