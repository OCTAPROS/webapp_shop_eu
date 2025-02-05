from fastapi import APIRouter
from api import auth_rtr, customer_rtr, order_rtr, product_rtr, dicts_rtr


api_router = APIRouter()

api_router.include_router(auth_rtr.router, prefix="/auth", tags=["Auth"])
api_router.include_router(customer_rtr.router, prefix="/customers", tags=["Customers"])
api_router.include_router(product_rtr.router, prefix="/products", tags=["Products"])
api_router.include_router(order_rtr.router, prefix="/orders", tags=["Orders"])
api_router.include_router(dicts_rtr.router, prefix="/dicts", tags=["Dictionaries"])
