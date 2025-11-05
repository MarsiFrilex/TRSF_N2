from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register_user():
    pass


@router.post("/login")
async def login_user():
    pass


@router.post("/refresh")
async def refresh_token():
    pass


@router.get("/me")
async def get_current_user():
    pass