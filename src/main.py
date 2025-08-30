from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routes.api import healthcheck, products
from .database import connect_to_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_database()
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

app.include_router(products.router, prefix="/api/v1")
app.include_router(healthcheck.router, prefix="/api/v1")
