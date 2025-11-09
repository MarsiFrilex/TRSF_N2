from src.services.orders_proxy_service import OrdersProxyService
from src.services.users_proxy_service import UsersProxyService


async def get_users_proxy_service() -> UsersProxyService:
    return UsersProxyService()


async def get_orders_proxy_service() -> OrdersProxyService:
    return OrdersProxyService()