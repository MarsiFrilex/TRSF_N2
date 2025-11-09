from fastapi import APIRouter, Depends, Request

from src.api.base_responses import SuccessResponse
from src.api.dependencies import get_orders_proxy_service, current_user_dependency
from src.schemas.orders_schemas import CreateItemSchema
from src.services.orders_proxy_service import OrdersProxyService

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(current_user_dependency)],
)


@router.post("")
async def create_item(
        request: Request,
        item: CreateItemSchema,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    result = await proxy_service.create_item(item, request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.get("")
async def get_items(
        request: Request,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    result = await proxy_service.get_items(request.headers, request.cookies)
    return SuccessResponse(data=result)


@router.delete("/{item_id}")
async def delete_item(
        request: Request,
        item_id: int,
        proxy_service: OrdersProxyService = Depends(get_orders_proxy_service),
):
    result = await proxy_service.delete_item(item_id, request.headers, request.cookies)
    return SuccessResponse(data=result)