
from src.core.exceptions import (
    UserConflictError,
    AuthError,
    VerificationError,
    QuotaExceededError,
    NotFoundError, AccessError,
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