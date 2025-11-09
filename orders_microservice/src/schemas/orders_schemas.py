from pydantic import BaseModel


class OrderSchema(BaseModel):
    id: int
    user_id: int
    status_id: int
    created_at: int
    updated_at: int


class OrderItemSchema(BaseModel):
    item_id: int
    count: int


class FullOrderSchema(BaseModel):
    id: int
    user_id: int
    status_id: int
    created_at: int
    updated_at: int
    items: list[OrderItemSchema]


class OrderCreateSchema(BaseModel):
    user_id: int
    status_id: int


class OrderUpdateSchema(BaseModel):
    status_id: int