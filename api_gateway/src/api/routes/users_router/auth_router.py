from fastapi import APIRouter, Depends, Request

from src.api.base_responses import SuccessResponse
from src.api.dependencies import get_users_proxy_service, current_user_dependency
from src.schemas.users_schemas import CreateUserSchema, LoginUserSchema, RefreshTokenSchema
from src.services.users_proxy_service import UsersProxyService

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/register-user")
async def register_user(
        request: Request,
        user: CreateUserSchema,
        proxy_service: UsersProxyService = Depends(get_users_proxy_service),
):
    result = await proxy_service.register_user(user, request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.post("/login-user")
async def login_user(
        request: Request,
        user: LoginUserSchema,
        proxy_service: UsersProxyService = Depends(get_users_proxy_service),
):
    result = await proxy_service.login_user(user, request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.post("/refresh-token")
async def refresh_token(
        request: Request,
        token: RefreshTokenSchema,
        proxy_service: UsersProxyService = Depends(get_users_proxy_service),
):
    result = await proxy_service.refresh_token(token, request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.get("/current-user")
async def current_user(
        user = Depends(current_user_dependency),
):
    return SuccessResponse(data=user)