from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas.product import ProductCreate, ProductShow, ProductUpdate
from db.session import get_db
from db.models.user import User
from apis.v1.route_login import get_current_user
from db.repository.product import create_new_product, list_products, update_product_by_id, delete_product_by_id
from typing import List

router = APIRouter()

@router.post("/", response_model=ProductShow, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product = None #create_new_product(product=product, db=db)
    return product

@router.get("/{id}", response_model=ProductShow)
def get_product_by_id(id:int, db: Session = Depends(get_db)):
    product = retrieve_product(id=id, db=db)
    if not product:
        raise HTTPException(detail=f"product with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    return product

@router.get("/", response_model=List[ProductShow])
def get_all_products(db: Session = Depends(get_db)):
    products = list_products(db=db)
    if not products:
        raise HTTPException(detail=f"No products to retrieve", status_code=status.HTTP_404_NOT_FOUND)
    return products

@router.put("/{id}", response_model=ProductShow)
def update_product(id:int, product: ProductUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    product = update_product_by_id(id=id, product=product, db=db, author_id=current_user.id)
    if isinstance(product, dict):
        raise HTTPException(
            detail=product.get("error"),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return product

@router.delete("/{id}")
def delete_product(id:int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    message = delete_product_by_id(id=id, db=db, author_id=current_user.id)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST)
    return message.get("msg")
