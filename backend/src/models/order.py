from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric, String, Integer, Date, Index

import sqlalchemy.dialects.oracle as ora
from sqlalchemy.orm import relationship
from datetime import datetime, date
from decimal import Decimal
from typing import List




class Order(SQLModel, table=True):
    __tablename__ = "order_t"

    id: int | None = Field(sa_column=Column(Integer, primary_key=True))
    customer_id: int = Field(sa_column=Column(Integer, nullable=False))
    order_number: str | None = Field(sa_column=Column(String, nullable=True))
    payment_method: str | None = Field(sa_column=Column(String, nullable=True))
    value: Decimal | None = Field(sa_column=Column(Numeric, nullable=True, default=0))
    delivery_method: str | None = Field(sa_column=Column(String, nullable=True))
    order_date: date | None = Field(sa_column=Column(Date))
    delivery_date: date | None = Field(sa_column=Column(Date))
    status: str | None = Field(sa_column=Column(String(100), default="NEW"))
    updated_at: datetime | None = Field(sa_column=Column(DateTime, nullable=True))
    created_at: datetime | None = Field(sa_column=Column(DateTime, default=datetime.now))

    # rows: list["OrderRow"] # = Relationship(back_populates="order_t")
    

class OrderRow(SQLModel, table=True):
    __tablename__ = "order_row_t"
    __table_args__ = (Index("idx_order_product", "order_id", "product_id"),)

    id: int | None = Field(sa_column=Column(Integer, primary_key=True))
    order_id: int = Field(sa_column=Column(Integer, nullable=False))
    product_id: int = Field(sa_column=Column(Integer, nullable=False))
    ordered_count: int = Field(sa_column=Column(Numeric, nullable=False))




# class RolePermissionLink(SQLModel, table=True):
#     role_id: str = Field(foreign_key="role.id", primary_key=True)
#     permission_id: str = Field(foreign_key="permission.id", primary_key=True)

# class Role(SQLModel, table=True):
#     id: int = Field(primary_key=True)
#     name: str = Field(index=True, unique=True)
#     permissions: list["Permission"] = Relationship(
#         back_populates="roles",
#         link_model=RolePermissionLink,
#     )

# class Permission(SQLModel, table=True):
#     id: int = Field(primary_key=True)
#     name: str = Field(index=True, unique=True)
#     roles: list[Role] = Relationship(
#         back_populates="permissions",
#         link_model=RolePermissionLink,
#     )