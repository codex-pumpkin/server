from fastapi import FastAPI, Depends, Security
from fastapi.testclient import TestClient
from types import SimpleNamespace
from unittest.mock import AsyncMock
from uuid import uuid4
import datetime

from src.service.apis.authentication_api import router as auth_router
from src.service.dependencies import get_auth_manager
from src.service.security_api import get_token_jwt_mandatory
from src.core.dtos import (
    TokenResponse,
    TokenModel,
    LoginRequest,
    SignupRequest,
    RefreshRequest,
)


def _dummy_token():
    return TokenModel(
        sub=uuid4(),
        is_admin=False,
        exp=datetime.datetime.now(),
        toc=datetime.datetime.now(),
    )


def setup_test_app():
    app = FastAPI()
    app.include_router(auth_router)

    # override the auth manager dependency with a simple AsyncMock-based object
    def override_auth_manager():
        mgr = SimpleNamespace()
        mgr.authenticate = AsyncMock(return_value=TokenResponse(access_token="access", refresh_token="refresh"))
        mgr.register = AsyncMock(return_value=None)
        mgr.refresh_access_token = AsyncMock(return_value=TokenResponse(access_token="new", refresh_token="newrefresh"))
        mgr.user_logout = AsyncMock(return_value=None)
        mgr.initiate_password_recovery = AsyncMock(return_value=None)
        mgr.complete_password_recovery = AsyncMock(return_value=None)
        mgr.verify_email_token = AsyncMock(return_value=None)
        return mgr

    app.dependency_overrides[get_auth_manager] = override_auth_manager
    app.dependency_overrides[get_token_jwt_mandatory] = lambda: _dummy_token()
    return app


app = setup_test_app()
client = TestClient(app)


def test_login_endpoint():
    resp = client.post("/auth/login", json={"email": "a@b.com", "password": "x"})
    assert resp.status_code == 200
    assert resp.json()["access_token"] == "access"


def test_signup_endpoint():
    resp = client.post("/auth/signup", json={"email": "a@b.com", "username": "u", "password": "x"})
    assert resp.status_code == 201


def test_refresh_endpoint():
    resp = client.post("/auth/refresh", json={"refresh_token": str(uuid4())})
    assert resp.status_code == 200
    assert resp.json()["access_token"] == "new"


def test_logout_endpoint():
    rtoken = str(uuid4())
    resp = client.post(f"/auth/logout?refresh_token={rtoken}")
    # logout returns whatever auth_manager.user_logout returns; since our override returns AsyncMock (None), status 200 or 204
    assert resp.status_code in (200, 204)

