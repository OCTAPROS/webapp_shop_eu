from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session, select

from db.db_session import get_session
from models.order import Order, OrderRow, OrderInsert, OrderRowInsert, OrderAdminView
from typing import List
from auth.dependencies import get_current_user
from models.user import User

router = APIRouter()

@router.get("/", response_model=List[OrderAdminView])
def get_all_orders(skip: int = 0, limit = 10, db_session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    objects = db_session.exec(select(OrderAdminView).offset(skip).limit(limit)).all()
    if not objects:
        raise HTTPException(detail=f"There are no Orders for selected criteria", status_code=status.HTTP_404_NOT_FOUND)
    return objects

# @router.get("/{id}", response_model=Order)
# def get_order_by_id(id:int, db_session: Session = Depends(get_session)):
#     order = db_session.get(Order, id)
#     if not order:
#         raise HTTPException(detail=f"Order with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
#     for r in order.order_rows:
#         print(r)
#     # print(order.order_rows.__dict__)
#     return order

@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(order_data: OrderInsert, 
                 db_session: Session = Depends(get_session),
                 current_user: User = Depends(get_current_user)
                 ):
    print("##############################")
    print(order_data.__dict__)
    print("##############################")
    order: Order = Order(**order_data.model_dump())

    db_session.add(order)  
    db_session.commit()
    db_session.refresh(order)

    print("##############################2")
    print(order.__dict__)
    print("##############################2")

    return order

# @router.put("/{id}", response_model=Order, status_code=status.HTTP_200_OK)
# def update_order(id:int, product_data: Order, db_session: Session = Depends(get_session)):
#     product = db_session.get(Order, id)
#     if not product:
#         raise HTTPException(detail=f"Product with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    
#     for field, value in product_data.model_dump().items():
#         setattr(product, field, value)
#     db_session.commit()
#     db_session.refresh(product)
#     return product

# @router.delete("/{id}", status_code=status.HTTP_200_OK)
# def delete_order(id:int, db_session: Session = Depends(get_session)):
#     product = db_session.get(Order, id)
#     if not product:
#         raise HTTPException(detail=f"Product with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
#     db_session.delete(product)
#     db_session.commit()
#     return product
