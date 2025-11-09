from fastapi import APIRouter

router = APIRouter(
    prefix="/orders-items",
    tags=["orders-items"]
)