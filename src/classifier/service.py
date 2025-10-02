from ollama import Client
from loguru import logger

LLM_NAME = "gemma3:270m"

async def classify(prompt: str) -> str:
    """
    A simple classifier service that classifies text into categories.
    Calls the phi3 model in ollama to classify the text.
    """
    from src.config.config import get_llm_config_by_name

    llm = get_llm_config_by_name(LLM_NAME)

    logger.info(f"Using LLM: {llm.name} ({llm.model}) at {llm.host}")
    client = Client(
        host=llm.host
    )

    if prompt is None or prompt.strip() == "":
        raise ValueError("Prompt must be specified")

    logger.info(f"Classifying with {llm.name}...")
    response = client.generate(model=llm.model, prompt=prompt)   
    logger.info(f"Classification complete.")

    return response.response
