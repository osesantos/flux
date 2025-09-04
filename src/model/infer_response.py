from pydantic import BaseModel

class InferResponse(BaseModel):
    provider: str
    model: str
    classification_confidence: float = 0.0
    latency_ms: float = 0.0
    cost_usd: float = 0.0
    response: str
