from typing import Any, Awaitable, Callable
from loguru import logger
from src.model import InferResponse, ClassifierResponse

async def infer_provider(query: str, provider: str = "", model: str = "", max_tokens: int = 256) -> InferResponse:
    response = "" 
    latency = 0.0
    classification_confidence = 0.0

    logger.info(f"Starting inference...")

    if provider == "" or model == "":
        from src.classifier.service import classify
        from src.classifier.prompts import llm_classification_prompt

        logger.info("No provider or model specified, classifying query...")
        cresp, classification_latency = await _mesure_latency_async(
            classify,
            llm_classification_prompt(query)
        )

        classification = _parse_classification_response(cresp)

        provider = classification.provider
        model = classification.model
        classification_confidence = classification.confidence

        logger.info(f"Classification ended: '{provider}:{model}' with confidence {classification_confidence}")
        latency += classification_latency

    if provider == "ollama":
        from .ollama import generate as ollama_generate

        logger.info("Using Ollama provider...")
        response, ollama_latency = await _mesure_latency_async(
            ollama_generate,
            query,
            model
        )
        logger.info(f"Ollama responded successfully.")
        latency += ollama_latency

    elif provider == "openai":
        from .openai import chat_completion as openai_chat_completion
        from src.model import OpenAiMessageRequest

        logger.info("Using OpenAI provider...")
        model = "gpt-4.1-2025-04-14" if model == "" else model
        logger.info(f"Using default OpenAI model: '{model}'")
        messages = [OpenAiMessageRequest(role="user", content=query)]
        openai_response, openai_latency = _mesure_latency(
            openai_chat_completion,
            messages, 
            max_tokens,
            model
        )
        response = openai_response.choices[0].message.content
        logger.info(f"OpenAI responded successfully.")
        latency += openai_latency

    return InferResponse(
        response=response,
        provider=provider,
        model=model,
        classification_confidence=classification_confidence,
        latency_ms=latency,
        cost_usd=0.0  # Placeholder for cost calculation
    )

async def _mesure_latency_async(coro_func: Callable[..., Awaitable[Any]], *args, **kwargs) -> tuple[Any, float]:
    """ 
    Measures the latency of an async function call in milliseconds.
    """
    import time

    logger.info(f"Measuring latency for async function {coro_func.__name__}...")

    start_time = time.perf_counter()
    result = await coro_func(*args, **kwargs)
    end_time = time.perf_counter()
    latency_ms = (end_time - start_time) * 1000 # Convert to milliseconds
    return result, latency_ms

def _mesure_latency(func: Callable[..., Any], *args, **kwargs) -> tuple[Any, float]:
    """ 
    Measures the latency of a function call in milliseconds.
    """
    import time

    logger.info(f"Measuring latency for function {func.__name__}...")

    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    latency_ms = (end_time - start_time) * 1000 # Convert to milliseconds
    return result, latency_ms

def _parse_classification_response(response: str) -> ClassifierResponse:
    """
    Parses the classification response string into a ClassifierResponse object.
    Expects a JSON string with keys: provider, model, confidence.
    """
    import json

    logger.info(f"Parsing classification response...")
    logger.debug(f"Raw classification response: {response}")

    try:
        response = response.strip()
        response = response.replace("'", '"')  # Replace single quotes with double quotes for valid JSON
        response = response.replace('\n', '')  # Remove newlines
        response = response.replace(' ', '')  # Remove spaces
        response = response.replace("```json", '')  # Remove markdown json block if present
        response = response.replace("```", '')  # Remove markdown block if present
        response = response.lower()  # Convert to lowercase

        # Fix confidence formatting if necessary
        response = response.replace(r'"confidence":0+(\d\.\d+)', r'"confidence":\1')

        data = json.loads(response)

        return ClassifierResponse(
            provider=data.get("provider", ""),
            model=data.get("model", ""),
            confidence=float(data.get("confidence", 0.0))
        )
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse classification response: {e}")
        return ClassifierResponse(provider="", model="", confidence=0.0)

