from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("")
async def create_order():
    pass


@router.get("")
async def get_orders():
    pass


@router.get("/{order_id}")
async def get_order():
    pass


@router.patch("/{order_id}")
async def update_order():
    pass


@router.delete("/{order_id}")
async def delete_order():
    pass