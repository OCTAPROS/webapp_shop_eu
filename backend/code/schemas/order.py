from pydantic import BaseModel, model_validator, ConfigDict
from typing import Optional
from datetime import datetime


class OrderCreate(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

class OrderUpdate(OrderCreate):
    pass    

class OrderShow(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    title: str
    slug: str
    content: Optional[str]
    created_at: datetime