from fastapi import APIRouter, Depends, HTTPException
from src.services.orders_service import OrdersService

from src.api.dependencies import get_orders_service
from src.schemas.orders_schemas import OrderUpdateSchema, OrderCreateSchema

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("")
async def create_order(
        new_order: OrderCreateSchema,
        service: OrdersService = Depends(get_orders_service),
):
    if result := await service.create_order(new_order):
        return result
    raise HTTPException(status_code=404, detail="Status not found")


@router.get("")
async def get_orders(
        service: OrdersService = Depends(get_orders_service),
):
    return await service.get_orders()


@router.get("/{order_id}")
async def get_order(
        order_id: int,
        service: OrdersService = Depends(get_orders_service),
):
    return await service.get_order(order_id)


@router.patch("/{order_id}")
async def update_order(
        order_id: int,
        new_order: OrderUpdateSchema,
        service: OrdersService = Depends(get_orders_service),
):
    if result := await service.update_order(order_id, new_order):
        return result
    raise HTTPException(status_code=404, detail="Order or status not found")


@router.delete("/{order_id}")
async def delete_order(
        order_id: int,
        service: OrdersService = Depends(get_orders_service),
):
    if result := await service.delete_order(order_id):
        return result
    raise HTTPException(status_code=404, detail="Order not found")