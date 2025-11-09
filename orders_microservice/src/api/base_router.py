from fastapi import APIRouter

from src.api.routes.orders_proxy import router as orders_router
from src.api.routes.orders_items_router import router as orders_items_router
from src.api.routes.items_router import router as items_router

base_router = APIRouter(prefix="/api/v1")
base_router.include_router(orders_router)
base_router.include_router(orders_items_router)
base_router.include_router(items_router)