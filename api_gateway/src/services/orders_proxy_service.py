from starlette.datastructures import Headers

from src.http_client.http_client import HTTPClient
from src.schemas.orders_schemas import *


class OrdersProxyService:
    def __init__(self):
        self.api_client = HTTPClient("http://orders_microservice:8002")

    # Orders endpoints
    async def get_orders(self, headers: Headers, cookies: dict):
        return await self.api_client.get("/api/v1/orders", headers=headers, cookies=cookies)

    async def create_order(self, order_data: OrderCreateSchema, headers: Headers, cookies: dict):
        return await self.api_client.post("/api/v1/orders", json_payload=order_data, headers=headers, cookies=cookies)

    async def get_order(self, order_id: int, headers: Headers, cookies: dict):
        return await self.api_client.get(f"/api/v1/orders/{order_id}", headers=headers, cookies=cookies)

    async def update_order(self, order_id: int, order_data: OrderUpdateSchema, headers: Headers, cookies: dict):
        return await self.api_client.patch(f"/api/v1/orders/{order_id}", json_payload=order_data, headers=headers, cookies=cookies)

    async def delete_order(self, order_id: int, headers: Headers, cookies: dict):
        return await self.api_client.delete(f"/api/v1/orders/{order_id}", headers=headers, cookies=cookies)

    # OrderItems endpoints
    async def add_item_to_order(self, item_data: AddItemSchema, headers: Headers, cookies: dict):
        return await self.api_client.post("/api/v1/order-items", json_payload=item_data, headers=headers, cookies=cookies)

    async def get_order_items(self, order_id: int, headers: Headers, cookies: dict):
        return await self.api_client.get(f"/api/v1/order-items/{order_id}", headers=headers, cookies=cookies)

    async def remove_item_from_order(self, order_id: int, item: RemoveItemSchema, headers: Headers, cookies: dict):
        return await self.api_client.delete(f"/api/v1/order-items/{order_id}", json_payload=item, headers=headers, cookies=cookies)

    # Items endpoints
    async def get_items(self, headers: Headers, cookies: dict):
        return await self.api_client.get("/api/v1/items", headers=headers, cookies=cookies)

    async def create_item(self, item_data: CreateItemSchema, headers: Headers, cookies: dict):
        return await self.api_client.post("/api/v1/items", json_payload=item_data, headers=headers, cookies=cookies)

    async def delete_item(self, item_id: int, headers: Headers, cookies: dict):
        return await self.api_client.delete(f"/api/v1/items/{item_id}", headers=headers, cookies=cookies)