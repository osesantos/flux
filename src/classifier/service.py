from ollama import Client
from loguru import logger

# TODO: Change to use env or config file
# URL = "http://ollama-phi.ollama.svc.cluster.local:11435"

client = Client(
    host="http://ollama-phi.ollama.svc.cluster.local:11435"
)

MODEL = "phi3:mini"

async def classify(prompt: str) -> str:
    """
    A simple classifier service that classifies text into categories.
    Calls the phi3 model in ollama to classify the text.
    """
    if prompt is None or prompt.strip() == "":
        raise ValueError("Prompt must be specified")

    logger.info(f"Classifying model={MODEL}...")
    response = client.generate(model=MODEL,prompt=prompt)   
    logger.info(f"Classificiation complete.")

    return response.response
