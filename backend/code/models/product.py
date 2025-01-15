from sqlmodel import SQLModel, create_engine, Session, Field, Column, Integer, String
from typing import Optional
from decimal import Decimal



class ProductBase(SQLModel):
    marka: str = Field(sa_column=Column("marka", String))
    typ: int = Field(sa_column=Column("typ", Integer))
    price: int = Field(sa_column=Column("cena", Integer))  # Decimal = Field(default=0, max_digits=10, decimal_places=2)
    name: str = Field(sa_column=Column("nazwa", String))
    ean: str
    stock_count: int = Field(sa_column=Column("ilosc_magazyn", String))

class Product(ProductBase, table=True):
    __tablename__ = "PRODUKT"
    id: Optional[int] = Field(primary_key=True, index=True)

  