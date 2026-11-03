from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="DocuMind PH")


class HealthResponse(BaseModel):
    ok: bool


@app.get("/api/health")
async def health() -> HealthResponse:
    return HealthResponse(ok=True)
