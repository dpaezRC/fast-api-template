from fastapi import FastAPI
from datetime import datetime


app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}
