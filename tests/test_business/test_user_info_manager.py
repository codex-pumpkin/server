import datetime
import uuid
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from src.business.factory.BusinessFactory import BusinessFactory
from src.business.impl.userinfo.UserInfoManager import UserInfoManager
from src.core.dtos import TokenModel, UpdateAccountRequest
from src.core.settings import settings
from src.persistence.factory.PersistenceFactory import PersistenceFactory


def _token() -> TokenModel:
    now = datetime.datetime.now(datetime.UTC)
    return TokenModel(
        sub=uuid.uuid4(),
        toc=now,
        exp=now + datetime.timedelta(minutes=5),
        is_admin=False,
    )


def _user(user_id: uuid.UUID, email: str = "old@example.com"):
    return SimpleNamespace(id=user_id, email=email, username="old-name")


@pytest.mark.asyncio
async def test_get_account_info_loads_current_user(monkeypatch):
    token = _token()
    repo = AsyncMock()
    repo.get_user_by_id.return_value = "account"

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(
        PersistenceFactory,
        "get_entity_repository",
        classmethod(fake_get_entity_repository),
    )

    manager = UserInfoManager()

    assert await manager.get_account_info(token) == "account"
    repo.get_user_by_id.assert_awaited_once_with(str(token.sub))


@pytest.mark.asyncio
async def test_update_user_name_email_without_email_change_updates_only(monkeypatch):
    token = _token()
    repo = AsyncMock()
    repo.get_user_by_id.return_value = _user(token.sub, email="same@example.com")

    async def fake_get_entity_repository(cls):
        return repo

    async def fake_get_basic_auth_manager(cls):
        raise AssertionError("auth manager should not be loaded")

    monkeypatch.setattr(
        PersistenceFactory,
        "get_entity_repository",
        classmethod(fake_get_entity_repository),
    )
    monkeypatch.setattr(
        BusinessFactory,
        "get_basic_auth_manager",
        classmethod(fake_get_basic_auth_manager),
    )

    manager = UserInfoManager()
    request = UpdateAccountRequest(email="same@example.com", username="new-name")

    await manager.update_user_name_email(token, request)

    repo.update_user.assert_awaited_once_with(
        user_id=str(token.sub),
        email="same@example.com",
        username="new-name",
    )
    repo.invalidate_all_refresh_tokens.assert_not_called()
    repo.unverify_user.assert_not_called()


@pytest.mark.asyncio
async def test_update_user_name_email_with_email_change_revokes_tokens(monkeypatch):
    token = _token()
    repo = AsyncMock()
    auth_manager = AsyncMock()
    repo.get_user_by_id.side_effect = [
        _user(token.sub, email="old@example.com"),
        _user(token.sub, email="new@example.com"),
    ]

    async def fake_get_entity_repository(cls):
        return repo

    async def fake_get_basic_auth_manager(cls):
        return auth_manager

    monkeypatch.setattr(
        PersistenceFactory,
        "get_entity_repository",
        classmethod(fake_get_entity_repository),
    )
    monkeypatch.setattr(
        BusinessFactory,
        "get_basic_auth_manager",
        classmethod(fake_get_basic_auth_manager),
    )

    manager = UserInfoManager()
    request = UpdateAccountRequest(email="new@example.com", username="new-name")

    await manager.update_user_name_email(token, request)

    repo.invalidate_all_refresh_tokens.assert_awaited_once_with(user_id=str(token.sub))
    repo.unverify_user.assert_awaited_once_with(user_id=str(token.sub))
    auth_manager.generate_email_verification.assert_awaited_once_with(token.sub, "new@example.com")


@pytest.mark.asyncio
async def test_profile_picture_roundtrip(monkeypatch):
    token = _token()
    temp_dir = Path(__file__).resolve().parent.parent / "_tmp_user_info"
    temp_dir.mkdir(exist_ok=True)
    original_path = settings.pictures_settings.path
    settings.pictures_settings.path = str(temp_dir)

    try:
        manager = UserInfoManager()

        assert await manager.get_profile_picture(token) is None

        await manager.update_profile_picture(token, b"image-bytes")

        expected_path = temp_dir / f"{token.sub}.jpg"
        assert expected_path.read_bytes() == b"image-bytes"
        assert await manager.get_profile_picture(token) == b"image-bytes"
    finally:
        settings.pictures_settings.path = original_path
