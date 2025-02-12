from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric, String, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from decimal import Decimal



class Product(SQLModel, table=True):
    __tablename__ = "product_t"

    # id: int | None = Field(sa_column=Column(Integer, primary_key=True))
    # brand: str = Field(sa_column=Column(String(20), nullable=False))
    # type: int =Field(sa_column=Column(String), nullable=False)
    # price: Decimal = Field(sa_column=Column(Numeric, nullable=False, default=0))  
    # name: str = Field(sa_column=Column(String(150)))
    # ean: str = Field(sa_column=Column(String(13), nullable=False))
    # updated_at: datetime | None = Field(sa_column=Column(DateTime, nullable=True))
    # created_at: datetime = Field(sa_column=Column(DateTime, default=datetime.now))    

    id: int | None = Field(Integer, primary_key=True)
    brand: str = Field(String(20), nullable=False)
    product_type_fk: int =Field(String, nullable=False)
    price: float = Field(Numeric, nullable=False)
    name: str = Field(String(150))
    ean: str = Field(String(13), nullable=False)
    
class ProductView(SQLModel, table=True):
    __tablename__ = "products_v"

    # id: int | None = Field(sa_column=Column(Integer, primary_key=True))
    # brand: str = Field(sa_column=Column(String(20), nullable=False))
    # type: int =Field(sa_column=Column(String), nullable=False)
    # price: Decimal = Field(sa_column=Column(Numeric, nullable=False, default=0))  
    # name: str = Field(sa_column=Column(String(150)))
    # ean: str = Field(sa_column=Column(String(13), nullable=False))
    # updated_at: datetime | None = Field(sa_column=Column(DateTime, nullable=True))
    # created_at: datetime = Field(sa_column=Column(DateTime, default=datetime.now))    

    id: int = Field(Integer, primary_key=True)
    brand_id: int 
    brand: str     
    price: float 
    name: str 
    ean: str 
    product_type_id: int
    product_type: str