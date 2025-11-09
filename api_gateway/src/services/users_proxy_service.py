from starlette.datastructures import Headers

from src.http_client.http_client import HTTPClient
from src.schemas.users_schemas import *


class UsersProxyService:
    def __init__(self):
        self.api_client = HTTPClient("http://users_microservice:8000")

    # Auth endpoints
    async def register_user(self, user: CreateUserSchema, headers: Headers, cookies: dict):
        return await self.api_client.post(f"/api/v1/auth/register-user", json_payload=user, headers=headers, cookies=cookies)

    async def login_user(self, user: LoginUserSchema, headers: Headers, cookies: dict):
        return await self.api_client.post(f"/api/v1/auth/login-user", json_payload=user, headers=headers, cookies=cookies)

    async def refresh_token(self, token: RefreshTokenSchema, headers: Headers, cookies: dict):
        return await self.api_client.post(f"/api/v1/auth/refresh-token", json_payload=token, headers=headers, cookies=cookies)

    async def get_current_user(self, headers: Headers, cookies: dict):
        return await self.api_client.get(f"/api/v1/auth/current-user", headers=headers, cookies=cookies)

    # Users endpoints
    async def get_users_list(self, headers: Headers, cookies: dict):
        return await self.api_client.get(f"/api/v1/users", headers=headers, cookies=cookies)

    async def get_concrete_user(self, user_id: int, headers: Headers, cookies: dict):
        return await self.api_client.get(f"/api/v1/users/{user_id}", headers=headers, cookies=cookies)

    async def update_user_info(self, user_id: int, user: UpdateUserSchema, headers: Headers, cookies: dict):
        return await self.api_client.patch(f"/api/v1/users/{user_id}", json_payload=user, headers=headers, cookies=cookies)

    async def update_user_roles(self, user_id: int, roles_ids: list[int], headers: Headers, cookies: dict):
        return await self.api_client.patch(f"/api/v1/users/{user_id}/roles", json_payload=roles_ids, headers=headers, cookies=cookies)