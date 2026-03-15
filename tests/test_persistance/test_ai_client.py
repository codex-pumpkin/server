import importlib
import types

import pytest

from src.core.exceptions import (
    LLMAPIConnectionError,
    LLMAPIError,
    LLMAuthenticationError,
    LLMBadRequestError,
    LLMNotFoundError,
    LLMPermissionDeniedError,
    LLMRateLimitError,
)


ai_module = importlib.import_module("src.persistence.impl.llm.AIClient")
AIClient = ai_module.AIClient


@pytest.mark.asyncio
async def test_get_response_passes_expected_payload(monkeypatch):
    captured = {}

    async def fake_acompletion(**kwargs):
        captured.update(kwargs)
        return types.SimpleNamespace(
            choices=[types.SimpleNamespace(message=types.SimpleNamespace(content="netlist"))]
        )

    monkeypatch.setattr(ai_module.litellm, "acompletion", fake_acompletion)

    client = AIClient()
    response = await client.get_response(
        user_question="build an rc filter",
        retrieved_context="context block",
        conversation_history="previous chat",
        api_key="secret",
        model="custom-model",
        api_url="http://llm.local/v1",
    )

    assert response == "netlist"
    assert captured["model"] == "custom-model"
    assert captured["api_key"] == "secret"
    assert captured["api_base"] == "http://llm.local/v1"
    assert captured["messages"][0]["role"] == "system"
    assert "context block" in captured["messages"][1]["content"]
    assert "previous chat" in captured["messages"][1]["content"]
    assert "build an rc filter" in captured["messages"][1]["content"]


@pytest.mark.asyncio
async def test_regenerate_omits_api_base_when_not_provided(monkeypatch):
    captured = {}

    async def fake_acompletion(**kwargs):
        captured.update(kwargs)
        return types.SimpleNamespace(
            choices=[types.SimpleNamespace(message=types.SimpleNamespace(content="fixed netlist"))]
        )

    monkeypatch.setattr(ai_module.litellm, "acompletion", fake_acompletion)

    client = AIClient()
    response = await client.regenerate(
        user_question="fix the circuit",
        regeneration_context="ngspice output",
        code="* broken",
        api_key="secret",
        model="repair-model",
    )

    assert response == "fixed netlist"
    assert captured["api_base"] == "https://api.openai.com/v1"
    assert captured["model"] == "repair-model"
    assert "fix the circuit" in captured["messages"][1]["content"]
    assert "ngspice output" in captured["messages"][1]["content"]
    assert "* broken" in captured["messages"][1]["content"]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("name", "raised_exc", "expected_exc"),
    [
        ("AuthenticationError", Exception("auth"), LLMAuthenticationError),
        ("APIConnectionError", Exception("conn"), LLMAPIConnectionError),
        ("NotFoundError", Exception("missing"), LLMNotFoundError),
        ("BadRequestError", Exception("bad"), LLMBadRequestError),
        ("PermissionDeniedError", Exception("forbidden"), LLMPermissionDeniedError),
        ("APIError", Exception("api"), LLMAPIError),
        ("RateLimitError", Exception("rate"), LLMRateLimitError),
    ],
)
async def test_ai_client_maps_litellm_errors(monkeypatch, name, raised_exc, expected_exc):
    exception_types = {}

    for exc_name in (
        "AuthenticationError",
        "APIConnectionError",
        "NotFoundError",
        "BadRequestError",
        "PermissionDeniedError",
        "APIError",
        "RateLimitError",
    ):
        exception_types[exc_name] = type(exc_name, (Exception,), {})
        monkeypatch.setattr(ai_module.litellm, exc_name, exception_types[exc_name])

    async def raising_completion(**kwargs):
        raise exception_types[name](str(raised_exc))

    monkeypatch.setattr(ai_module.litellm, "acompletion", raising_completion)
    client = AIClient()

    with pytest.raises(expected_exc):
        await client.get_response("question", "context", "history", "key")

    with pytest.raises(expected_exc):
        await client.regenerate("question", "regen", "code", "key")
