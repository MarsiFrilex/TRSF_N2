import asyncio

import uvicorn

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.api.base_router import base_router
from src.database.connection import create_tables

app = FastAPI()
app.include_router(base_router)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    # asyncio.run(create_tables())
    uvicorn.run(app, host="0.0.0.0", port=8000)