from webfrontend.v1 import route_blog, route_auth
from fastapi import APIRouter


app_router = APIRouter()
app_router.include_router(route_blog.router, prefix="", tags=[""], include_in_schema=False)
app_router.include_router(route_auth.router, prefix="/auth", tags=[""], include_in_schema=False)


