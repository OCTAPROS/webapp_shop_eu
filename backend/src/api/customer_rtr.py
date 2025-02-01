from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlmodel import Field, Session, SQLModel, create_engine, select
from db.db_session import get_session
from models.customer import Customer


router = APIRouter()

@router.get("", response_model=List[Customer])
def get_all_customers(db_session = Depends(get_session)):
    customers = db_session.exec(select(Customer)).all()
    if not customers:
        raise HTTPException(detail=f"No Customers to retrieve", status_code=status.HTTP_404_NOT_FOUND)
    return customers

@router.get("/{id}", response_model=Customer)
def get_customer_by_id(id:int, db_session: Session = Depends(get_session)):
    customer = db_session.get(Customer, id)
    if not customer:
        raise HTTPException(detail=f"Customer with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    return customer

