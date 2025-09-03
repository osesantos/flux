from .prompts import llm_classification_prompt
from ollama import Client
from loguru import logger

# TODO: Change to use env or config file
#URL = "http://ollama-phi.ollama.svc.cluster.local:11435"
URL = "http://localhost:11435"
MODEL = "phi3:mini"

async def classify(prompt: str) -> str:
    """
    A simple classifier service that classifies text into categories.
    Calls the phi3 model in ollama to classify the text.
    """
    client = Client(host=URL)

    logger.info(f"Classifying using model: '{MODEL}'")
    response = client.generate(model=MODEL,prompt=prompt)   

    return response.response.strip()

