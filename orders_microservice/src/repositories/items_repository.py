from sqlalchemy import select, insert, delete

from src.database.connection import async_session_maker
from src.database.models import Items


class ItemsRepository:

    @staticmethod
    async def create_item(title: str, price: float):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(Items)
                .values(title=title, price=price)
                .returning(Items)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def read_items():
        async with async_session_maker() as session:
            result = await session.execute(
                select(Items)
            )
            await session.commit()
            return result.scalars().all() or []

    @staticmethod
    async def delete_item(item_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Items)
                .where(Items.id == item_id)
                .returning(Items)
            )
            await session.commit()
            return result.scalar_one_or_none()