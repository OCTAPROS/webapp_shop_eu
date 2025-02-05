from passlib.context import CryptContext
from datetime import timedelta, datetime
import jwt
from core.config import settings
import uuid
import logging


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
        return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def generate_password_hash(password):
        return pwd_context.hash(password)


def create_access_token(user_data: dict, expiry: timedelta = None, refresh: bool = False):
    payload = {}
    payload["user"] = user_data
    expiration_time = datetime.now() + timedelta(seconds=settings.JWT_ACCESS_TOKEN_EXPIRE_SECONDS)
    payload["exp"] = int(expiration_time.timestamp())
    payload["jti"] = str(uuid.uuid4())
    payload["refresh"] = refresh

    token = jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return token

def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token,
            key=settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return token_data
    
    except jwt.PyJWTError as e:
        logging.exception(e)
        return None
    
