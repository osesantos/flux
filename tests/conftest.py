import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_openai_client(monkeypatch):
    """Fixture to mock the OpenAI client across all tests."""
    from src.providers import openai

    mock = MagicMock()
    monkeypatch.setattr(openai, "client", mock)
    return mock


@pytest.fixture
def fake_openai_response():
    """Fixture to create a fake OpenAI response object for testing."""
    fake_choice = MagicMock()
    fake_choice.index = 0
    fake_choice.message.role = "assistant"
    fake_choice.message.content = "Hello from OpenAI!"
    fake_choice.finish_reason = "stop"

    fake_response = MagicMock()
    fake_response.id = "resp_123"
    fake_response.object = "chat.completion"
    fake_response.created = 123456789
    fake_response.model = "gpt-3.5-turbo"
    fake_response.choices = [fake_choice]
    fake_response.usage = {"prompt_tokens": 5, "completion_tokens": 7}

    return fake_response

