from pydantic import BaseModel

class InferResponse(BaseModel):
    provider: str
    model: str
    latency_ms: float
    cost_usd: float
    response: str
