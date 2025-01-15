from sqlmodel import SQLModel, create_engine, Session, Field, Column, Integer, String
from typing import Optional
from decimal import Decimal


class UserBase(SQLModel):
    email: str
    password: str
    is_superuser: bool
    is_active: bool

class User(UserBase, table=True):
    __tablename__ = "USER"
    id: Optional[int] = Field(primary_key=True, index=True)

