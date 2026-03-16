from datetime import datetime

from fastapi import APIRouter

router = APIRouter(prefix="/healthcheck")


@router.get(
    "/",
    tags=["Healthcheck"],
    summary="Healthcheck endpoint",
    description="Returns the health status of the application.",
)
def healthcheck():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}
