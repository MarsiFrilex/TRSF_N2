from src.services.users_proxy_service import UsersProxyService


async def get_users_proxy_service() -> UsersProxyService:
    return UsersProxyService()