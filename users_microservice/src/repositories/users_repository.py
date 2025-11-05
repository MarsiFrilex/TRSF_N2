from sqlalchemy import insert, select, update, delete

from src.schemas.user_schemas import InsertUserSchema, UpdateUserSchema, FullUserSchema, RoleSchema
from src.database.connection import async_session_maker
from src.database.models import Users, Roles, UserRoles


class UsersRepository:

    @staticmethod
    async def get_all():
        async with async_session_maker() as session:
            result = await session.execute(select(Users))
            return result.scalars().all()

    @staticmethod
    async def get(user_id: int):
        async with async_session_maker() as session:
            user_res = await session.execute(select(Users).where(Users.id == user_id))
            if user := user_res.scalar_one_or_none():
                roles_res = await session.execute(
                    select(Roles)
                    .join(UserRoles, Roles.id == UserRoles.role_id)
                    .where(UserRoles.user_id == user_id)
                )
                roles = roles_res.scalars().all()
                return FullUserSchema(
                    id=user.id,
                    user_name=user.user_name,
                    email=user.email,
                    hashed_password=user.hashed_password,
                    created_at=user.created_at,
                    updated_at=user.updated_at,
                    roles=[RoleSchema(
                        id=role.id,
                        title=role.title
                    ) for role in roles]
                )
            return None

    @staticmethod
    async def get_by_email(email: str):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Users)
                .where(Users.email == email)
            )
            return result.scalar_one_or_none()

    @staticmethod
    async def create(user: InsertUserSchema):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(Users)
                .values(**user.model_dump())
                .returning(Users.id)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def update(user_id: int, user: InsertUserSchema):
        async with async_session_maker() as session:
            result = await session.execute(
                update(Users)
                .values(**user.model_dump(exclude_none=True))
                .where(Users.id == user_id)
                .returning(Users)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def update_roles(user_id: int, roles_ids: list[int] | None):
        async with async_session_maker() as session:
            insert_roles = [
                {"user_id": user_id, "role_id": role_id}
                for role_id in roles_ids
            ]
            await session.execute(delete(UserRoles).where(UserRoles.user_id == user_id))
            await session.execute(insert(UserRoles).values(insert_roles))
            await session.commit()

    @staticmethod
    async def delete(user_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Users)
                .where(Users.id == user_id)
                .returning(Users)
            )
            await session.commit()
            return result.scalar_one_or_none()