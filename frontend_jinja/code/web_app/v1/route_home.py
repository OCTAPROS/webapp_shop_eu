from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from typing import Optional


templates = Jinja2Templates(directory="web_app/templates")
router = APIRouter()

@router.get("/")
def home(request: Request, alert: Optional[str] = None):
    return templates.TemplateResponse("webstore/home.html", {"request": request, "alert": alert})