from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.core.exceptions import (
    AccessError,
    AuthError,
    LLMAPIConnectionError,
    LLMAPIError,
    LLMAuthenticationError,
    LLMBadRequestError,
    LLMNotFoundError,
    LLMPermissionDeniedError,
    LLMRateLimitError,
    NotFoundError,
    QuotaExceededError,
    UserConflictError,
    VerificationError,
)
from src.service.error_handlers import register_error_handlers


def _build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()
    register_error_handlers(app)

    @app.get("/conflict")
    async def conflict():
        """Conflict."""
        raise UserConflictError(field="email")

    @app.get("/auth")
    async def auth():
        """Auth."""
        raise AuthError("Bad credentials")

    @app.get("/verify")
    async def verify():
        """Verify."""
        raise VerificationError("Token expired")

    @app.get("/quota")
    async def quota():
        """Quota."""
        raise QuotaExceededError("Daily limit reached")

    @app.get("/not-found")
    async def not_found():
        """Not found."""
        raise NotFoundError("conversation", "123")

    @app.get("/access")
    async def access():
        """Access."""
        raise AccessError("conversation", "123")

    @app.get("/llm-bad-request")
    async def llm_bad_request():
        """Llm bad request."""
        raise LLMBadRequestError()

    @app.get("/llm-connection")
    async def llm_connection():
        """Llm connection."""
        raise LLMAPIConnectionError()

    @app.get("/llm-api")
    async def llm_api():
        """Llm api."""
        raise LLMAPIError()

    @app.get("/llm-auth")
    async def llm_auth():
        """Llm auth."""
        raise LLMAuthenticationError()

    @app.get("/llm-not-found")
    async def llm_not_found():
        """Llm not found."""
        raise LLMNotFoundError()

    @app.get("/llm-permission")
    async def llm_permission():
        """Llm permission."""
        raise LLMPermissionDeniedError()

    @app.get("/llm-rate-limit")
    async def llm_rate_limit():
        """Llm rate limit."""
        raise LLMRateLimitError()

    return app


def test_user_conflict_handler_returns_409():
    """Test user conflict handler returns 409."""
    client = TestClient(_build_app())
    response = client.get("/conflict")

    assert response.status_code == 409
    detail = response.json()["detail"]
    assert detail["field"] == "email"
    assert "already taken" in detail["detail"]


def test_auth_handler_returns_401():
    """Test auth handler returns 401."""
    client = TestClient(_build_app())
    response = client.get("/auth")

    assert response.status_code == 401
    assert response.json()["detail"] == {
        "detail": "Authentication failed.",
        "issue": "Bad credentials",
    }


def test_verification_handler_returns_401():
    """Test verification handler returns 401."""
    client = TestClient(_build_app())
    response = client.get("/verify")

    assert response.status_code == 401
    assert response.json()["detail"] == {
        "detail": "Verification failed",
        "issue": "Token expired",
    }


def test_quota_handler_returns_429():
    """Test quota handler returns 429."""
    client = TestClient(_build_app())
    response = client.get("/quota")

    assert response.status_code == 429
    assert response.json()["detail"] == {
        "detail": "Quota exceeded",
        "issue": "Daily limit reached",
    }


def test_not_found_handler_returns_404():
    """Test not found handler returns 404."""
    client = TestClient(_build_app())
    response = client.get("/not-found")

    assert response.status_code == 404
    detail = response.json()["detail"]
    assert detail["detail"] == "Not found"
    assert "conversation with id: 123 is not found!" in detail["issue"]


def test_access_handler_returns_403():
    """Test access handler returns 403."""
    client = TestClient(_build_app())
    response = client.get("/access")

    assert response.status_code == 403
    detail = response.json()["detail"]
    assert detail["detail"] == "Access issue"
    assert "You dont have access to conversation with id: 123" in detail["issue"]


def test_llm_bad_request_handler_returns_400():
    """Test llm bad request handler returns 400."""
    client = TestClient(_build_app())
    response = client.get("/llm-bad-request")

    assert response.status_code == 400
    detail = response.json()["detail"]
    assert detail["detail"] == "LLM API bad request"
    assert "bad request" in detail["issue"].lower()


def test_llm_api_connection_handler_returns_503():
    """Test llm api connection handler returns 503."""
    client = TestClient(_build_app())
    response = client.get("/llm-connection")

    assert response.status_code == 503
    detail = response.json()["detail"]
    assert detail["detail"] == "LLM API connection error"
    assert "connect" in detail["issue"].lower()


def test_llm_api_error_handler_returns_502():
    """Test llm api error handler returns 502."""
    client = TestClient(_build_app())
    response = client.get("/llm-api")

    assert response.status_code == 502
    detail = response.json()["detail"]
    assert detail["detail"] == "LLM API error"
    assert "error occurred while communicating" in detail["issue"].lower()


def test_llm_authentication_handler_returns_401():
    """Test llm authentication handler returns 401."""
    client = TestClient(_build_app())
    response = client.get("/llm-auth")

    assert response.status_code == 401
    detail = response.json()["detail"]
    assert detail["detail"] == "LLM API authentication error"
    assert "authenticate" in detail["issue"].lower()


def test_llm_not_found_handler_returns_404():
    """Test llm not found handler returns 404."""
    client = TestClient(_build_app())
    response = client.get("/llm-not-found")

    assert response.status_code == 404
    detail = response.json()["detail"]
    assert detail["detail"] == "LLM resource not found"
    assert "not found" in detail["issue"].lower()


def test_llm_permission_denied_handler_returns_403():
    """Test llm permission denied handler returns 403."""
    client = TestClient(_build_app())
    response = client.get("/llm-permission")

    assert response.status_code == 403
    detail = response.json()["detail"]
    assert detail["detail"] == "LLM API permission denied"
    assert "denied permission" in detail["issue"].lower()


def test_llm_rate_limit_handler_returns_429():
    """Test llm rate limit handler returns 429."""
    client = TestClient(_build_app())
    response = client.get("/llm-rate-limit")

    assert response.status_code == 429
    detail = response.json()["detail"]
    assert detail["detail"] == "LLM rate limit exceeded"
    assert "rate limit" in detail["issue"].lower()
