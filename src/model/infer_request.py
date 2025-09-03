from pydantic import BaseModel

class InferRequest(BaseModel):
    provider: str | None = ""
    model: str | None = ""
    query: str
    max_tokens: int | None = 256
