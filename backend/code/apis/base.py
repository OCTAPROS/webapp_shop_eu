from fastapi import APIRouter
from apis.v1 import route_products, route_user, route_auth


api_router = APIRouter()

api_router.include_router(route_auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(route_user.router, prefix="/users", tags=["users"])
api_router.include_router(route_products.router, prefix="/products", tags=["products"])
