from pydantic import BaseModel
from .llm_config import LLMConfig

class Config(BaseModel):
    version: str
    llms: list[LLMConfig]

