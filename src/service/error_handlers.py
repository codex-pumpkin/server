from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.core.exceptions import (
    UserConflictError,
    AuthError
)


def register_error_handlers(app: FastAPI):
    @app.exception_handler(UserConflictError)
    async def conflict_handler(request: Request, exc: UserConflictError) -> JSONResponse:
        return JSONResponse(
            status_code=409,
            content={"detail": exc.message, "field": exc.field}
        )

    @app.exception_handler(AuthError)
    async def auth_handler(request: Request, exc: AuthError) -> JSONResponse:
        return JSONResponse(
            status_code=401,
            content={"detail": exc.message}
        )