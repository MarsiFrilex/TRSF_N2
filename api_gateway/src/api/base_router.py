from fastapi import APIRouter

from src.api.routes.users_router import users_proxy_router
from src.api.routes.orders_proxy import orders_proxy_router

base_router = APIRouter(prefix="/api/v1")

base_router.include_router(users_proxy_router)
base_router.include_router(orders_proxy_router)