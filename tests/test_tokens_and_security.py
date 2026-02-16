import uuid

import pytest
from fastapi import HTTPException

from src.business.impl.auth.tokens import check_if_jwt_valid, decode_jwt, encode_jwt
from src.service.security_api import get_token_jwt


def test_encode_decode_jwt_roundtrip():
    payload = {"sub": str(uuid.uuid4()), "is_admin": True}
    encoded = encode_jwt(payload)
    decoded = decode_jwt(encoded)

    assert decoded["sub"] == payload["sub"]
    assert decoded["is_admin"] is True
    assert "exp" in decoded


def test_check_if_jwt_valid_false_for_garbage():
    assert check_if_jwt_valid("not-a-jwt") is False


def test_get_token_jwt_returns_token_model_for_valid_header_token():
    payload = {"sub": str(uuid.uuid4()), "is_admin": False}
    token = encode_jwt(payload)

    token_data = get_token_jwt(access_token=token)
    assert token_data.sub == uuid.UUID(payload["sub"])
    assert token_data.is_admin is False


def test_get_token_jwt_raises_401_for_invalid_token():
    with pytest.raises(HTTPException) as exc:
        get_token_jwt(access_token="bad-token")

    assert exc.value.status_code == 401

