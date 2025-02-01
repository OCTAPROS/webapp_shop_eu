from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session, select

from db.db_session import get_session
from models.product import Product  #, ProductPublic
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Product])
def get_all_products(skip: int = 0, limit = 10, db_session: Session = Depends(get_session)):
    products = db_session.exec(select(Product).offset(skip).limit(limit)).all()
    if not products:
        raise HTTPException(detail=f"There are no products for selected criteria", status_code=status.HTTP_404_NOT_FOUND)
    return products

@router.get("/{id}", response_model=Product)
def get_product_by_id(id:int, db_session: Session = Depends(get_session)):
    product = db_session.get(Product, id)
    if not product:
        raise HTTPException(detail=f"Product with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    return product

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: Product, db_session: Session = Depends(get_session)):
    db_session.add(product)  
    db_session.commit()
    db_session.refresh(product)
    return product

@router.put("/{id}", response_model=Product, status_code=status.HTTP_200_OK)
def update_product(id:int, product_data: Product, db_session: Session = Depends(get_session)):
    product = db_session.get(Product, id)
    if not product:
        raise HTTPException(detail=f"Product with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    
    for field, value in product_data.model_dump().items():
        setattr(product, field, value)
    db_session.commit()
    db_session.refresh(product)
    return product

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_product(id:int, db_session: Session = Depends(get_session)):
    product = db_session.get(Product, id)
    if not product:
        raise HTTPException(detail=f"Product with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    db_session.delete(product)
    db_session.commit()
    return product
