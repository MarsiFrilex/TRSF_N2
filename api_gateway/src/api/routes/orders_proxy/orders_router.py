from fastapi import APIRouter, Depends, Request

from src.api.base_responses import SuccessResponse
from src.api.dependencies import get_orders_proxy_service, current_user_dependency
from src.schemas.orders_schemas import OrderCreateSchema, OrderUpdateSchema
from src.services.orders_proxy_service import OrdersProxyService

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    dependencies=[Depends(current_user_dependency)],
)


@router.post("")
async def create_order(
        request: Request,
        new_order: OrderCreateSchema,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    result = await proxy_service.create_order(new_order, request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.get("")
async def get_orders(
        request: Request,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    result = await proxy_service.get_orders(request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.get("/{order_id}")
async def get_order(
        request: Request,
        order_id: int,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    result = await proxy_service.get_order(order_id, request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.patch("/{order_id}")
async def update_order(
        request: Request,
        order_id: int,
        new_order: OrderUpdateSchema,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    result = await proxy_service.update_order(order_id, new_order, request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.delete("/{order_id}")
async def delete_order(
        request: Request,
        order_id: int,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    result = await proxy_service.delete_order(order_id, request.headers, request.cookies)
    return SuccessResponse(data=result)