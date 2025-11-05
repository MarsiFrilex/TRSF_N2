from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_orders_service
from src.schemas.orders_items_schemas import RemoveItemSchema, AddItemSchema
from src.services.orders_service import OrdersService

router = APIRouter(
    prefix="/order-items",
    tags=["OrderItems"]
)


@router.post("")
async def add_item_to_order(
        item: AddItemSchema,
        service: OrdersService = Depends(get_orders_service),
):
    if result := await service.add_item_to_order(item.order_id, item.item_id, item.count):
        return result
    raise HTTPException(status_code=404, detail="Item or order not found")


@router.get("/{order_id}")
async def get_order_items(
        order_id: int,
        service: OrdersService = Depends(get_orders_service),
):
    return await service.get_order_items(order_id)


@router.delete("/{order_id}")
async def remove_item_from_order(
        order_id: int,
        item: RemoveItemSchema,
        service: OrdersService = Depends(get_orders_service),
):
    if result := await service.remove_item_from_order(order_id, item.item_id):
        return result
    raise HTTPException(status_code=404, detail="Item or order not found")