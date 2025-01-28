from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric
import sqlalchemy.dialects.oracle as ora
from sqlalchemy.orm import relationship
import uuid
from datetime import date, datetime
from typing import List, Optional
import oracledb



# class ProductBase(SQLModel):
#     marka: str = Field(sa_column=Column("marka", String))
#     typ: int = Field(sa_column=Column("typ", Integer))
#     price: int = Field(sa_column=Column("cena", Integer))  # Decimal = Field(default=0, max_digits=10, decimal_places=2)
#     name: str = Field(sa_column=Column("nazwa", String))
#     ean: str
#     stock_count: int = Field(sa_column=Column("ilosc_magazyn", String))

# class Product(ProductBase, table=True):
#     __tablename__ = "PRODUKT"
#     id: Optional[int] = Field(primary_key=True, index=True)

class ProductBase(SQLModel):
    name: str = Field(sa_column=Column(ora.NVARCHAR2(100)))
    brand: str = Field(sa_column=Column(ora.NVARCHAR2(100), nullable=True))
    ean: str | None = Field(sa_column=Column(ora.NVARCHAR2(50), nullable=True))
    price: float = Field(sa_column=Column(ora.NUMBER(10,2), nullable=False, default=0))
    updated_at: datetime | None = Field(sa_column=Column(ora.TIMESTAMP, nullable=True))
    created_at: datetime = Field(sa_column=Column(ora.TIMESTAMP, default=datetime.now))

class Product(ProductBase, table=True):
    __tablename__ = "product"
    id: int | None = Field(sa_column=Column(ora.NUMBER(38,0), Identity(start=1), primary_key=True))
    
    