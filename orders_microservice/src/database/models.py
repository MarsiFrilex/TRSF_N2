import time

from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from src.database.connection import Base


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, nullable=False)
    status_id = Column(Integer, ForeignKey('statuses.id'), nullable=False)
    created_at = Column(BigInteger, nullable=False, default=int(time.time()))
    updated_at = Column(BigInteger, nullable=False, default=int(time.time()), onupdate=int(time.time()))


class OrdersItems(Base):
    __tablename__ = 'orders_items'
    order_id = Column(Integer, ForeignKey('orders.id', ondelete="CASCADE"), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)
    count = Column(Integer, nullable=False)


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Integer, nullable=False)


class Statuses(Base):
    __tablename__ = 'statuses'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)