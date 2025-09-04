from typing import Optional
from pydantic import BaseModel
from .openai_message_request import OpenAiMessageRequest


class OpenAiChoice(BaseModel):
    index: int
    message: OpenAiMessageRequest
    finish_reason: str

class OpenAiResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: list[OpenAiChoice]
