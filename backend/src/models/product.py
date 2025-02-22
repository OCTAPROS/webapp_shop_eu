from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric, String, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from decimal import Decimal



class Product(SQLModel, table=True):
    __tablename__ = "product_t"

    id: int | None = Field(Integer, primary_key=True)
    brand_id: str = Field(String(20), nullable=False)
    product_type_id: int =Field(String, nullable=False)
    price: float = Field(Numeric, nullable=False)
    name: str = Field(String(150))
    ean: str | None = Field(String(13), nullable=False)
    description: str | None = Field(String(1000), nullable=False)

class ProductInsert(SQLModel):
    id: int | None
    name: str
    brand_id: int 
    product_type_id: int    
    price: float 
    ean: str
    qty_on_stock: int
    description: str

class ProductUpdate(ProductInsert):
    pass
    
class ProductView(SQLModel, table=True):
    __tablename__ = "products_v"

    id: int = Field(Integer, primary_key=True)
    brand_id: int 
    brand: str
    price: float 
    name: str 
    ean: str 
    product_type_id: int
    product_type: str
    qty_on_stock: int | None