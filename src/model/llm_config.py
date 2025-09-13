from pydantic import BaseModel

class LLMConfig(BaseModel):
    name: str
    model: str
    provider: str
    url: str
    port: int
    host: str
