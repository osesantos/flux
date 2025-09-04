from ollama import Client

# TODO: Change to use env or config file
#URL = "http://ollama-phi.ollama.svc.cluster.local:11435"

client = Client(
    host="http://localhost:11434"
)
MODEL = "mistral"

async def generate(query: str) -> str:
    """
    Generate a response from the Ollama model based on the input query.
    """
    if query is None or query.strip() == "":
        raise ValueError("Query must be specified")

    response = client.generate(model=MODEL,prompt=query)   

    return response.response.strip()
