from fastapi import APIRouter, Depends, Request

from src.api.dependencies import get_orders_proxy_service
from src.schemas.orders_schemas import AddItemSchema, RemoveItemSchema
from src.services.orders_proxy_service import OrdersProxyService

router = APIRouter(
    prefix="/orders-items",
    tags=["orders-items"]
)


@router.post("")
async def add_item_to_order(
        request: Request,
        item: AddItemSchema,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    return await proxy_service.add_item_to_order(item, request.headers, request.cookies)


@router.get("/{order_id}")
async def get_order_items(
        request: Request,
        order_id: int,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    return await proxy_service.get_order_items(order_id, request.headers, request.cookies)


@router.delete("/{order_id}")
async def remove_item_from_order(
        request: Request,
        order_id: int,
        item: RemoveItemSchema,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    return await proxy_service.remove_item_from_order(order_id, item, request.headers, request.cookies)