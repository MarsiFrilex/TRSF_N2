from fastapi import APIRouter

from src.api.routes.orders_proxy.orders_router import router as orders_router
from src.api.routes.orders_proxy.orders_items_router import router as orders_items_router
from src.api.routes.orders_proxy.items_router import router as items_router

orders_proxy_router = APIRouter()

orders_proxy_router.include_router(orders_router)
orders_proxy_router.include_router(orders_items_router)
orders_proxy_router.include_router(items_router)