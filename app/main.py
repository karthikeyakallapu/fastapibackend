from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.config import settings
import uvicorn


@asynccontextmanager
async def lifespan(app : FastAPI):
    print("Starting app with version", app.version, "....")

    yield
    print("Application has Shutdown...")


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    port = settings.port,
    lifespan=lifespan

)


@app.get("/")
async def hello_world():
    return {"hello": "Hii"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
