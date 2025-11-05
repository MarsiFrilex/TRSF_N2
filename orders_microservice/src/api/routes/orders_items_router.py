from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/order-items",
    tags=["OrderItems"]
)


@router.post("")
async def add_item_to_order():
    pass


@router.get("/{order_id}")
async def get_order_items():
    pass


@router.delete("/{order_id}")
async def remove_item_from_order():
    pass