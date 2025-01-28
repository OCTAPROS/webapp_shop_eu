from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric
import sqlalchemy.dialects.oracle as ora
from sqlalchemy.orm import relationship
import uuid
from datetime import date, datetime
from typing import List, Optional
import oracledb

# class OrderRow(SQLModel, table=True):
#     __tablename__ = "ZAMOWIENIE_WIERSZ"
#     order_id: int = Field(sa_column=Column("zamowienie_id", Integer, primary_key=True))
#     product_id: int = Field(sa_column=Column("produkt_id", Integer))
#     amount: int = Field(sa_column=Column("ilosc", Integer))


# class Order(SQLModel, table=True):
#     __tablename__ = "ZAMOWIENIE"
#     id: Optional[int] = Field(primary_key=True, index=True)

#     customer_id: str = Field(sa_column=Column("klient_id", String))
#     order_number: str = Field(sa_column=Column("nr_zamowienia", String))
#     payment_method: str = Field(sa_column=Column("formaplatnosci", String))
#     value: str = Field(sa_column=Column("wartosc", Numeric))
#     delivery_method: str = Field(sa_column=Column("formaodbioru", Numeric))
#     order_date: DateTime = Field(sa_column=Column("data_zlozenia", DateTime))
#     dispatch_date: DateTime = Field(sa_column=Column("data_wyslania", DateTime))
#     status: str = Field(sa_column=Column("status", String))
#     payment_method: str = Field(sa_column=Column("formaplatnosci", String))

#     # order_rows: list[OrderRow] = Relationship(back_populates="order")


class OrderHead(SQLModel, table=True):
    __tablename__ = "order_head"
    id: int | None = Field(sa_column=Column(ora.NUMBER(38,0), Identity(start=1), primary_key=True))
    value: float | None = Field(sa_column=Column(ora.NUMBER(10,2), nullable=True, default=0))
    customer_id: float | None = Field(sa_column=Column(ora.NUMBER(36,0), nullable=True, default=0))
    order_number: str | None = Field(sa_column=Column(ora.NVARCHAR2(100)))
    payment_method: str | None = Field(sa_column=Column(ora.NVARCHAR2(100)))
    value: float | None = Field(sa_column=Column(ora.NUMBER(10,2), nullable=True, default=0))
    # delivery_method: str = Field(sa_column=Column("formaodbioru", Numeric))
    # order_date: DateTime = Field(sa_column=Column("data_zlozenia", DateTime))
    # dispatch_date: DateTime = Field(sa_column=Column("data_wyslania", DateTime))
    status: str | None = Field(sa_column=Column(ora.NVARCHAR2(100)))
    payment_method: str | None = Field(sa_column=Column(ora.NVARCHAR2(100)))
    # updated_at: datetime | None = Field(sa_column=Column(ora.TIMESTAMP, nullable=True))
    # created_at: datetime | None = Field(sa_column=Column(ora.TIMESTAMP, default=datetime.now))
    # on_stock: int = Field(sa_column=Column(ora.NUMBER(10,0), nullable=False, default=0))
    # rows: List["OrderRow"] = Relationship(back_populates="order_head")
    

class OrderRow(SQLModel, table=True):
    __tablename__ = "order_row"
    order_row_id: int | None = Field(sa_column=Column(ora.NUMBER(38,0), Identity(start=1), primary_key=True))
    # order_id: int = Field(sa_column=Column(ora.NUMBER(38,0), nullable=False, index=True))  #foreign_key="order_head.id"
    order_id: int = Field(foreign_key="order_head.id", nullable=False)
    # order: OrderHead = relationship(OrderHead)
    product_id: int = Field(sa_column=Column(ora.NUMBER(38,0), nullable=False, index=True))
    ordered_count: int = Field(sa_column=Column(ora.NUMBER(10,0), nullable=False, default=0))

    # order_head: OrderHead = Relationship(back_populates="rows")


