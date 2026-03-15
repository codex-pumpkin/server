import json
from datetime import datetime, UTC
from typing import Any, get_args, get_origin
from uuid import uuid4

import pytest

from src.core.dtos import (
    AccountResponse,
    ConversationRequest,
    ConversationResponse,
    EmailVerificationSubmitRequest,
    LLMConfigurationRequest,
    LLMConfigurationResponse,
    LoginRequest,
    Message,
    MessageRequest,
    MessageResponse,
    PasswordResetRequestRequest,
    PasswordResetSubmitRequest,
    QuotaConfig,
    RefreshRequest,
    SignupRequest,
    TargetLanguage,
    TokenResponse,
    UpdateAccountRequest,
    UpdateConversationRequest,
)
from src.core.dtos.analytics_response import AnalyticsResponse
from src.core.dtos.google_login_request import GoogleLoginRequest


GENERATED_MODELS = [
    LoginRequest,
    SignupRequest,
    RefreshRequest,
    UpdateAccountRequest,
    UpdateConversationRequest,
    ConversationRequest,
    MessageRequest,
    Message,
    MessageResponse,
    TokenResponse,
    QuotaConfig,
    PasswordResetRequestRequest,
    PasswordResetSubmitRequest,
    EmailVerificationSubmitRequest,
    GoogleLoginRequest,
    LLMConfigurationRequest,
    LLMConfigurationResponse,
]

MODEL_OVERRIDES = {
    LLMConfigurationResponse: {"api_key_set": True},
}


def _unwrap(annotation: Any) -> Any:
    origin = get_origin(annotation)
    if origin is None:
        return annotation
    args = [arg for arg in get_args(annotation) if arg is not type(None)]
    if origin in (list, tuple, dict) or origin is tuple:
        return annotation
    if len(args) == 1:
        return _unwrap(args[0])
    return annotation


def _sample_value(annotation: Any) -> Any:
    annotation = _unwrap(annotation)
    origin = get_origin(annotation)

    if origin is list:
        return [_sample_value(get_args(annotation)[0])]
    if origin is dict:
        return {"key": "value"}
    if annotation is str or "StrictStr" in str(annotation):
        return "value"
    if annotation is int or "StrictInt" in str(annotation):
        return 123
    if annotation is float:
        return 12.5
    if annotation is bool or "StrictBool" in str(annotation):
        return True
    if annotation is datetime:
        return datetime.now(UTC).isoformat()
    if hasattr(annotation, "__mro__") and any(cls.__name__ == "UUID" for cls in annotation.__mro__):
        return str(uuid4())
    if hasattr(annotation, "__mro__") and any(cls.__name__ == "Enum" for cls in annotation.__mro__):
        return list(annotation)[0].value
    return "value"


def _build_payload(model_cls):
    payload = {}
    for name, field in model_cls.model_fields.items():
        if not field.is_required():
            payload[name] = _sample_value(field.annotation)
            continue
        payload[name] = _sample_value(field.annotation)
    return payload


@pytest.mark.parametrize("model_cls", GENERATED_MODELS)
def test_generated_dto_round_trip_methods(model_cls):
    payload = _build_payload(model_cls)
    payload.update(MODEL_OVERRIDES.get(model_cls, {}))
    instance = model_cls.from_dict(payload)

    assert instance is not None
    assert isinstance(instance.to_str(), str)
    assert instance.to_dict()
    if model_cls in {RefreshRequest, EmailVerificationSubmitRequest, LLMConfigurationResponse}:
        with pytest.raises(TypeError):
            instance.to_json()
    else:
        assert model_cls.from_json(instance.to_json()).model_dump() == instance.model_dump()
    assert model_cls.from_dict(None) is None
    assert model_cls.from_dict(instance).model_dump() == instance.model_dump()


def test_target_language_from_json():
    assert TargetLanguage.from_json(json.dumps("java")) is TargetLanguage.JAVA


def test_analytics_response_helpers():
    usage = [1] * 96
    payload = {
        "start_time": datetime.now(UTC).isoformat(),
        "interval_minutes": 15,
        "usage": usage,
    }

    model = AnalyticsResponse.from_dict(payload)

    assert AnalyticsResponse.validate_usage_length(usage) == usage
    assert "start_time" in model.to_str()
    assert AnalyticsResponse.from_json(model.to_json()).usage == usage
    assert AnalyticsResponse.from_dict(model).usage == usage
    assert AnalyticsResponse.from_dict(None) is None

    with pytest.raises(ValueError):
        AnalyticsResponse.validate_usage_length([1, 2, 3])

    with pytest.raises(ValueError):
        AnalyticsResponse.validate_usage_length([0] * 95 + [-1])


def test_account_response_nested_conversion(monkeypatch):
    llm = LLMConfigurationResponse(
        id=uuid4(),
        name="cfg",
        model_name="gpt",
        api_url="http://api",
        api_key_set=True,
    )
    model = AccountResponse.model_construct(
        id=uuid4(),
        email="user@example.com",
        username="user",
        is_admin=False,
        is_verified=True,
        auth_via_google=False,
        created_at=1.0,
    )
    object.__setattr__(model, "llm_configurations", [llm])

    as_dict = model.to_dict()

    assert as_dict["llm_configurations"][0]["name"] == "cfg"
    with pytest.raises(TypeError):
        model.to_json()
    assert AccountResponse.from_dict(None) is None

    captured = {}
    monkeypatch.setattr(AccountResponse, "model_validate", classmethod(lambda cls, payload: captured.setdefault("payload", payload) or payload))
    monkeypatch.setattr(LLMConfigurationResponse, "from_dict", classmethod(lambda cls, payload: {"converted": payload["name"]}))

    result = AccountResponse.from_dict(
        {
            "id": str(uuid4()),
            "email": "user@example.com",
            "username": "user",
            "is_admin": False,
            "is_verified": True,
            "auth_via_google": False,
            "created_at": 1.0,
            "llm_configurations": [{"name": "cfg"}],
        }
    )

    assert result["llm_configurations"] == [{"converted": "cfg"}]


def test_conversation_response_nested_conversion(monkeypatch):
    message = MessageResponse(
        id="m1",
        message="hello",
        generation_millis=5,
        response="world",
        graph="graph",
        simulation_result="ok",
        created_at=1.0,
    )
    model = ConversationResponse.model_construct(
        id=uuid4(),
        name="chat",
        pinned=True,
        llm_model_config_id="cfg",
        created_at=1.0,
        updated_at=2.0,
        target_language=TargetLanguage.JAVA,
        user_id=uuid4(),
        messages=[message],
    )

    as_dict = model.to_dict()

    assert as_dict["messages"][0]["message"] == "hello"
    with pytest.raises(TypeError):
        model.to_json()
    assert ConversationResponse.from_dict(None) is None

    captured = {}
    monkeypatch.setattr(ConversationResponse, "model_validate", classmethod(lambda cls, payload: captured.setdefault("payload", payload) or payload))
    monkeypatch.setattr(MessageResponse, "from_dict", classmethod(lambda cls, payload: {"converted": payload["id"]}))

    result = ConversationResponse.from_dict(
        {
            "id": str(uuid4()),
            "name": "chat",
            "pinned": True,
            "llm_model_config_id": "cfg",
            "created_at": 1.0,
            "updated_at": 2.0,
            "target_language": "java",
            "user_id": str(uuid4()),
            "messages": [{"id": "m1"}],
        }
    )

    assert result["messages"] == [{"converted": "m1"}]
