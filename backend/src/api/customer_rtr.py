from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlmodel import Field, Session, SQLModel, create_engine, select
from db.db_session import get_session
from models.customer import Customer
from auth.dependencies import AccessTokenBearer, decode_token 
from auth.dependencies import get_current_user
from models.user import User, UserLoginModel, UserPublicModel

router = APIRouter()

@router.get("", response_model=List[Customer])
def get_all_customers(
        db_session = Depends(get_session), 
        current_user: User = Depends(get_current_user)
    ):
    objs = db_session.exec(select(Customer)).all()
    if not objs:
        raise HTTPException(detail=f"No Customers to retrieve", status_code=status.HTTP_404_NOT_FOUND)
    return objs

@router.get("/{id}", response_model=Customer)
def get_customer_by_id(id:int, 
                       db_session: Session = Depends(get_session),
                       current_user: User = Depends(get_current_user)
                       ):
    obj = db_session.get(Customer, id)
    if not obj:
        raise HTTPException(detail=f"Customer with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    return obj
