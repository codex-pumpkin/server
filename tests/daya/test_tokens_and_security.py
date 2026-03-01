import uuid

import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from src.business.impl.auth.tokens import check_if_jwt_valid, decode_jwt, encode_jwt
from src.service.security_api import (
    get_token_jwt,
    get_token_jwt_mandatory,
    get_token_jwt_mandatory_admin,
)


def test_encode_decode_jwt_roundtrip():
    """Test encode decode jwt roundtrip."""
    payload = {"sub": str(uuid.uuid4()), "is_admin": True}
    encoded = encode_jwt(payload)
    decoded = decode_jwt(encoded)

    assert decoded["sub"] == payload["sub"]
    assert decoded["is_admin"] is True
    assert "exp" in decoded


def test_check_if_jwt_valid_false_for_garbage():
    """Test check if jwt valid false for garbage."""
    assert check_if_jwt_valid("not-a-jwt") is False


def test_get_token_jwt_returns_token_model_for_valid_header_token():
    """Test get token jwt returns token model for valid header token."""
    payload = {"sub": str(uuid.uuid4()), "is_admin": False}
    token = encode_jwt(payload)
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)

    token_data = get_token_jwt(access_token=credentials)
    assert token_data.sub == uuid.UUID(payload["sub"])
    assert token_data.is_admin is False


def test_get_token_jwt_raises_401_for_invalid_token():
    """Test get token jwt raises 401 for invalid token."""
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials="bad-token")
    with pytest.raises(HTTPException) as exc:
        get_token_jwt(access_token=credentials)

    assert exc.value.status_code == 401


def test_get_token_jwt_mandatory_raises_401_when_missing():
    """Test get token jwt mandatory raises 401 when missing."""
    with pytest.raises(HTTPException) as exc:
        get_token_jwt_mandatory(access_token=None)

    assert exc.value.status_code == 401
    assert "logging in is required" in exc.value.detail


def test_get_token_jwt_mandatory_admin_returns_token_for_admin():
    """Test get token jwt mandatory admin returns token for admin."""
    payload = {"sub": str(uuid.uuid4()), "is_admin": True}
    token = encode_jwt(payload)
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)

    token_data = get_token_jwt_mandatory_admin(access_token=credentials)
    assert token_data.sub == uuid.UUID(payload["sub"])
    assert token_data.is_admin is True


def test_get_token_jwt_mandatory_admin_raises_401_for_non_admin():
    """Test get token jwt mandatory admin raises 401 for non admin."""
    payload = {"sub": str(uuid.uuid4()), "is_admin": False}
    token = encode_jwt(payload)
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)

    with pytest.raises(HTTPException) as exc:
        get_token_jwt_mandatory_admin(access_token=credentials)

    assert exc.value.status_code == 401
    assert "admin status is requiered!" in exc.value.detail
