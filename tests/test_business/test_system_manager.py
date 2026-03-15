import datetime
import uuid
from unittest.mock import AsyncMock

import pytest

from src.business.impl.system.SystemManager import SystemManager
from src.core.dtos import AnalyticsRequest, LLMConfigurationRequest, QuotaConfig
from src.core.exceptions import NotFoundError
from src.persistence.factory.PersistenceFactory import PersistenceFactory


def _llm_request() -> LLMConfigurationRequest:
    return LLMConfigurationRequest(
        name="Primary",
        model_name="gpt-4.1",
        api_url="http://llm.local",
        api_key="secret",
    )


@pytest.mark.asyncio
async def test_system_manager_delegates_to_repository(monkeypatch):
    repo = AsyncMock()
    quota = QuotaConfig(member=5, admin=50)
    analytics = {"usage": [0]}
    request = _llm_request()
    llm_id = uuid.uuid4()

    repo.get_llm_configs.return_value = ["config"]
    repo.get_quota.return_value = quota
    repo.get_usage_data.return_value = analytics
    repo.get_model.return_value = object()

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(
        PersistenceFactory,
        "get_entity_repository",
        classmethod(fake_get_entity_repository),
    )

    manager = SystemManager()

    assert await manager.get_llm_configs() == ["config"]
    assert await manager.get_quota_settings() == quota
    assert await manager.get_analytics(AnalyticsRequest(period_of_days=7, time_interval_minutes=30)) == analytics

    await manager.apply_quota_adjustment(quota)
    await manager.validate_and_persist_llm_config(request)
    await manager.update_llm_config(llm_id, request)
    await manager.process_llm_removal(llm_id)

    repo.change_quota.assert_awaited_once_with(quota)
    repo.add_model.assert_awaited_once_with(
        name=request.name,
        url=request.api_url,
        key=request.api_key,
        model_name=request.model_name,
    )
    repo.change_model.assert_awaited_once_with(
        model_id=str(llm_id),
        name=request.name,
        url=request.api_url,
        key=request.api_key,
        model_name=request.model_name,
    )
    repo.remove_model.assert_awaited_once_with(model_id=str(llm_id))


@pytest.mark.asyncio
async def test_update_llm_config_raises_when_model_missing(monkeypatch):
    repo = AsyncMock()
    repo.get_model.return_value = None

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(
        PersistenceFactory,
        "get_entity_repository",
        classmethod(fake_get_entity_repository),
    )

    manager = SystemManager()

    with pytest.raises(NotFoundError):
        await manager.update_llm_config(uuid.uuid4(), _llm_request())


@pytest.mark.asyncio
async def test_process_llm_removal_raises_when_model_missing(monkeypatch):
    repo = AsyncMock()
    repo.get_model.return_value = None

    async def fake_get_entity_repository(cls):
        return repo

    monkeypatch.setattr(
        PersistenceFactory,
        "get_entity_repository",
        classmethod(fake_get_entity_repository),
    )

    manager = SystemManager()

    with pytest.raises(NotFoundError):
        await manager.process_llm_removal(uuid.uuid4())
