from ollama import Client
from loguru import logger

# TODO: Change to use env or config file
# URL = "http://ollama-phi.ollama.svc.cluster.local:11435"

BASE_URL = "http://localhost"


async def generate(query: str, model: str) -> str:
    """
    Generate a response from the Ollama model based on the input query.
    """
    if query is None or query.strip() == "":
        raise ValueError("Query must be specified")

    client = Client(
        host=_get_host(model)
    )

    logger.info(f"Generating model={model}...")
    response = client.generate(model=model, prompt=query)
    logger.info(f"Generation complete.")

    return response.response.strip()


async def embeddings(query: str, model: str = "nomic-embed-text") -> list[float]:
    """
    Generate embeddings from the Ollama embedding model based on the input query.
    """
    if query is None or query.strip() == "":
        raise ValueError("Query must be specified")

    client = Client(
        host=_get_host(model)
    )

    logger.info(f"Generating embeddings model={model}...")
    response = client.embeddings(model=model, prompt=query)
    logger.info(f"Embeddings generation complete.")

    # Convert sequence to list of floats
    return [float(x) for x in response.embedding]


def _get_port(model: str) -> int:
    """
    Get the port number for the specified Ollama model.
    TODO: Change to use env or a dict in config file
    """
    model_ports = {
        "mistral": 11434,
        "phi3:mini": 11435,
        "nomic-embed-text": 11436,
        "gemma3:1b": 11437
    }
    return model_ports.get(model, 11434)  # Default to 11434 if model not found


def _get_host(model: str) -> str:
    """
    Get the host URL for the specified Ollama model.
    """
    base_url = "ollama.svc.cluster.local"
    port = _get_port(model)
    model_hosts = {
        "mistral": f"http://ollama-mistral.{base_url}:{port}",
        "phi3:mini": f"http://ollama-phi.{base_url}:{port}",
        "nomic-embed-text": f"http://ollama-embed.{base_url}:{port}",
        "gemma3:1b": f"http://ollama-gemma.{base_url}:{port}"
    }
    # Default to localhost:11434 if model not found
    return model_hosts.get(model, "http://localhost:11434")
