from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from models.user import User
from sqlmodel import Session, select

from db.db_session import get_session
from models.user import User, UserLogin
from core.security import create_access_token, Hasher
from core.config import settings


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


@router.post("/token", status_code=status.HTTP_200_OK)
def login_for_access_token(user_login_data: UserLogin , db_session: Session = Depends(get_session)):
    user: User = authenticate_user(user_email=user_login_data.username, password=user_login_data.password, db_session=db_session)
    if not user:
        raise HTTPException(
            detail=f"Incorrect email or password",
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


def authenticate_user(user_email: str, password: str, db_session: Session = Depends(get_session)):
    user: User = db_session.exec(select(User).where(User.email == user_email)).one_or_none()
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user


def get_current_user(token: str = Depends(oauth2_scheme), db_session: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials. Try to login again"
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user: User = db_session.exec(select(User).where(User.email == email)).first()
    if user is None:
        raise credentials_exception
    return user
        

@router.get("/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)], ):
    return current_user