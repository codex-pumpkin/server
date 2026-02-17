
from src.core.exceptions import (
    UserConflictError,
    AuthError,
    VerificationError,
    QuotaExceededError,
    NotFoundError, 
    AccessError,
    LLMBadRequestError,
    LLMAPIConnectionError,
    LLMAPIError,
    LLMAuthenticationError,
    LLMNotFoundError,
    LLMPermissionDeniedError,
    LLMRateLimitError
)

from fastapi import FastAPI, Request, HTTPException, status

def register_error_handlers(app: FastAPI):

    @app.exception_handler(UserConflictError)
    async def conflict_handler(request: Request, exc: UserConflictError):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"detail": exc.message, "field": exc.field},
        )

    @app.exception_handler(AuthError)
    async def auth_handler(request: Request, exc: AuthError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"detail": "Authentication failed.", "issue": exc.message},
        )

    @app.exception_handler(VerificationError)
    async def verification_handler(request: Request, exc: VerificationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"detail": "Verification failed", "issue": exc.message},
        )

    @app.exception_handler(QuotaExceededError)
    async def quota_handler(request: Request, exc: QuotaExceededError):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={"detail": "Quota exceeded", "issue": exc.message},
        )

    @app.exception_handler(NotFoundError)
    async def not_found_handler(request: Request, exc: NotFoundError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"detail": "Not found", "issue": exc.message}
        )

    @app.exception_handler(AccessError)
    async def access_handler(request: Request, exc: AccessError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"detail": "Access issue", "issue": exc.message}
        )
    
    @app.exception_handler(LLMBadRequestError)
    async def llm_bad_request_handler(request: Request, exc: LLMBadRequestError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"detail": "LLM API bad request", "issue": exc.message}
        )  
    
    @app.exception_handler(LLMAPIConnectionError)
    async def llm_api_connection_handler(request: Request, exc: LLMAPIConnectionError   ):
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"detail": "LLM API connection error", "issue": exc.message}
        )
    
    @app.exception_handler(LLMAPIError)
    async def llm_api_error_handler(request: Request, exc: LLMAPIError):
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail={"detail": "LLM API error", "issue": exc.message}
        )
    
    @app.exception_handler(LLMAuthenticationError)
    async def llm_authentication_handler(request: Request, exc: LLMAuthenticationError):    
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"detail": "LLM API authentication error", "issue": exc.message}
        )
    
    @app.exception_handler(LLMNotFoundError)
    async def llm_not_found_handler(request: Request, exc: LLMNotFoundError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"detail": "LLM resource not found", "issue": exc.message}
        )
    
    @app.exception_handler(LLMPermissionDeniedError)
    async def llm_permission_denied_handler(request: Request, exc: LLMPermissionDeniedError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"detail": "LLM API permission denied", "issue": exc.message}
        )
    
    @app.exception_handler(LLMRateLimitError)
    async def llm_rate_limit_handler(request: Request, exc: LLMRateLimitError):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={"detail": "LLM rate limit exceeded", "issue": exc.message}
        )