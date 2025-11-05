from fastapi import APIRouter, Depends

from src.api.dependencies import get_users_service
from src.schemas.user_schemas import UpdateUserSchema
from src.services.users_service import UsersService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("")
async def get_users_list(users_service: UsersService = Depends(get_users_service)):
    return await users_service.get_all()


@router.get("/{user_id}")
async def get_concrete_user(
        user_id: int,
        users_service: UsersService = Depends(get_users_service)
):
    return await users_service.get(user_id)


@router.patch("/{user_id}")
async def update_user_info(
        user_id: int,
        user: UpdateUserSchema,
        users_service: UsersService = Depends(get_users_service)
):
    return await users_service.update(user_id, user)


@router.patch("/{user_id}/roles")
async def update_user_roles(
        user_id: int,
        roles_ids: list[int] | None,
        users_service: UsersService = Depends(get_users_service)
):
    return await users_service.update_roles(user_id, roles_ids)