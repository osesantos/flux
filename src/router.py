from fastapi.routing import APIRouter
from src.model import InferRequest, ClassifyRequest, ClassifyResponse, EmbedRequest

router = APIRouter(prefix="/v1", tags=["v1"])

@router.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok"}

@router.post("/infer")
async def infer(payload: InferRequest):
    """
    Inference endpoint that routes the request to the appropriate provider based on the payload.
    If no provider or model is specified, it classifies the query to determine the best provider.
    Example payload:
    {
        "query": "What is the capital of France?",
        "provider": "ollama",  # Optional
        "model": "mistral",    # Optional
        "max_tokens": 256      # Optional
    }
    """
    from src.providers.base import infer_provider

    return await infer_provider(payload.query, payload.provider or "", payload.model or "", payload.max_tokens or 256)

@router.post("/classify")
async def classify_prompt(payload: ClassifyRequest):
    """
    Classification endpoint that classifies the query to determine the best provider.
    Example payload:
    {
        "prompt": "What is the capital of France?"
    }
    """
    from src.classifier.service import classify

    response = await classify(payload.prompt)
    return ClassifyResponse(response=response)

@router.post("/embed")
async def embed_query(payload: EmbedRequest):
    """
    Embedding endpoint that generates embeddings for the given query using the specified provider.
    Example query: "What is the capital of France?"
    """
    from src.embedder.service import embed_text

    return await embed_text(payload.query)
