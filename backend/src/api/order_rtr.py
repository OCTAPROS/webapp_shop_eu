from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session, select

from db.db_session import get_dbsession
from models.order import OrderHead, OrderRow
from typing import List

router = APIRouter()

@router.get("/", response_model=List[OrderHead])
def get_all_orders(skip: int = 0, limit = 10, db_session: Session = Depends(get_dbsession)):
    objects = db_session.exec(select(OrderHead).offset(skip).limit(limit)).all()
    if not objects:
        raise HTTPException(detail=f"There are no Orders for selected criteria", status_code=status.HTTP_404_NOT_FOUND)
    return objects

@router.get("/{id}", response_model=OrderHead)
def get_order_by_id(id:int, db_session: Session = Depends(get_dbsession)):
    order = db_session.get(OrderHead, id)
    if not order:
        raise HTTPException(detail=f"Order with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    # product_public = ProductPublic(**product.model_dump())
    # print(product_public)
    return order

@router.post("/", response_model=OrderHead, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderHead, db_session: Session = Depends(get_dbsession)):
    print("###### wdqwdqwdqwdwq")
    db_session.add(order)  
    db_session.commit()
    db_session.refresh(order)
    return order

# @router.put("/{id}", response_model=Order, status_code=status.HTTP_200_OK)
# def update_order(id:int, product_data: Order, db_session: Session = Depends(get_dbsession)):
#     product = db_session.get(Order, id)
#     if not product:
#         raise HTTPException(detail=f"Product with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    
#     for field, value in product_data.model_dump().items():
#         setattr(product, field, value)
#     db_session.commit()
#     db_session.refresh(product)
#     return product

# @router.delete("/{id}", status_code=status.HTTP_200_OK)
# def delete_order(id:int, db_session: Session = Depends(get_dbsession)):
#     product = db_session.get(Order, id)
#     if not product:
#         raise HTTPException(detail=f"Product with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
#     db_session.delete(product)
#     db_session.commit()
#     return product
