from src.providers import openai
from src.model import OpenAiMessageRequest, OpenAiResponse, OpenAiChoice


def test_chat_completion_parses_response(mock_openai_client, fake_openai_response):
    # Arrange
    mock_openai_client.chat.completions.create.return_value = fake_openai_response
    messages = [OpenAiMessageRequest(role="user", content="Hi!")]

    # Act
    result: OpenAiResponse = openai.chat_completion(messages, model="gpt-3.5-turbo")

    # Assert
    assert isinstance(result, OpenAiResponse)
    assert result.id == "resp_123"
    assert result.model == "gpt-3.5-turbo"
    assert len(result.choices) == 1

    choice: OpenAiChoice = result.choices[0]
    assert choice.message.role == "assistant"
    assert choice.message.content == "Hello from OpenAI!"
    assert choice.finish_reason == "stop"


def test_parse_messages():
    messages = [
        OpenAiMessageRequest(role="user", content="Hello"),
        OpenAiMessageRequest(role="system", content="You are a bot."),
    ]
    parsed = list(openai._parse_messages(messages))

    assert parsed == [
        {"role": "user", "content": "Hello"},
        {"role": "system", "content": "You are a bot."},
    ]

