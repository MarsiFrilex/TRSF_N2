from fastapi import APIRouter

from src.api.routes.users_router.auth_router import router as auth_router
from src.api.routes.users_router.users_router import router as users_router

users_proxy_router = APIRouter()

users_proxy_router.include_router(auth_router)
users_proxy_router.include_router(users_router)