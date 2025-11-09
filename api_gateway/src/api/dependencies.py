from fastapi import Security, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.services.orders_proxy_service import OrdersProxyService
from src.services.users_proxy_service import UsersProxyService

auth_scheme = HTTPBearer()


async def get_users_proxy_service() -> UsersProxyService:
    return UsersProxyService()


async def get_orders_proxy_service() -> OrdersProxyService:
    return OrdersProxyService()


async def current_user_dependency(request: Request, token: HTTPAuthorizationCredentials = Security(auth_scheme)):
    auth_service = await get_users_proxy_service()
    return await auth_service.get_current_user(request.headers, request.cookies)