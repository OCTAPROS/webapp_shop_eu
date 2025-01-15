from fastapi import APIRouter
from api import auth, customer, product


api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(customer.router, prefix="/customers", tags=["Customers"])
api_router.include_router(product.router, prefix="/products", tags=["Products"])
