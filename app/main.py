from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.config import settings
import uvicorn
from app.api.router import router as api_router
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import check_db_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting app with version", app.version, "....")
    await check_db_connection()
    yield
    print("Application has Shutdown...")


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    port=settings.port,
    lifespan=lifespan
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(api_router, prefix="/api")


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
