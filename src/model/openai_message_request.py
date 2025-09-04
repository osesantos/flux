from pydantic import BaseModel

class OpenAiMessageRequest(BaseModel):
    role: str
    content: str
