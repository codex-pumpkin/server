from unittest.mock import AsyncMock

import pytest

from src.business.factory.BusinessFactory import BusinessFactory
from src.service import dependencies
from src.service.main import app


@pytest.mark.asyncio
async def test_dependencies_return_factory_instances(monkeypatch):
    inference = object()
    system = object()
    auth = object()
    user_info = object()

    async def fake_get_inference_manager(cls):
        return inference

    async def fake_get_system_manager(cls):
        return system

    async def fake_get_basic_auth_manager(cls):
        return auth

    async def fake_get_user_info_manager(cls):
        return user_info

    monkeypatch.setattr(BusinessFactory, "get_inference_manager", classmethod(fake_get_inference_manager))
    monkeypatch.setattr(BusinessFactory, "get_system_manager", classmethod(fake_get_system_manager))
    monkeypatch.setattr(BusinessFactory, "get_basic_auth_manager", classmethod(fake_get_basic_auth_manager))
    monkeypatch.setattr(BusinessFactory, "get_user_info_manager", classmethod(fake_get_user_info_manager))

    assert await dependencies.get_inference_manager() is inference
    assert await dependencies.get_system_manager() is system
    assert await dependencies.get_auth_manager() is auth
    assert await dependencies.get_user_info_manager() is user_info


def test_service_app_registers_expected_routes_and_metadata():
    paths = {route.path for route in app.routes}

    assert app.title == "CodeX - REST API"
    assert "/auth/login" in paths
    assert "/account" in paths
    assert "/conversations" in paths
    assert "/llm-configurations" in paths
    assert "/quota" in paths
    assert "/analytics" in paths
