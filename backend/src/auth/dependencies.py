from typing import Any, List

from fastapi import Depends, Request, status
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

from db.db_session import get_session
from models.user import User
from auth.utils import decode_token
from sqlmodel import Session, select


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)
        token = creds.credentials
        token_data = decode_token(token)
        if not self.token_valid:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="Invalid or expired token"
            )
    
        self.verify_token_data(token_data)

        return token_data

    
    def token_valid(self, token: str) -> bool:
        token_data = decode_token(token)
        return True if token_data is not None else False

    def verify_token_data(self, token_data):
        raise NotImplementedError("Please Override this method in child classes")
    

class AccessTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and token_data["refresh"]:
            raise HTTPException(
            detail=f"Please provide an access token",
            status_code=status.HTTP_403_FORBIDDEN
        )


class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and not token_data["refresh"]:
            raise HTTPException(
            detail=f"Please provide a refresh token",
            status_code=status.HTTP_403_FORBIDDEN
        )

def get_current_user(
        token_details: dict = Depends(AccessTokenBearer()), 
        db_session: Session = Depends(get_session)
        ):
    user_email = token_details["user"]["email"]
    user = db_session.exec(select(User).where(User.email == user_email)).one_or_none()
    if user: 
        return user
    else:
        raise Exception("user not found")
    
class RoleChecker():
    pass