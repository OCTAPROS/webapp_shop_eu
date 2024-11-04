from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from typing import Optional


templates = Jinja2Templates(directory="webfrontend/templates")
router = APIRouter()

@router.get("/")
def home(request: Request, alert: Optional[str] = None):
    a = dir(request)
    for x in a:
        print(request.get(x))
    return templates.TemplateResponse("blogs/home.html", {"request": request, "alert": alert})