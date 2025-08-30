from fastapi import FastAPI, APIRouter
from datetime import datetime


app = FastAPI()
api_v1 = APIRouter(prefix="/api/v1")


@api_v1.get(
    "/healthcheck",
    tags=["Healthcheck"],
    summary="Healthcheck endpoint",
    description="Returns the health status of the application.",
)
def healthcheck():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}


app.include_router(api_v1)
