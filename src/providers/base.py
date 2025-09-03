from classifier.service import classify
from classifier.prompts import llm_classification_prompt
from loguru import logger
from src.model import InferResponse

async def infer_provider(query: str, provider: str = "", model: str = "", max_tokens: int = 256) -> InferResponse:
    response = "" 
    if provider == "" and model == "":
        logger.info("No provider or model specified, classifying query...")
        model = await classify(llm_classification_prompt(query))
        logger.info(f"Classified provider: '{model}'")

    if model == "ollama":
        from .ollama import generate as ollama_generate
        logger.info("Using Ollama provider...")
        response = await ollama_generate(query)
        logger.info(f"Ollama response: '{response}'")

    return InferResponse(
        response=response,
        provider=provider,
        model=model,
        latency_ms=0,  # Placeholder for latency measurement
        cost_usd=0.0  # Placeholder for cost calculation
    )
