from fastapi import APIRouter

from routers.catalog import catalog_router
from routers.user import user_router

api_router = APIRouter()

api_router.include_router(catalog_router)
api_router.include_router(user_router)
