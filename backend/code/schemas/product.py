from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ProductCreate(BaseModel):
    name: str
    image_uri: str
    description: str
    price: int
    created_at: datetime
    modified_at: Optional[datetime] | None

class ProductShow(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id: int
    image_uri: str
    description: str
    price: int
    created_at: datetime
    modified_at: Optional[datetime] | None

class ProductUpdate(ProductCreate):
    pass