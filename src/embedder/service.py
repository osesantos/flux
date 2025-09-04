from src.providers.ollama import embeddings

async def embed_text(text: str) -> list[float]:
    """
    Generate embeddings for the given text using the Ollama embedding model.
    """
    if text is None or text.strip() == "":
        raise ValueError("Text must be specified")

    try:
        return await embeddings(text, "nomic-embed-text")
    except ValueError as e:
        raise ValueError(f"Failed to parse embeddings: {e}")
