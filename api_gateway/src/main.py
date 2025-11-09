import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from src.api.app_exceptions import app_exception_handler
from src.api.base_router import base_router

app = FastAPI()
app.include_router(base_router)

app.add_exception_handler(Exception, app_exception_handler)
app.add_exception_handler(HTTPException, app_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)