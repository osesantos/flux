from pydantic import BaseModel

class LLMConfig(BaseModel):
    name: str
    model: str
    provider: str
    url: str = "http://localhost"
    port: int = 11434
    host: str = "http://localhost:11434"
