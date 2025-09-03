from pydantic import BaseModel

class ClassifyResponse(BaseModel):
    response: str
