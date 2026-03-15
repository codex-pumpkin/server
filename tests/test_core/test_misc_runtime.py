import runpy
import types

import pytest

from src.business.factory.BusinessFactory import BusinessFactory
from src.business.interfaces import (
    IBasicAuthManager,
    IInferenceManager,
    IPromptManager,
    ISystemManager,
    IUserInfoManager,
)
from src.persistence.impl.database.database import Base
from src.persistence.impl.database.hash_util import hash_password, validate_password
from src.persistence.impl.database.model_types import generate_code


@pytest.mark.asyncio
async def test_business_factory_getters_return_singletons():
    BusinessFactory._singletons.clear()

    inference = await BusinessFactory.get_inference_manager()
    system = await BusinessFactory.get_system_manager()
    auth = await BusinessFactory.get_basic_auth_manager()
    user_info = await BusinessFactory.get_user_info_manager()
    prompt = await BusinessFactory.get_prompt_manager()

    assert isinstance(inference, IInferenceManager)
    assert isinstance(system, ISystemManager)
    assert isinstance(auth, IBasicAuthManager)
    assert isinstance(user_info, IUserInfoManager)
    assert isinstance(prompt, IPromptManager)
    assert inference is await BusinessFactory.get_inference_manager()


def test_hash_util_and_model_types_helpers():
    hashed = hash_password("password")

    assert hashed != "password"
    assert validate_password(hashed, "password") is True
    assert validate_password(hashed, "wrong") is False

    code = generate_code()
    assert len(code) == 6
    assert code.isdigit()


def test_base_repr_uses_first_columns_and_selected_columns():
    model = types.SimpleNamespace(
        __table__=types.SimpleNamespace(columns=types.SimpleNamespace(keys=lambda: ["id", "name", "secret", "visible"])),
        __class__=types.SimpleNamespace(__name__="FakeModel"),
        repr_first_cols=2,
        repr_cols=("visible",),
        id="1",
        name="demo",
        secret="hidden",
        visible="shown",
    )

    rendered = Base.__repr__(model)

    assert "id=1" in rendered
    assert "name=demo" in rendered
    assert "visible=shown" in rendered
    assert "secret=hidden" not in rendered


def test_main_entrypoint_runs_startup(monkeypatch):
    created = []
    init_calls = []
    uvicorn_calls = []

    monkeypatch.setattr("src.persistence.impl.database.orm.create_tables", lambda: created.append(True))
    monkeypatch.setattr("src.persistence.impl.chroma_database.initDB.init_db", lambda: init_calls.append(True))
    monkeypatch.setattr("uvicorn.run", lambda *args, **kwargs: uvicorn_calls.append((args, kwargs)))
    monkeypatch.setattr("os.makedirs", lambda path, exist_ok=False: created.append(path))

    runpy.run_module("src.main", run_name="__main__")

    assert True in created
    assert init_calls == [True]
    assert uvicorn_calls[0][0] == ("src.service.main:app",)
    assert uvicorn_calls[0][1]["port"] == 8000
