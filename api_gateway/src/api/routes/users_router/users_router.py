from fastapi import APIRouter, Depends, Request

from src.api.base_responses import SuccessResponse
from src.api.dependencies import get_users_proxy_service
from src.schemas.users_schemas import UpdateUserSchema
from src.services.users_proxy_service import UsersProxyService

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("")
async def get_users_list(
        request: Request,
        proxy_service: UsersProxyService = Depends(get_users_proxy_service),
):
    result = await proxy_service.get_users_list(request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.get("/{user_id}")
async def get_concrete_user(
        request: Request,
        user_id: int,
        proxy_service: UsersProxyService = Depends(get_users_proxy_service),
):
    result = await proxy_service.get_concrete_user(user_id, request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.patch("/{user_id}")
async def update_users_info(
        request: Request,
        user_id: int,
        user: UpdateUserSchema,
        proxy_service: UsersProxyService = Depends(get_users_proxy_service),
):
    result = await proxy_service.update_user_info(user_id, user, request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.patch("/{user_id}/roles")
async def update_users_roles(
        request: Request,
        user_id: int,
        roles_ids: list[int],
        proxy_service: UsersProxyService = Depends(get_users_proxy_service),
):
    result = await proxy_service.update_user_roles(user_id, roles_ids, request.headers, request.cookies)
    return SuccessResponse(data=result)