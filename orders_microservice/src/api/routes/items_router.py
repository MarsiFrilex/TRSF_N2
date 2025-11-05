from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_items_service
from src.schemas.items_schemas import CreateItemSchema
from src.services.items_service import ItemsService

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.post("")
async def create_item(
        item: CreateItemSchema,
        service: ItemsService = Depends(get_items_service),
):
    return await service.create_item(item.title, item.price)


@router.get("")
async def get_items(
        service: ItemsService = Depends(get_items_service),
):
    return await service.get_items()


@router.delete("/{item_id}")
async def delete_item(
        item_id: int,
        service: ItemsService = Depends(get_items_service),
):
    if result := await service.delete_item(item_id):
        return result
    raise HTTPException(status_code=404, detail="Item not found")