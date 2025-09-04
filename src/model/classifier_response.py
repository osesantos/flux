from pydantic import BaseModel

class ClassifierResponse(BaseModel):
    provider: str
    model: str
    confidence: float
