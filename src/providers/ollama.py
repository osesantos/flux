from ollama import Client

# TODO: Change to use env or config file
#URL = "http://ollama-phi.ollama.svc.cluster.local:11435"

BASE_URL = "http://localhost"

async def generate(query: str, model: str) -> str:
    """
    Generate a response from the Ollama model based on the input query.
    """
    if query is None or query.strip() == "":
        raise ValueError("Query must be specified")

    port = _get_port(model)

    client = Client(
        host=f"{BASE_URL}:{port}"
    )

    response = client.generate(model=model,prompt=query)   

    return response.response.strip()

async def embeddings(query: str, model: str = "nomic-embed-text") -> list[float]:
    """
    Generate embeddings from the Ollama embedding model based on the input query.
    """
    if query is None or query.strip() == "":
        raise ValueError("Query must be specified")

    port = _get_port(model)

    client = Client(
        host=f"{BASE_URL}:{port}"
    )

    response = client.embeddings(model=model,prompt=query)   

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
