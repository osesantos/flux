import os
from typing import Iterable
import openai
from openai.types.chat import ChatCompletionMessageParam
from src.config.config import GetLLMConfigByName
from src.model.openai_message_request import OpenAiMessageRequest
from src.model.openai_response import OpenAiChoice, OpenAiResponse
from loguru import logger

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def chat_completion(messages: list[OpenAiMessageRequest], max_tokens: int = 500, llm_name: str = "openai") -> OpenAiResponse:
    """
    Calls the OpenAI API to get a chat completion.
    """
    if not messages or len(messages) == 0:
        raise ValueError("At least one message must be provided")

    llm = GetLLMConfigByName(llm_name)

    logger.info(f"Generating chat completion model={llm_name}...")
    response = client.chat.completions.create(
        model=llm.model,
        messages=_parse_messages(messages),
        max_tokens=max_tokens
    )
    logger.info(f"Chat completion generation complete.")

    return _parse_response(response)


def _parse_messages(messages: list[OpenAiMessageRequest]) -> Iterable[ChatCompletionMessageParam]:
    """
    Converts a list of OpenAiMessageRequest objects to the format expected by the OpenAI API.
    """
    for msg in messages:
        yield {"role": msg.role, "content": msg.content} # type: ignore


def _parse_message_response(choice) -> OpenAiMessageRequest:
    """
    Parses the OpenAI API response into an OpenAiResponse object.
    """
    msg = choice.message
    return OpenAiMessageRequest(role=msg.role, content=msg.content)

def _parse_choice_response(choice) -> OpenAiChoice:
    """
    Parses the OpenAI API response into an OpenAiChoice object.
    """
    return OpenAiChoice(
        index=choice.index,
        message=_parse_message_response(choice),
        finish_reason=choice.finish_reason
    )

def _parse_response(response) -> OpenAiResponse:
    """
    Parses the OpenAI API response into an OpenAiResponse object.
    """
    logger.info(f"Parsing response...")
    return OpenAiResponse(
        id=response.id,
        object=response.object,
        created=response.created,
        model=response.model,
        choices=[_parse_choice_response(choice) for choice in response.choices],
    )

