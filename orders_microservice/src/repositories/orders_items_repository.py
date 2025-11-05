from sqlalchemy import select, insert, delete, and_

from src.database.connection import async_session_maker
from src.database.models import OrdersItems


class OrdersItemsRepository:

    @staticmethod
    async def get_order_items(order_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                select(OrdersItems)
                .where(OrdersItems.order_id == order_id)
            )
            await session.commit()
            return result.scalars().all() or []

    @staticmethod
    async def add_item_to_order(order_id: int, item_id: int, count: int):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(OrdersItems)
                .values(
                    order_id=order_id,
                    item_id=item_id,
                    count=count,
                )
                .returning(OrdersItems)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def remove_item_from_order(order_id: int, item_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(OrdersItems)
                .where(and_(
                    OrdersItems.order_id==order_id,
                    OrdersItems.item_id==item_id
                ))
                .returning(OrdersItems)
            )
            await session.commit()
            return result.scalar_one_or_none()