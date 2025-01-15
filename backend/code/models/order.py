from sqlmodel import SQLModel, create_engine, Session, Field, Column, Integer, String
from typing import Optional
from decimal import Decimal



class Order(SQLModel, table=True):
    __tablename__ = "ZAMOWIENIE"
    id: Optional[int] = Field(primary_key=True, index=True)
    imie: str
    nazwisko: str
