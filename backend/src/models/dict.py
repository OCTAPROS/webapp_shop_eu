from sqlmodel import Field, SQLModel, create_engine, Column, Sequence, Identity, Relationship, ForeignKey, Field, DateTime, Numeric, String, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from decimal import Decimal



class DictRow(SQLModel, table=True):
    __tablename__ = "dicts_t"

    id: int | None = Field(Integer, primary_key=True)
    dict_name: str = Field(String(20), nullable=False)
    dict_key: str = Field(String(20), nullable=False)
    dict_value: str = Field(String(50), nullable=False)
    

class DictRowPublic(SQLModel):

    id: int | None = Field(Integer, primary_key=True)
    # dict_name: str = Field(String(20), nullable=False)
    dict_key: str = Field(String(20), nullable=False)
    dict_value: str = Field(String(50), nullable=False)