import asyncio
import datetime
import uuid
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from src.business.impl.auth.BasicAuthManager import BasicAuthManager
from src.business.impl.auth.tokens import decode_jwt
from src.core.dtos import (
    EmailVerificationSubmitRequest,
    LoginRequest,
    PasswordResetRequestRequest,
    PasswordResetSubmitRequest,
    RefreshRequest,
    SignupRequest,
    TokenInfo,
)
from src.core.exceptions import AuthError, VerificationError
from src.persistence import PersistenceFactory


def _token_info(
    token_type: str = "refresh",
    valid: bool = True,
    user_id: uuid.UUID | None = None,
    expires_delta_minutes: int = 30,
) -> TokenInfo:
    user_id = user_id or uuid.uuid4()
    now = datetime.datetime.now(datetime.UTC).replace(tzinfo=None)
    return TokenInfo(
        id=uuid.uuid4(),
        token_type=token_type,
        valid=valid,
        created_at=now,
        expires_at=now + datetime.timedelta(minutes=expires_delta_minutes),
        user_id=user_id,
    )


def _user_dto(user_id: uuid.UUID | None = None, verified: bool = True, is_admin: bool = False):
    user_id = user_id or uuid.uuid4()
    now = datetime.datetime.now(datetime.UTC).replace(tzinfo=None).timestamp()
    return SimpleNamespace(
        id=user_id,
        email="test@example.com",
        username="test-user",
        is_admin=is_admin,
        is_verified=verified,
        auth_via_google=False,
        created_at=now,
    )


def _patch_repo(monkeypatch, repo):
    async def _get_entity_repository(cls):
        return repo

    monkeypatch.setattr(
        PersistenceFactory, "get_entity_repository", classmethod(_get_entity_repository)
    )


def _patch_mail_sender(monkeypatch, sender):
    async def _get_mail_sender(cls):
        return sender

    monkeypatch.setattr(PersistenceFactory, "get_mail_sender", classmethod(_get_mail_sender))


def test_authenticate_success_returns_tokens(monkeypatch):
    repo = AsyncMock()
    user = _user_dto(verified=True)
    refresh = _token_info(token_type="refresh", user_id=user.id)
    repo.authenticate.return_value = user
    repo.create_token.return_value = refresh
    _patch_repo(monkeypatch, repo)

    manager = BasicAuthManager()
    request = LoginRequest(email=user.email, username=None, password="secret")

    result = asyncio.run(manager.authenticate(request))

    assert result.refresh_token == str(refresh.id)
    decoded = decode_jwt(result.access_token)
    assert decoded["sub"] == str(user.id)
    repo.invalidate_all_refresh_tokens.assert_awaited_once_with(str(user.id))
    repo.create_token.assert_awaited_once_with(str(user.id), "refresh")


def test_authenticate_raises_when_user_missing(monkeypatch):
    repo = AsyncMock()
    repo.authenticate.return_value = None
    _patch_repo(monkeypatch, repo)

    manager = BasicAuthManager()
    request = LoginRequest(email="missing@example.com", username=None, password="secret")

    with pytest.raises(AuthError):
        asyncio.run(manager.authenticate(request))


def test_authenticate_raises_when_user_not_verified(monkeypatch):
    repo = AsyncMock()
    repo.authenticate.return_value = _user_dto(verified=False)
    _patch_repo(monkeypatch, repo)

    manager = BasicAuthManager()
    request = LoginRequest(email="test@example.com", username=None, password="secret")

    with pytest.raises(AuthError):
        asyncio.run(manager.authenticate(request))


def test_refresh_access_token_success_includes_admin_claim(monkeypatch):
    repo = AsyncMock()
    user = _user_dto(is_admin=True)
    old_token = _token_info(token_type="refresh", user_id=user.id)
    new_token = _token_info(token_type="refresh", user_id=user.id)
    repo.get_token.return_value = old_token
    repo.change_token.return_value = new_token
    repo.get_user_by_id.return_value = user
    _patch_repo(monkeypatch, repo)

    manager = BasicAuthManager()
    request = RefreshRequest(refresh_token=old_token.id)

    result = asyncio.run(manager.refresh_access_token(request))

    decoded = decode_jwt(result.access_token)
    assert decoded["sub"] == str(user.id)
    assert decoded["is_admin"] is True
    assert result.refresh_token == str(old_token.id)


def test_refresh_access_token_rejects_wrong_token_type(monkeypatch):
    repo = AsyncMock()
    wrong_token = _token_info(token_type="email")
    repo.get_token.return_value = wrong_token
    _patch_repo(monkeypatch, repo)

    manager = BasicAuthManager()
    request = RefreshRequest(refresh_token=wrong_token.id)

    with pytest.raises(AuthError):
        asyncio.run(manager.refresh_access_token(request))


def test_verify_email_token_invalid_type_raises(monkeypatch):
    repo = AsyncMock()
    token = _token_info(token_type="password")
    repo.get_token.return_value = token
    _patch_repo(monkeypatch, repo)

    manager = BasicAuthManager()
    request = EmailVerificationSubmitRequest(verification_token=token.id)

    with pytest.raises(VerificationError):
        asyncio.run(manager.verify_email_token(request))


def test_initiate_password_recovery_sends_mail(monkeypatch):
    repo = AsyncMock()
    mail_sender = AsyncMock()
    user = _user_dto()
    token = _token_info(token_type="password", user_id=user.id)
    repo.get_user_by_email.return_value = user
    repo.create_token.return_value = token

    _patch_repo(monkeypatch, repo)
    _patch_mail_sender(monkeypatch, mail_sender)

    manager = BasicAuthManager()
    request = PasswordResetRequestRequest(email=user.email)
    asyncio.run(manager.initiate_password_recovery(request))

    mail_sender.send_password_reset_email.assert_awaited_once_with(user.email, str(token.id))


def test_complete_password_recovery_changes_password(monkeypatch):
    repo = AsyncMock()
    token = _token_info(token_type="password", user_id=uuid.uuid4())
    repo.get_token.return_value = token
    _patch_repo(monkeypatch, repo)

    manager = BasicAuthManager()
    request = PasswordResetSubmitRequest(reset_token=str(token.id), new_password="new-secret")
    asyncio.run(manager.complete_password_recovery(request))

    repo.invalidate_token.assert_awaited_once_with(str(token.id))
    repo.change_password.assert_awaited_once_with(str(token.user_id), "new-secret")


def test_register_creates_user_and_sends_verification(monkeypatch):
    repo = AsyncMock()
    user = _user_dto()
    repo.create_user.return_value = user
    _patch_repo(monkeypatch, repo)

    manager = BasicAuthManager()
    manager.generate_email_verification = AsyncMock()
    request = SignupRequest(email=user.email, username=user.username, password="secret")

    asyncio.run(manager.register(request))

    repo.create_user.assert_awaited_once_with(request)
    manager.generate_email_verification.assert_awaited_once_with(user)

