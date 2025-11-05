from src.repositories.items_repository import ItemsRepository


class ItemsService:
    def __init__(
            self,
            repository: ItemsRepository,
    ):
        self.repository = repository

    async def create_item(self, title: str, price: float):
        return await self.repository.create_item(title, price)

    async def get_items(self):
        return await self.repository.read_items()

    async def delete_item(self, item_id: int):
        return await self.repository.delete_item(item_id)