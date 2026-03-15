from unittest.mock import AsyncMock

import pytest

from src.business.impl.prompt.PromptManager import PromptManager
from src.persistence.factory.PersistenceFactory import PersistenceFactory


@pytest.mark.asyncio
async def test_retrieve_context_joins_chunks(monkeypatch):
    repo = AsyncMock()
    repo.get_similar_chunks.return_value = ["chunk one", "chunk two"]

    async def fake_get_semantic_repository(cls):
        return repo

    monkeypatch.setattr(
        PersistenceFactory,
        "get_semantic_repository",
        classmethod(fake_get_semantic_repository),
    )

    manager = PromptManager()

    result = await manager.retrieve_context("prompt", top_k=2)

    assert result == "chunk one\nchunk two"
    repo.get_similar_chunks.assert_awaited_once_with("prompt", 2)


def test_make_regeneration_context_includes_exit_code_and_output():
    manager = PromptManager()

    result = manager.make_regeneration_context(7, "bad node")

    assert "7" in result
    assert "bad node" in result


def test_get_conversation_context_formats_history():
    manager = PromptManager()

    assert manager.get_conversation_context([]) == ""
    assert manager.get_conversation_context([("hello", "world")]) == (
        "Conversation history:\nUser: hello\nAI: world\n"
    )
