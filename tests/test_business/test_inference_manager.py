import datetime
import uuid
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from src.business.factory.BusinessFactory import BusinessFactory
from src.business.impl.inference.InferenceManager import InferenceManager
from src.core.dtos import (
    ConversationRequest,
    MessageRequest,
    MessageResponse,
    TargetLanguage,
    TokenModel,
    UpdateConversationRequest,
)
from src.core.dtos.validation_result import ValidationResult
from src.core.exceptions import AccessError, LLMRemovedError, NotFoundError, QuotaExceededError
from src.core.settings import settings
from src.persistence.factory.PersistenceFactory import PersistenceFactory


def _token() -> TokenModel:
    now = datetime.datetime.now(datetime.UTC)
    return TokenModel(
        sub=uuid.uuid4(),
        toc=now,
        exp=now + datetime.timedelta(minutes=10),
        is_admin=False,
    )


def _message_response(message: str) -> MessageResponse:
    return MessageResponse(
        id=str(uuid.uuid4()),
        message=message,
        generation_millis=5,
        response=f"response:{message}",
        graph="{}",
        created_at=datetime.datetime.now(datetime.UTC).replace(tzinfo=None).timestamp(),
    )


def _conversation(token: TokenModel, llm_id: str | None = "llm-1", messages=None):
    if messages is None:
        messages = [_message_response("first")]
    return SimpleNamespace(
        user_id=token.sub,
        llm_model_config_id=llm_id,
        messages=messages,
        pinned=False,
    )


@pytest.mark.asyncio
async def test_get_conversations_by_user_delegates_to_repository(monkeypatch):
    token = _token()
    repo = AsyncMock()
    repo.get_chats.return_value = ["chat"]

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(PersistenceFactory, "get_entity_repository", classmethod(fake_get_entity_repository))

    manager = InferenceManager()

    assert await manager.get_conversations_by_user(token) == ["chat"]
    repo.get_chats.assert_awaited_once_with(str(token.sub))


@pytest.mark.asyncio
async def test_post_message_to_conversation_rejects_quota_exceeded(monkeypatch):
    token = _token()
    repo = AsyncMock()
    repo.is_quota_exceeded.return_value = True

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(PersistenceFactory, "get_entity_repository", classmethod(fake_get_entity_repository))

    with pytest.raises(QuotaExceededError):
        await InferenceManager().post_message_to_conversation(uuid.uuid4(), MessageRequest(message="hi"), token)


@pytest.mark.asyncio
async def test_post_message_to_conversation_rejects_removed_llm(monkeypatch):
    token = _token()
    repo = AsyncMock()
    repo.is_quota_exceeded.return_value = False
    repo.get_chat_by_id.return_value = _conversation(token, llm_id=None)

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(PersistenceFactory, "get_entity_repository", classmethod(fake_get_entity_repository))

    with pytest.raises(LLMRemovedError):
        await InferenceManager().post_message_to_conversation(uuid.uuid4(), MessageRequest(message="hi"), token)


@pytest.mark.asyncio
async def test_post_message_to_conversation_persists_message_and_updates_name(monkeypatch):
    token = _token()
    conversation_id = uuid.uuid4()
    repo = AsyncMock()
    repo.is_quota_exceeded.return_value = False
    repo.get_chat_by_id.side_effect = [
        _conversation(token),
        _conversation(token),
    ]
    repo.get_messages.return_value = [_message_response("last")]

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(PersistenceFactory, "get_entity_repository", classmethod(fake_get_entity_repository))
    manager = InferenceManager()
    manager._get_message = AsyncMock(return_value=SimpleNamespace(response="* New Name", message="hi", graph="{}", generation_millis=12))
    manager._generate_conversation_name = AsyncMock(return_value="New Name")

    result = await manager.post_message_to_conversation(conversation_id, MessageRequest(message="hi"), token)

    assert result.message == "last"
    repo.add_message.assert_awaited_once()
    repo.update_chat.assert_awaited_once_with(chat_id=str(conversation_id), name="New Name", is_pinned=False)


@pytest.mark.asyncio
async def test_message_regeneration_replaces_last_message(monkeypatch):
    token = _token()
    conversation_id = uuid.uuid4()
    repo = AsyncMock()
    repo.is_quota_exceeded.return_value = False
    repo.get_chat_by_id.return_value = _conversation(token)
    repo.get_messages.return_value = [_message_response("replaced")]

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(PersistenceFactory, "get_entity_repository", classmethod(fake_get_entity_repository))
    manager = InferenceManager()
    manager._get_message = AsyncMock(return_value=SimpleNamespace(response="* Regenerated", message="hi", graph="{}", generation_millis=11))

    result = await manager.message_regeneration(conversation_id, MessageRequest(message="hi"), token)

    assert result.message == "replaced"
    repo.delete_last_message.assert_awaited_once_with(chat_id=str(conversation_id))
    repo.add_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_remove_conversation_checks_missing_and_access(monkeypatch):
    token = _token()
    repo = AsyncMock()
    repo.get_chat_by_id.return_value = None

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(PersistenceFactory, "get_entity_repository", classmethod(fake_get_entity_repository))
    manager = InferenceManager()

    with pytest.raises(NotFoundError):
        await manager.remove_conversation(uuid.uuid4(), token)

    repo.get_chat_by_id.return_value = SimpleNamespace(user_id=uuid.uuid4())

    with pytest.raises(AccessError):
        await manager.remove_conversation(uuid.uuid4(), token)


@pytest.mark.asyncio
async def test_remove_conversation_deletes_owned_conversation(monkeypatch):
    token = _token()
    conversation_id = uuid.uuid4()
    repo = AsyncMock()
    repo.get_chat_by_id.return_value = SimpleNamespace(user_id=token.sub)

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(PersistenceFactory, "get_entity_repository", classmethod(fake_get_entity_repository))

    await InferenceManager().remove_conversation(conversation_id, token)

    repo.delete_chat.assert_awaited_once_with(str(conversation_id))


@pytest.mark.asyncio
async def test_start_conversation_routes_between_guest_and_user_flows():
    manager = InferenceManager()
    request = ConversationRequest(
        message="hello",
        llm_model_config_id="llm-1",
        target_language=TargetLanguage("spice_netlist"),
        name="Draft",
    )

    manager._start_conversation_not_logged_in = AsyncMock(return_value="guest")
    manager._start_conversation = AsyncMock(return_value="user")

    assert await manager.start_conversation(None, request) == "guest"
    assert await manager.start_conversation(_token(), request) == "user"


@pytest.mark.asyncio
async def test_start_conversation_not_logged_in_builds_response(monkeypatch):
    repo = AsyncMock()
    repo.get_key_of_model.return_value = "api-key"
    repo.get_model.return_value = SimpleNamespace(model_name="gpt-test", api_url="http://llm")
    graph_generator = AsyncMock()
    graph_generator.gen_graph.return_value = '{"graph":true}'

    async def fake_get_entity_repository(cls):
        return repo

    async def fake_get_graph_generator(cls):
        return graph_generator

    monkeypatch.setattr(PersistenceFactory, "get_entity_repository", classmethod(fake_get_entity_repository))
    monkeypatch.setattr(PersistenceFactory, "get_graph_generator", classmethod(fake_get_graph_generator))

    manager = InferenceManager()
    manager._get_llm_response_and_validate = AsyncMock(return_value="* Auto Name\nR1 1 0 1k")
    manager._generate_conversation_name = AsyncMock(return_value="Auto Name")
    request = ConversationRequest(
        message="guest prompt",
        llm_model_config_id="llm-1",
        target_language=TargetLanguage("spice_netlist"),
        name="ignored",
    )

    response = await manager._start_conversation_not_logged_in(request)

    assert response.name == "Auto Name"
    assert response.messages[0].graph == '{"graph":true}'
    assert response.messages[0].response.startswith("* Auto Name")


@pytest.mark.asyncio
async def test_start_conversation_for_user_creates_chat_and_posts_message(monkeypatch):
    token = _token()
    chat_id = str(uuid.uuid4())
    repo = AsyncMock()
    repo.is_quota_exceeded.return_value = False
    repo.create_chat.return_value = chat_id
    repo.get_chat_by_id.return_value = "conversation"

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(PersistenceFactory, "get_entity_repository", classmethod(fake_get_entity_repository))
    manager = InferenceManager()
    manager.post_message_to_conversation = AsyncMock()
    request = ConversationRequest(
        message="hello",
        llm_model_config_id="llm-1",
        target_language=TargetLanguage("spice_netlist"),
        name="Draft",
    )

    result = await manager._start_conversation(token, request)

    assert result == "conversation"
    manager.post_message_to_conversation.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_conversation_checks_access_and_updates(monkeypatch):
    token = _token()
    conversation_id = uuid.uuid4()
    repo = AsyncMock()

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(PersistenceFactory, "get_entity_repository", classmethod(fake_get_entity_repository))
    manager = InferenceManager()
    request = UpdateConversationRequest(name="Renamed", pinned=True)

    repo.get_chat_by_id.return_value = None
    with pytest.raises(NotFoundError):
        await manager.update_conversation(conversation_id, request, token)

    repo.get_chat_by_id.return_value = SimpleNamespace(user_id=uuid.uuid4())
    with pytest.raises(AccessError):
        await manager.update_conversation(conversation_id, request, token)

    repo.get_chat_by_id.return_value = SimpleNamespace(user_id=token.sub)
    await manager.update_conversation(conversation_id, request, token)
    repo.update_chat.assert_awaited_once_with(
        chat_id=str(conversation_id),
        is_pinned=True,
        name="Renamed",
    )


@pytest.mark.asyncio
async def test_get_message_checks_chat_access(monkeypatch):
    token = _token()
    repo = AsyncMock()

    manager = InferenceManager()

    repo.get_chat_by_id.return_value = None
    with pytest.raises(NotFoundError):
        await manager._get_message(uuid.uuid4(), MessageRequest(message="hi"), token, repo)

    repo.get_chat_by_id.return_value = SimpleNamespace(user_id=uuid.uuid4(), messages=[])
    with pytest.raises(AccessError):
        await manager._get_message(uuid.uuid4(), MessageRequest(message="hi"), token, repo)


@pytest.mark.asyncio
async def test_get_message_builds_validated_message(monkeypatch):
    token = _token()
    conversation_id = uuid.uuid4()
    repo = AsyncMock()
    repo.get_chat_by_id.return_value = _conversation(token, messages=[_message_response("one"), _message_response("two")])
    repo.get_llm_by_chat_id.return_value = SimpleNamespace(api_key="key", model_name="model", api_url="http://llm")

    manager = InferenceManager()
    manager._get_llm_response_and_validate = AsyncMock(return_value="valid code")
    manager._get_graph_representation = AsyncMock(return_value='{"ok":true}')

    result = await manager._get_message(conversation_id, MessageRequest(message="next"), token, repo, remove_last=True)

    assert result.message == "next"
    assert result.response == "valid code"
    assert result.graph == '{"ok":true}'
    manager._get_llm_response_and_validate.assert_awaited_once_with(
        user_input="next",
        conversation_history=[("one", "response:one")],
        api_key="key",
        model="model",
        llm_url="http://llm",
    )


@pytest.mark.asyncio
async def test_get_llm_response_and_validate_handles_regeneration(monkeypatch):
    prompt_manager = AsyncMock()
    prompt_manager.retrieve_context.return_value = "docs"
    prompt_manager.get_conversation_context.return_value = "history"
    prompt_manager.make_regeneration_context.return_value = "retry context"
    validator = AsyncMock()
    validator.validate_code.side_effect = [
        ValidationResult(isValid=False, exitCode=1, rawOutput="bad"),
        ValidationResult(isValid=True, exitCode=0, rawOutput="ok"),
    ]
    ai_client = AsyncMock()
    ai_client.get_response.return_value = "```spice\nbad code\n```"
    ai_client.regenerate.return_value = "```spice\nfixed code\n```"

    async def fake_get_prompt_manager(cls):
        return prompt_manager

    async def fake_get_code_validator(cls):
        return validator

    async def fake_get_ai_client(cls):
        return ai_client

    monkeypatch.setattr(BusinessFactory, "get_prompt_manager", classmethod(fake_get_prompt_manager))
    monkeypatch.setattr(PersistenceFactory, "get_code_validator", classmethod(fake_get_code_validator))
    monkeypatch.setattr(PersistenceFactory, "get_ai_client", classmethod(fake_get_ai_client))

    result = await InferenceManager()._get_llm_response_and_validate("question", [("u", "a")], "key", "model", "http://llm")

    assert result == "fixed code"
    ai_client.regenerate.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_llm_response_and_validate_returns_failure_after_retries(monkeypatch):
    prompt_manager = AsyncMock()
    prompt_manager.retrieve_context.return_value = "docs"
    prompt_manager.get_conversation_context.return_value = "history"
    prompt_manager.make_regeneration_context.return_value = "retry context"
    validator = AsyncMock()
    validator.validate_code.side_effect = [
        ValidationResult(isValid=False, exitCode=1, rawOutput="bad"),
        ValidationResult(isValid=False, exitCode=1, rawOutput="still bad"),
    ]
    ai_client = AsyncMock()
    ai_client.get_response.return_value = "bad code"
    ai_client.regenerate.return_value = "still bad"

    async def fake_get_prompt_manager(cls):
        return prompt_manager

    async def fake_get_code_validator(cls):
        return validator

    async def fake_get_ai_client(cls):
        return ai_client

    monkeypatch.setattr(BusinessFactory, "get_prompt_manager", classmethod(fake_get_prompt_manager))
    monkeypatch.setattr(PersistenceFactory, "get_code_validator", classmethod(fake_get_code_validator))
    monkeypatch.setattr(PersistenceFactory, "get_ai_client", classmethod(fake_get_ai_client))

    original_retries = settings.llm_settings.num_of_regenerations
    settings.llm_settings.num_of_regenerations = 1
    try:
        result = await InferenceManager()._get_llm_response_and_validate("question", [], "key", "model", "http://llm")
    finally:
        settings.llm_settings.num_of_regenerations = original_retries

    assert result == "Failed to generate valid code after multiple attempts."


@pytest.mark.asyncio
async def test_clean_markdown_and_generate_name():
    manager = InferenceManager()

    assert await manager._clean_markdown("```spice\nR1 1 0 1k\n```") == "R1 1 0 1k"
    assert await manager._clean_markdown("plain") == "plain"
    assert await manager._generate_conversation_name("* My Circuit\nR1 1 0 1k") == "My Circuit"
