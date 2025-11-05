from fastapi import Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.repositories.auth_repository import AuthRepository
from src.repositories.users_repository import UsersRepository
from src.services.auth_service import AuthService
from src.services.users_service import UsersService

auth_scheme = HTTPBearer()


async def get_auth_service() -> AuthService:
    return AuthService(AuthRepository(), UsersRepository())


async def get_users_service() -> UsersService:
    return UsersService(AuthRepository(), UsersRepository())


async def get_current_user(token: HTTPAuthorizationCredentials = Security(auth_scheme), auth_service = Depends(get_auth_service)):
    return await auth_service.get_current_user(token.credentials)