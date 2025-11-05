from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("")
async def get_users_list():
    pass


@router.get("/{user_id}")
async def get_concrete_user():
    pass


@router.patch("/{user_id}")
async def update_user_info():
    pass


@router.patch("/{user_id}/roles")
async def update_user_roles():
    pass