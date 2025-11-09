from fastapi import APIRouter
from src.api.routes.auth_router import router as auth_router

from src.api.routes.users_router import router as users_router

base_router = APIRouter(prefix="/api/v1")
base_router.include_router(auth_router)
base_router.include_router(users_router)