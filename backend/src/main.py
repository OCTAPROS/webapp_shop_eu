from fastapi import FastAPI
from core.config import settings
from api._base import api_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "https://localhost:80"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
