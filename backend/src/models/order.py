from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric, String, Integer, Date, Index

import sqlalchemy.dialects.oracle as ora
from sqlalchemy.orm import relationship
from datetime import datetime, date
from decimal import Decimal
from typing import List, Optional
from pydantic import field_validator



class OrderRow(SQLModel, table=True):
    __tablename__ = "order_row_t"

    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order_t.id")  # Foreign key linking to Order
    product_id: int 
    quantity: int 

    order: "Order" = Relationship(back_populates="order_rows")  # Relationship to Order


class Order(SQLModel, table=True):
    __tablename__ = "order_t"

    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int   
    payment_method_id: int 
    delivery_method_id: int 

    order_rows: List[OrderRow] = Relationship(back_populates="order")  


class OrderRowInsert(SQLModel):  # ✅ Input model for individual order rows
    product_id: int
    quantity: int


class OrderInsert(SQLModel):  # ✅ Input model for order creation
    customer_id: int
    payment_method_id: int
    delivery_method_id: int
    order_rows: List[OrderRowInsert] = Field(default_factory=list)

class OrderAdminView(SQLModel, table=True):
    __tablename__ = "orders_admin_v"

    id: int = Field(default=None, primary_key=True)
    customer_id: int   
    first_name: str 
    last_name: str 
    phone_number: str 
    street: str 
    city: str 
    order_number: str 
    payment_method_id: int
    payment_method: str 
    delivery_method_id: int
    delivery_method: str 
    status_id: int
    order_status: str
    order_value: float