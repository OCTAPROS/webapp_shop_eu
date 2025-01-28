from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric
import sqlalchemy.dialects.oracle as ora
from sqlalchemy.orm import relationship
import uuid
from datetime import date, datetime
from typing import List, Optional
import oracledb



class User(SQLModel, table=True):
    __tablename__ = "user"
    id: int | None = Field(sa_column=Column(ora.NUMBER(38,0), Identity(start=1), primary_key=True))
    email: str = Field(sa_column=Column(ora.NVARCHAR2(100), nullable=True))
    password: str = Field(sa_column=Column(ora.NVARCHAR2(100), nullable=True))
    is_superuser: bool = Field(sa_column=Column(ora.NUMBER(1,0), default=0))
    is_active: bool = Field(sa_column=Column(ora.NUMBER(1,0), default=0))

class UserLogin(SQLModel):
    username: str
    password: str