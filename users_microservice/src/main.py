import uvicorn

from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse

from src.api.base_router import base_router
from src.api.app_exceptions import app_exception_handler

app = FastAPI()
app.include_router(base_router)

app.add_exception_handler(Exception, app_exception_handler)
app.add_exception_handler(HTTPException, app_exception_handler)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)