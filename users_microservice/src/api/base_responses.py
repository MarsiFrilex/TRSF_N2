from pydantic import BaseModel


class ErrorResponse(BaseModel):
    success: bool = False
    error_code: int
    message: str
