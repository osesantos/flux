from fastapi import FastAPI
from fastapi.routing import APIRouter

router = APIRouter(prefix="/v1", tags=["v1"])

@router.post("/infer")
async def infer(payload: dict):
    """
    Minimal hello world for inference endpoint.
    payload example: {"query": "What is the capital of France?"}
    """

    query = payload.get("query", "")
    return {"response": f"Echo: {query}"}
