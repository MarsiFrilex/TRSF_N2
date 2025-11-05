from pydantic import BaseModel


class LoginUserSchema(BaseModel):
    email: str
    password: str


class RefreshTokenSchema(BaseModel):
    token: str