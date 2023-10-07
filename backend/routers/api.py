from fastapi import APIRouter

from routers.catalog import catalog_router

api_router = APIRouter(prefix='/api/v1')
api_router.include_router(catalog_router)