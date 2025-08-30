from fastapi import FastAPI
from .routes.api import healthcheck, products

app = FastAPI()

app.include_router(products.router, prefix="/api/v1")
app.include_router(healthcheck.router, prefix="/api/v1")
