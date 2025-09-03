from pydantic import BaseModel

class ClassifyRequest(BaseModel):
    prompt: str
