from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric, String, Integer, Date, Index

import sqlalchemy.dialects.oracle as ora
from sqlalchemy.orm import relationship
from datetime import datetime, date
from decimal import Decimal
from typing import List


# class OrderRowInsertModel(SQLModel):
#     product_id: int = Field(Integer, nullable=False)
#     quantity: int = Field(Integer, nullable=False)

# class OrderInsertModel(SQLModel):
#     order_rows: list[OrderRowInsertModel]

#     customer_id: int = Field(Integer, nullable=False)
#     order_number: str | None = Field(String, nullable=True)
#     # # payment_method: str | None = Field(String, nullable=True)
#     # # delivery_method: int | None = Field(Integer, nullable=True)
#     # # order_date: date | None = Field(Date)
#     # # delivery_date: date | None = Field(Date)
#     status: str | None = Field(String(100))

#     # order_rows = List[OrderRowInsertModel]

class OrderRowInsert(SQLModel):
    # order_id: int = Field(sa_column=Column(Integer, ForeignKey("order_t.id"), nullable=False, primary_key=True))
    # product_id: int = Field(sa_column=Column(Integer, ForeignKey("product_t.id"), nullable=False, primary_key=True))
    # quantity: int = Field(sa_column=Column(Integer, nullable=False))

    # order_id: int = Field(Integer, foreign_key="order_t.id", nullable=False, primary_key=True)
    product_id: int #= Field(Integer, nullable=False)
    quantity: int #= Field(Integer, nullable=False)


class OrderInsert(SQLModel):
    # customer_id: int = Field(Integer, nullable=False, foreign_key="customer_t.id")
    # order_number: str | None = Field(String, nullable=True)
    # payment_method: str | None = Field(sa_column=Column(String, nullable=True))
    # delivery_method: int | None = Field(sa_column=Column(Integer, nullable=True))
    # order_date: date | None = Field(sa_column=Column(Date))
    # delivery_date: date | None = Field(sa_column=Column(Date))
    # status: str | None = Field(sa_column=Column(String(100), default="NEW"))
    # updated_at: datetime | None = Field(sa_column=Column(DateTime, nullable=True))
    # created_at: datetime | None = Field(sa_column=Column(DateTime, default=datetime.now))

    customer_id: int #= Field(Integer, nullable=False)
    order_number: str | None #= Field(String, nullable=True)
    payment_method: str | None #= Field(String, nullable=True)
    delivery_method: int | None #= Field(Integer, nullable=True)
    order_date: date | None #= Field(sa_column=Column(Date), nullable=True)
    delivery_date: date | None #= Field(sa_column=Column(Date), nullable=True)
    status: str | None #= Field(String(100), nullable=True)

    # order_rows: List[OrderRowInsert] 


class Order(OrderInsert, table=True):
    __tablename__ = "order_t"

    id: int | None = Field(sa_column=Column(Integer, primary_key=True))
    # order_rows: list["OrderRow"] = Relationship(back_populates="order")






class OrderRow(OrderRowInsert, table=True):
    __tablename__ = "order_row_t"
    order_id: int = Field(sa_column=Column(Integer, ForeignKey("order_t.id"), nullable=False, primary_key=True))
    product_id: int = Field(sa_column=Column(Integer, ForeignKey("product_t.id"), nullable=False, primary_key=True))
    quantity: int = Field(sa_column=Column(Integer, nullable=False))
    # order: Order = Relationship(back_populates="order_rows")
