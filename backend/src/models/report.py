from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric, String, Integer
import sqlalchemy.dialects.oracle as ora
from sqlalchemy.orm import relationship
import uuid
from datetime import date, datetime
from typing import List, Optional
# from models.customer import Customer


class Report1(SQLModel, table=True):
    __tablename__ = "report1_v"

    id: int =  Field(primary_key=True)
    customer_id: int 
    order_number: str | None  
    payment_method: str | None 
    status: str | None  
    order_value: float | None

