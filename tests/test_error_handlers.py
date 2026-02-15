from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.core.exceptions import AuthError, UserConflictError, VerificationError
from src.service.error_handlers import register_error_handlers


def _build_app() -> FastAPI:
    app = FastAPI()
    register_error_handlers(app)

    @app.get("/conflict")
    async def conflict():
        raise UserConflictError(field="email")

    @app.get("/auth")
    async def auth():
        raise AuthError("Bad credentials")

    @app.get("/verify")
    async def verify():
        raise VerificationError("Token expired")

    return app


def test_user_conflict_handler_returns_409():
    client = TestClient(_build_app())
    response = client.get("/conflict")

    assert response.status_code == 409
    assert response.json()["field"] == "email"
    assert "already taken" in response.json()["detail"]


def test_auth_handler_returns_401():
    client = TestClient(_build_app())
    response = client.get("/auth")

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Authentication failed.",
        "issue": "Bad credentials",
    }


def test_verification_handler_returns_401():
    client = TestClient(_build_app())
    response = client.get("/verify")

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Verification failed",
        "issue": "Token expired",
    }

