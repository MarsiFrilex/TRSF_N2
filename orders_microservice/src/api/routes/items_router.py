from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.post("")
async def create_item():
    pass


@router.get("")
async def get_items():
    pass


@router.delete("/{item_id}")
async def delete_item():
    pass