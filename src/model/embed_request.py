from pydantic import BaseModel

class EmbedRequest(BaseModel):
    query: str
