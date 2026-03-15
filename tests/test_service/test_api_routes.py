import datetime
import uuid
from pathlib import Path
from unittest.mock import AsyncMock

import pytest

from src.core.dtos import (
    AccountResponse,
    AnalyticsRequest,
    AnalyticsResponse,
    ConversationRequest,
    LLMConfigurationRequest,
    MessageRequest,
    QuotaConfig,
    RefreshRequest,
    SignupRequest,
    TargetLanguage,
    TokenModel,
    TokenResponse,
    UpdateAccountRequest,
    UpdateConversationRequest,
)
from src.core.dtos.google_login_request import GoogleLoginRequest
from src.core.settings import settings
from src.service.apis import account_api, analytics_api, authentication_api, conversations_api, llm_api, quota_api


def _token(admin: bool = False) -> TokenModel:
    now = datetime.datetime.now(datetime.UTC)
    return TokenModel(
        sub=uuid.uuid4(),
        toc=now,
        exp=now + datetime.timedelta(minutes=5),
        is_admin=admin,
    )


def _conversation_request() -> ConversationRequest:
    return ConversationRequest(
        message="hello",
        llm_model_config_id="llm-1",
        target_language=TargetLanguage("spice_netlist"),
        name="Draft",
    )


@pytest.mark.asyncio
async def test_authentication_routes_delegate_to_manager(monkeypatch):
    manager = AsyncMock()
    token = TokenResponse(access_token="access", refresh_token=str(uuid.uuid4()))
    manager.authenticate.return_value = token
    manager.refresh_access_token.return_value = token
    manager.google_callback.return_value = token

    login_request = await authentication_api.auth_login_post(
        login_request=authentication_api.LoginRequest(email="user@example.com", username=None, password="secret"),
        auth_manager=manager,
    )
    signup_request = SignupRequest(email="user@example.com", username="user", password="secret")
    refresh_request = RefreshRequest(refresh_token=uuid.uuid4())

    assert login_request == token
    await authentication_api.auth_signup_post(signup_request, manager)
    assert await authentication_api.auth_refresh_post(refresh_request, manager) == token
    await authentication_api.auth_logout_post(refresh_token=uuid.uuid4(), token_jwt=_token(), auth_manager=manager)
    await authentication_api.auth_request_password_reset_post(
        authentication_api.PasswordResetRequestRequest(email="user@example.com"),
        manager,
    )
    await authentication_api.auth_submit_password_reset_post(
        authentication_api.PasswordResetSubmitRequest(reset_token=str(uuid.uuid4()), new_password="new-secret"),
        manager,
    )
    await authentication_api.auth_submit_email_verification_post(
        authentication_api.EmailVerificationSubmitRequest(verification_token=uuid.uuid4()),
        manager,
    )

    manager.register.assert_awaited_once_with(signup_request)
    manager.user_logout.assert_awaited_once()
    manager.initiate_password_recovery.assert_awaited_once()
    manager.complete_password_recovery.assert_awaited_once()
    manager.verify_email_token.assert_awaited_once()


@pytest.mark.asyncio
async def test_google_callback_exchanges_tokens_and_calls_manager(monkeypatch):
    manager = AsyncMock()
    manager.google_callback.return_value = TokenResponse(access_token="app-access", refresh_token=str(uuid.uuid4()))

    class FakeResponse:
        def __init__(self, status_code, payload):
            self.status_code = status_code
            self._payload = payload

        def json(self):
            return self._payload

    class FakeAsyncClient:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            return False

        async def post(self, url, data):
            return FakeResponse(200, {"access_token": "google-access"})

        async def get(self, url, headers):
            return FakeResponse(200, {"name": "Test User", "email": "user@example.com", "picture": "http://img"})

    monkeypatch.setattr(authentication_api.httpx, "AsyncClient", FakeAsyncClient)

    result = await authentication_api.google_callback(GoogleLoginRequest(id_token="google-code"), manager)

    assert result.access_token == "app-access"
    manager.google_callback.assert_awaited_once_with(
        username="Test User",
        email="user@example.com",
        picture="http://img",
    )


@pytest.mark.asyncio
async def test_account_routes_delegate_and_handle_pictures():
    token = _token()
    manager = AsyncMock()
    account = AccountResponse(
        id=token.sub,
        email="user@example.com",
        username="user",
        is_admin=False,
        is_verified=True,
        auth_via_google=False,
        created_at=1.0,
    )
    manager.get_account_info.return_value = account
    manager.get_profile_picture.return_value = b"jpeg-data"

    temp_dir = Path(__file__).resolve().parent.parent / "_tmp_service_account"
    temp_dir.mkdir(exist_ok=True)
    original_path = settings.pictures_settings.path
    settings.pictures_settings.path = str(temp_dir)
    try:
        assert await account_api.account_get(token, manager) == account

        await account_api.account_put(UpdateAccountRequest(email="new@example.com", username="new"), token, manager)

        response = await account_api.account_profile_picture_get(token, manager)
        assert response.media_type == "image/jpeg"
        assert await response.body_iterator.__anext__() == b"jpeg-data"

        class FakeUpload:
            async def read(self):
                return b"file-bytes"

        await account_api.account_profile_picture_put(FakeUpload(), token, manager)
        assert (temp_dir / f"{token.sub}.jpg").read_bytes() == b"file-bytes"
        manager.update_profile_picture.assert_awaited_once_with(token, b"file-bytes")
    finally:
        settings.pictures_settings.path = original_path


@pytest.mark.asyncio
async def test_account_picture_get_returns_none_when_missing():
    manager = AsyncMock()
    manager.get_profile_picture.return_value = None

    assert await account_api.account_profile_picture_get(_token(), manager) is None


@pytest.mark.asyncio
async def test_conversation_routes_delegate_to_inference_manager():
    token = _token()
    manager = AsyncMock()
    conversation_id = uuid.uuid4()
    request = _conversation_request()
    message_request = MessageRequest(message="next")
    update_request = UpdateConversationRequest(name="Updated", pinned=True)
    manager.get_conversations_by_user.return_value = ["chat"]
    manager.start_conversation.return_value = "started"
    manager.message_regeneration.return_value = "regenerated"
    manager.post_message_to_conversation.return_value = "posted"

    assert await conversations_api.conversations_get(token, manager) == ["chat"]
    assert await conversations_api.conversations_post(request, token, manager) == "started"
    await conversations_api.conversations_id_put(conversation_id, update_request, token, manager)
    await conversations_api.conversations_id_delete(conversation_id, token, manager)
    assert await conversations_api.conversations_id_messages_put(conversation_id, message_request, token, manager) == "regenerated"
    assert await conversations_api.conversations_id_messages_post(conversation_id, message_request, token, manager) == "posted"

    manager.update_conversation.assert_awaited_once()
    manager.remove_conversation.assert_awaited_once()


@pytest.mark.asyncio
async def test_llm_quota_and_analytics_routes_delegate():
    system_manager = AsyncMock()
    llm_request = LLMConfigurationRequest(
        name="Primary",
        model_name="gpt-4.1",
        api_url="http://llm",
        api_key="secret",
    )
    quota = QuotaConfig(member=10, admin=100)
    analytics_request = AnalyticsRequest(period_of_days=7, time_interval_minutes=30)
    analytics = AnalyticsResponse(
        start_time=datetime.datetime.now(datetime.UTC).replace(tzinfo=None),
        interval_minutes=30,
        usage=[0] * 96,
    )
    system_manager.get_llm_configs.return_value = ["cfg"]
    system_manager.get_quota_settings.return_value = quota
    system_manager.get_analytics.return_value = analytics

    assert await llm_api.llm_configurations_get(system_manager) == ["cfg"]
    await llm_api.llm_configurations_post(llm_request, _token(admin=True), system_manager)
    await llm_api.llm_configurations_id_put(uuid.uuid4(), llm_request, _token(admin=True), system_manager)
    await llm_api.llm_configurations_id_delete(uuid.uuid4(), _token(admin=True), system_manager)

    assert await quota_api.quota_get(system_manager, _token()) == quota
    await quota_api.quota_put(quota, _token(admin=True), system_manager)
    assert await analytics_api.analytics_get(analytics_request, _token(admin=True), system_manager) == analytics

    system_manager.validate_and_persist_llm_config.assert_awaited_once()
    system_manager.update_llm_config.assert_awaited_once()
    system_manager.process_llm_removal.assert_awaited_once()
    system_manager.apply_quota_adjustment.assert_awaited_once_with(quota_config=quota)
