from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
from jose import JWTError, jwt
from src.config import config
from src.utils.passwords import get_password_hash, verify_password


class AuthRepository:
    @staticmethod
    async def verify_password(plain_password: str, hashed_password: str) -> bool:
        return verify_password(plain_password, hashed_password)

    @staticmethod
    async def get_password_hash(password: str) -> str:
        return get_password_hash(password)

    @staticmethod
    async def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(hours=3) + expires_delta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)

    @staticmethod
    async def create_refresh_token(data: dict, expires_delta: timedelta = timedelta(days=7)):
        to_encode = data.copy()
        expire = datetime.now() + expires_delta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)

    @staticmethod
    async def decode_token(token: str):
        try:
            return jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        except JWTError:
            raise HTTPException(status_code=401, detail="Не валидный токен")