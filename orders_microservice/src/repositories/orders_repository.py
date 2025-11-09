from sqlalchemy import select, insert, update, delete

from src.database.connection import async_session_maker
from src.database.models import Orders

from src.database.models import OrdersItems
from src.schemas.orders_schemas import OrderCreateSchema, OrderUpdateSchema, OrderItemSchema, FullOrderSchema


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
            order = result.scalar_one_or_none()
            items_res = await session.execute(
                select(OrdersItems)
                .where(OrdersItems.order_id == order_id)
            )
            order_items = [
                OrderItemSchema(
                    item_id=item.item_id,
                    count=item.count
                ) for item in items_res.scalars().all()
            ]
            await session.commit()
            full_order = FullOrderSchema(
                id=order.id,
                user_id=order.user_id,
                status_id=order.status_id,
                created_at=order.created_at,
                updated_at=order.updated_at,
                items=order_items
            )
            return full_order

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