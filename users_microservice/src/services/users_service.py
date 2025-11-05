from passlib.utils import has_salt_info

from src.repositories.auth_repository import AuthRepository
from src.repositories.users_repository import UsersRepository
from src.schemas.user_schemas import UpdateUserSchema, InsertUserSchema


class UsersService:
    def __init__(
            self,
            auth_repository: AuthRepository,
            users_repository: UsersRepository,
    ):
        self.auth_repository = auth_repository
        self.users_repository = users_repository

    async def get_all(self):
        return await self.users_repository.get_all()

    async def get(self, user_id: int):
        return await self.users_repository.get(user_id)

    async def update(self, user_id: int, user: UpdateUserSchema):
        user_insert = InsertUserSchema(
            user_name=user.user_name or None,
            email=user.email or None,
            hashed_password=None,
        )
        if hashed_password := await self.auth_repository.get_password_hash(user.password):
            user_insert.hashed_password = hashed_password
        return await self.users_repository.update(user_id, user_insert)

    async def update_roles(self, user_id: int, roles_ids: list[int] | None):
        return await self.users_repository.update_roles(user_id, roles_ids)