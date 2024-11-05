from pydantic import BaseModel, EmailStr, Field, ConfigDict


class ProductCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)

class ProductShow(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id: int
    email: EmailStr
    is_active: bool

class ProductUpdate(ProductCreate):
    pass