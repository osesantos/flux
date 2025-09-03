from ollama import Client
from loguru import logger

# TODO: Change to use env or config file
#URL = "http://ollama-phi.ollama.svc.cluster.local:11435"
URL = "http://localhost:11434"
MODEL = "mistral"

async def generate(query: str) -> str:
    """
    Generate a response from the Ollama model based on the input query.
    """
    prompt = query
    model = MODEL
    client = Client(host=URL)

    logger.info(f"Ollama generate - query: '{query}', model: '{model}'")
    response = client.generate(model=model,prompt=prompt)   
    logger.info(f"Ollama generate - response: '{response.response.strip()}'")

    return response.response.strip()
