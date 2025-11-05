from sqlalchemy import select, insert, update, delete

from src.database.connection import async_session_maker
from src.database.models import Orders
from src.schemas.orders_schemas import OrderCreateSchema, OrderUpdateSchema


class OrdersRepository:

    @staticmethod
    async def create_order(new_order: OrderCreateSchema):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(Orders)
                .values(**new_order.model_dump())
                .returning(Orders)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def get_orders():
        async with async_session_maker() as session:
            result = await session.execute(
                select(Orders)
            )
            await session.commit()
            return result.scalars().all() or []

    @staticmethod
    async def get_order(order_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Orders)
                .where(Orders.id == order_id)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def update_order(order_id: int, new_order: OrderUpdateSchema):
        async with async_session_maker() as session:
            result = await session.execute(
                update(Orders)
                .values(**new_order.model_dump())
                .where(Orders.id == order_id)
                .returning(Orders)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def delete_order(order_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Orders)
                .where(Orders.id == order_id)
                .returning(Orders)
            )
            await session.commit()
            return result.scalar_one_or_none()