from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status
from src.repositories.auth_repository import AuthRepository
from src.repositories.users_repository import UsersRepository
from src.schemas.user_schemas import InsertUserSchema, CreateUserSchema


class AuthService:
    def __init__(
            self,
            auth_repository: AuthRepository,
            users_repository: UsersRepository,
    ):
        self.auth_repository = auth_repository
        self.users_repository = users_repository

    async def register(self, user: CreateUserSchema):
        if not await self.users_repository.get_by_email(user.email):
            hashed_password = await self.auth_repository.get_password_hash(user.password)
            user_insert = InsertUserSchema(
                user_name=user.user_name,
                email=user.email,
                hashed_password=hashed_password
            )
            return await self.users_repository.create(user_insert)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Пользователь с таким email уже существует")

    async def login(self, email: str, password: str):
        if user := await self.users_repository.get_by_email(email):
            if await self.auth_repository.verify_password(password, user.hashed_password):
                data: dict = {"sub": str(user.id)}

                access_token = await self.auth_repository.create_access_token(data)
                refresh_token = await self.auth_repository.create_refresh_token(data)

                return {"access_token": access_token, "refresh_token": refresh_token}
        raise HTTPException(status_code=401, detail="Not authenticated")

    async def get_current_user(self, token: str):
        payload = await self.auth_repository.decode_token(token)

        expire = payload.get('exp')
        expire_time = datetime.fromtimestamp(int(expire), timezone.utc)
        current_time = datetime.now(timezone.utc) + timedelta(hours=3)

        print(expire, expire_time, current_time)

        if (not expire) or (expire_time < current_time):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Токен истек')

        user_id = payload.get('sub')
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Не найден ID пользователя')

        if user := await self.users_repository.get(int(user_id)):
            return user
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пользователь не найден')

    async def refresh_token(self, token: str):
        payload = await self.auth_repository.decode_token(token)

        user_id = payload.get('sub')
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Не найден ID пользователя')

        if user := await self.users_repository.get(int(user_id)):
            access_token = await self.auth_repository.create_access_token({"sub": str(user.id)})
            return {"access_token": access_token, "refresh_token": token}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пользователь не найден')