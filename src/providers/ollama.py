from ollama import Client
from loguru import logger
from src.config.config import get_llm_config_by_name

async def generate(query: str, llm_name: str) -> str:
    """
    Generate a response from the Ollama model based on the input query.
    """
    if query is None or query.strip() == "":
        raise ValueError("Query must be specified")

    llm = get_llm_config_by_name(llm_name)
    client = Client(
        host=llm.host
    )

    logger.info(f"Generating model={llm_name}...")
    response = client.generate(model=llm.model, prompt=query)
    logger.info(f"Generation complete.")

    return response.response.strip()


async def embeddings(query: str, llm_name: str = "nomic-embed-text") -> list[float]:
    """
    Generate embeddings from the Ollama embedding model based on the input query.
    """
    if query is None or query.strip() == "":
        raise ValueError("Query must be specified")

    llm = get_llm_config_by_name(llm_name)
    client = Client(
        host=llm.host 
    )

    logger.info(f"Generating embeddings model={llm_name}...")
    response = client.embeddings(model=llm.name, prompt=query)
    logger.info(f"Embeddings generation complete.")

    # Convert sequence to list of floats
    return [float(x) for x in response.embedding]
