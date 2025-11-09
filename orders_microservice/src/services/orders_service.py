from src.repositories.orders_items_repository import OrdersItemsRepository
from src.repositories.orders_repository import OrdersRepository

from src.schemas.orders_schemas import OrderCreateSchema, OrderUpdateSchema


class OrdersService:
    def __init__(
            self,
            orders_repository: OrdersRepository,
            orders_items_repository: OrdersItemsRepository,
    ):
        self.orders_repository = orders_repository
        self.orders_items_repository = orders_items_repository

    async def get_orders(self):
        return await self.orders_repository.get_orders()

    async def get_order(self, order_id: int):
        return await self.orders_repository.get_order(order_id)

    async def create_order(self, new_order: OrderCreateSchema):
        return await self.orders_repository.create_order(new_order)

    async def update_order(self, order_id: int, new_order: OrderUpdateSchema):
        return await self.orders_repository.update_order(order_id, new_order)

    async def delete_order(self, order_id: int):
        return await self.orders_repository.delete_order(order_id)

    async def get_order_items(self, order_id: int):
        return await self.orders_items_repository.get_order_items(order_id)

    async def add_item_to_order(self, order_id: int, item_id: int, count: int):
        return await self.orders_items_repository.add_item_to_order(order_id, item_id, count)

    async def remove_item_from_order(self, order_id: int, item_id: int):
        return await self.orders_items_repository.remove_item_from_order(order_id, item_id)