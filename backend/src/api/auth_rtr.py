from fastapi import APIRouter, Depends, status, HTTPException
from db.db_session import get_session
from models.user import User, UserLoginModel, UserPublicModel
from core.config import settings
from typing import List
from auth.utils import verify_password, create_access_token
from datetime import timedelta
from sqlmodel import Session, select
from fastapi.responses import JSONResponse
from auth.dependencies import get_current_user

router = APIRouter()


@router.post("/token")
def login_user(login_data: UserLoginModel, db_session: Session = Depends(get_session), status_code=status.HTTP_200_OK):
    user: User = db_session.exec(select(User).where(User.email == login_data.username)).one_or_none()
    if user:
        password_valid = verify_password(login_data.password, user.password_hash)

        if password_valid:
            access_token = create_access_token(
                user_data={
                    "email": user.email,
                    "user_id": user.id,
                    "customer_id": user.customer_id
                }
            )

            return JSONResponse(
                content={
                    "message": "Login successful",
                    "access_token": access_token,
                    # "refresh_token": refresh_token,
                    "user": {
                        "email": user.email,
                        "user_id": user.id,
                        "customer_id": user.customer_id
                    }
                }
            )
        
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid email or password"
    ) 
        

@router.get("/me", response_model=UserPublicModel)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/users", response_model=List[UserPublicModel])
def get_all_users(skip: int = 0, limit = 10, db_session: Session = Depends(get_session)):
    objects = db_session.exec(select(User).offset(skip).limit(limit)).all()
    if not objects:
        raise HTTPException(detail=f"There are no users for selected criteria", status_code=status.HTTP_404_NOT_FOUND)
    return objects