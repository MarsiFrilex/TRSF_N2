import time

from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger

from src.database.connection import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(BigInteger, default=int(time.time()), nullable=False)
    updated_at = Column(BigInteger, default=int(time.time()), onupdate=int(time.time()), nullable=False)


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)


class UserRoles(Base):
    __tablename__ = "user_roles"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)