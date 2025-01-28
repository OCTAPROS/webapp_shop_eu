from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric
import sqlalchemy.dialects.oracle as ora
from sqlalchemy.orm import relationship
import uuid
from datetime import date, datetime
from typing import List, Optional
import oracledb


# class Customer(SQLModel, table=True):
#     __tablename__ = "KLIENT"
#     id: Optional[int] = Field(primary_key=True, index=True)
#     name: str = Field(sa_column=Column("imie", String))
#     last_name: str = Field(sa_column=Column("nazwisko", String))


class Customer(SQLModel, table=True):
    __tablename__ = "customer"
    id: int | None = Field(sa_column=Column(ora.NUMBER(38,0), Identity(start=1), primary_key=True))
    name: str = Field(sa_column=Column(ora.NVARCHAR2(100)))
    last_name: str = Field(sa_column=Column(ora.NVARCHAR2(100)))