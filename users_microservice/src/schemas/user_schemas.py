from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    user_name: str
    email: str
    password: str


class InsertUserSchema(BaseModel):
    user_name: str | None
    email: str | None
    hashed_password: str | None


class UpdateUserSchema(BaseModel):
    user_name: str | None
    email: str | None
    password: str | None


class RoleSchema(BaseModel):
    id: int
    title: str


class UserSchema(BaseModel):
    id: int
    user_name: str
    email: str
    hashed_password: str
    created_at: int
    updated_at: int


class FullUserSchema(UserSchema):
    roles: list[RoleSchema]