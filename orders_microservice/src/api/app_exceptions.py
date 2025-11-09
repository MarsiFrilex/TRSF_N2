from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from src.api.base_responses import ErrorResponse


async def app_exception_handler(_: Request, exc: Exception):
    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content=ErrorResponse(
                message=exc.detail,
                error_code=exc.status_code
            ).model_dump()
        )
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            message="Server error",
            error_code=500
        ).model_dump()
    )