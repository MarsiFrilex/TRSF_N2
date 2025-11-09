from fastapi import APIRouter, Depends
from src.schemas.auth_schemas import RefreshTokenSchema, LoginUserSchema
from src.schemas.user_schemas import CreateUserSchema
from src.services.auth_service import AuthService

from src.api.dependencies import get_auth_service, get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register-user")
async def register_user(
        user: CreateUserSchema,
        auth_service: AuthService = Depends(get_auth_service)
):
    user_id = await auth_service.register(user)
    return {"id": user_id}


@router.post("/login-user")
async def login_user(
        user: LoginUserSchema,
        auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.login(user.email, user.password)


@router.post("/refresh-token")
async def refresh_token(
        token: RefreshTokenSchema,
        auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.refresh_token(token.token)


@router.get("/current-user")
async def get_current_user(user = Depends(get_current_user)):
    return user