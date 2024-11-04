import json
from fastapi import APIRouter, Request, Depends, responses, status, Form
from fastapi.templating import Jinja2Templates

from schemas.user import UserCreate
from pydantic import ValidationError


templates = Jinja2Templates(directory="webfrontend/templates")
router = APIRouter()

@router.get("/register")
def register_user(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})

# @router.post("/register")
# def register(request: Request, email: str = Form(...), password: str= Form(...), db: Session = Depends(get_db)):
#     errors = []
#     try:
#         user = UserCreate(email=email, password=password)
#         create_new_user(user=user, db=db)
#         return responses.RedirectResponse("/?alert=Successfully%20Registered", status_code=status.HTTP_302_FOUND)
    
#     except ValidationError as e:
#         errors_list = json.loads(e.json())
#         for item in errors_list:
#             errors.append(item.get("loc")[0]+ ": " + item.get("msg"))
#         return templates.TemplateResponse("auth/register.html", {"request": request, "errors": errors})
    
@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


# @router.post("/login")
# def login(request: Request,
#     email: str = Form(...),
#     password: str = Form(...),
#     db: Session = Depends(get_db)
# ):
#     errors = []
#     user = authenticate_user(email=email,password=password,db=db)
#     if not user:
#         errors.append("Incorrect email or password")
#         return templates.TemplateResponse("auth/login.html", {"request": request,"errors":errors})
#     access_token = create_access_token(data={"sub": email})
#     response = responses.RedirectResponse(
#             "/?alert=Successfully Logged In", status_code=status.HTTP_302_FOUND
#         )
#     response.set_cookie(key="access_token",value=f"Bearer {access_token}",httponly=True)
#     return response