from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)

class UserShow(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id: int
    email: EmailStr
    is_active: bool

    # class Config():
    #     from_attributes = True