from sqlmodel import SQLModel, create_engine, Session, Field, Column, Integer, String
from typing import Optional
from decimal import Decimal


class Customer(SQLModel, table=True):
    __tablename__ = "KLIENT"
    id: Optional[int] = Field(primary_key=True, index=True)
    name: str = Field(sa_column=Column("imie", String))
    last_name: str = Field(sa_column=Column("nazwisko", String))