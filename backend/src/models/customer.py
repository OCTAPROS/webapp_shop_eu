from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric, String, Integer
import sqlalchemy.dialects.oracle as ora
from sqlalchemy.orm import relationship
from datetime import date, datetime
from typing import List
from decimal import Decimal

class Customer(SQLModel, table=True):
    __tablename__ = "customer_t"
    id: int | None = Field(sa_column=Column(Integer, primary_key=True))
    first_name: str = Field(sa_column=Column(String(150), nullable=False))
    last_name: str = Field(sa_column=Column(String(150), nullable=False))
    email: str = Field(sa_column=Column(String(50), nullable=False))
    phone_number: str = Field(sa_column=Column(String(9), nullable=False))
    city_id: int = Field(sa_column=Column(Integer, ForeignKey("city_t.id"), nullable=False))
    postal_code: str = Field(sa_column=Column(String(15), nullable=False))
    street: str = Field(sa_column=Column(String(50), nullable=False))
    nip: str = Field(sa_column=Column(String(20), nullable=False))
    company_name: str = Field(sa_column=Column(String(20), nullable=False))

    city: "City" = Relationship(back_populates="customers")
 

class City(SQLModel, table=True):
    __tablename__ = "city_t"
    id: int | None = Field(sa_column=Column(Integer, primary_key=True))
    city: str = Field(sa_column=Column(String(100), nullable=False))

    customers: List[Customer] = Relationship(back_populates="city")