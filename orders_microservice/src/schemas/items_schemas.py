from pydantic import BaseModel


class CreateItemSchema(BaseModel):
    title: str
    price: float