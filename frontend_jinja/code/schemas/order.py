from pydantic import BaseModel, model_validator, ConfigDict
from typing import Optional
from datetime import datetime


class OrderCreate(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @model_validator(mode="before")
    def generate_slug(cls, values):
        if 'title' in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values

class OrderUpdate(OrderCreate):
    pass    

class OrderShow(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    title: str
    slug: str
    content: Optional[str]
    created_at: datetime