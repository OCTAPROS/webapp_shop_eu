from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric, String, Integer
import sqlalchemy.dialects.oracle as ora
from sqlalchemy.orm import relationship
import uuid
from datetime import date, datetime
from typing import List, Optional
# from models.customer import Customer


class User(SQLModel, table=True):
    __tablename__ = "user_t"

    id: int | None = Field(sa_column=Column(Integer, primary_key=True))
    email: str = Field(sa_column=Column(String, nullable=True))
    password_hash: str = Field(sa_column=Column(String, nullable=True))
    is_superuser: bool = Field(sa_column=Column(ora.NUMBER(1,0), default=0))
    is_active: bool = Field(sa_column=Column(ora.NUMBER(1,0), default=0))
    customer_id: int | None = Field(sa_column=Column(Integer, ForeignKey("customer_t.id"), nullable=True))

    # as_customer: Customer = Relationship(back_populates="as_user")


# class Role(SQLModel, table=True):
#     __tablename__ = "user_t"

#     id: int | None = Field(sa_column=Column(Integer, primary_key=True))
#     email: str = Field(sa_column=Column(String, nullable=True))
#     password: str = Field(sa_column=Column(String, nullable=True))
#     is_superuser: bool = Field(sa_column=Column(ora.NUMBER(1,0), default=0))
#     is_active: bool = Field(sa_column=Column(ora.NUMBER(1,0), default=0))


class UserPublicModel(SQLModel):
    id: int | None #= Field(sa_column=Column(Integer, primary_key=True))
    email: str #= Field(sa_column=Column(String, nullable=True))
    is_superuser: bool #= Field(sa_column=Column(ora.NUMBER(1,0), default=0))
    is_active: bool #= Field(sa_column=Column(ora.NUMBER(1,0), default=0))
    customer_id: int | None #= Field(sa_column=Column(Integer, ForeignKey("customer_t.id"), nullable=True))

class UserLoginModel(SQLModel):
    username: str
    password: str