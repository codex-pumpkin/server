# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

'''
authenticate(request: LoginRequest): Tokens
register(request: SignupRequestRequest): AccountResponse
authenticateWithGoogle(request: GoogleLoginRequest): Tokens
terminateSession(): void
refreshAccessToken(request: RefreshRequest): Tokens
validateAccessToken(sessionToken: String): ValidationResult
verifyEmailToken(request: EmailVerificationSubmitRequest): boolean
initiatePasswordRecovery(request: PasswordResetRequestRequest): void
completePasswordRecovery(request: PasswordResetSubmitRequest): boolean
retrieveAccount(userId: UUID): AccountResponse
modifyAccount(accountUpdate: UpdateAccountRequest): AccountResponse
generateEmailVerification(userId: UUID): void
checkEmailVerificationStatus(userId: UUID): boolean
getCurrentAccountFromToken(token: String): AccountResponse
invalidateRefreshToken(refreshToken: String): void
checkAccountExists(email: String): boolean
'''
#TODO: replace impl with business package
from business.logic_interfaces.IBasicAuthMang import IBasicAuthMang

from service.openapi_server.dependencies import get_auth_manager


from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from service.openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field
from typing import Any, Optional
from typing_extensions import Annotated
from uuid import UUID
from service.openapi_server.models.email_verification_submit_request import EmailVerificationSubmitRequest
from service.openapi_server.models.login_request import LoginRequest
from service.openapi_server.models.password_reset_request_request import PasswordResetRequestRequest
from service.openapi_server.models.password_reset_submit_request import PasswordResetSubmitRequest
from service.openapi_server.models.refresh_request import RefreshRequest
from service.openapi_server.models.signup_request import SignupRequest
from service.openapi_server.models.token_response import TokenResponse
from service.openapi_server.security_api import get_token_JWT

router = APIRouter()



@router.get(
    "/auth/google/login",
    responses={
        200: {"model": TokenResponse, "description": "Login successful"},
        401: {"description": "Could not authenticate"},
    },
    tags=["Authentication"],
    summary="Login via the google identity provider.",
    response_model_by_alias=True,
)
async def auth_google_login_get(
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> TokenResponse:
    authManeger: IBasicAuthMang = Depends(get_auth_manager())
    return await authManeger.authenticateWithGoogle(token_JWT)


@router.get(
    "/auth/google/callback",
    responses={
        200: {"model": TokenResponse, "description": "Login successful"},
        401: {"description": "Could not authenticate"},
    },
    tags=["Authentication"],
    summary="Callback for the google identity provider.",
    response_model_by_alias=True,
)
async def auth_google_callback_get(
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> TokenResponse:
    authManager: IBasicAuthMang = Depends(get_auth_manager())
    return await authManager.google_callback(token_JWT)


@router.post(
    "/auth/login",
    responses={
        200: {"model": TokenResponse, "description": "Login successful"},
        400: {"description": "Invalid request input (e.g., missing password or invalid email format)"},
        401: {"description": "Invalid credentials"},
    },
    tags=["Authentication"],
    summary="Login with email/username and password",
    response_model_by_alias=True,
)
async def auth_login_post(
    login_request: LoginRequest = Body(None, description=""),
) -> TokenResponse:
    authManger = Depends(get_auth_manager())
    return await authManger.authenticate(login_request)


@router.post(
    "/auth/signup",
    responses={
        201: {"model": TokenResponse, "description": "User created successfully"},
        400: {"description": "Invalid request input"},
        409: {"description": "Email or username already exists"},
    },
    tags=["Authentication"],
    summary="Create a new account",
    response_model_by_alias=True,
)
async def auth_signup_post(
    signup_request: SignupRequest = Body(None, description=""),
) -> TokenResponse:
    authManger = Depends(get_auth_manager())
    return await authManger.register(signup_request)


@router.post(
    "/auth/refresh",
    responses={
        200: {"model": TokenResponse, "description": "Token refreshed successfully"},
        400: {"description": "Refresh token missing or invalid format"},
        401: {"description": "Refresh token expired or not recognized"},
    },
    tags=["Authentication"],
    summary="Refresh access token using a refresh token",
    response_model_by_alias=True,
)
async def auth_refresh_post(
    refresh_request: RefreshRequest = Body(None, description=""),
) -> TokenResponse:
    authManger = Depends(get_auth_manager())
    return await authManger.refreshAccessToken(refresh_request)


@router.post(
    "/auth/logout",
    responses={
        204: {"description": "Successfully logged out (no content)"},
        400: {"description": "Invalid refresh token format"},
        401: {"description": "Refresh token was invalid i.e. expired, not found, etc"},
    },
    tags=["Authentication"],
    summary="Logout from one or all sessions",
    response_model_by_alias=True,
)
async def auth_logout_post(
    refresh_token: Annotated[Optional[UUID], Field(description="The refresh token to invalidate. If omitted, all sessions will be terminated.")] = Query(None, description="The refresh token to invalidate. If omitted, all sessions will be terminated.", alias="refresh_token"),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> None:
    """If a refresh token is provided as a query parameter, only that session is logged out. If none is provided, **all** sessions for the user are logged out. """
    authManger = Depends(get_auth_manager())
    return await authManger.user_logout(token_JWT,refresh_token)


@router.post(
    "/auth/request-password-reset",
    responses={
        204: {"description": "Password-reset token sent"},
    },
    tags=["Authentication"],
    summary="Request a password-reset token to a specified email address.",
    response_model_by_alias=True,
)
async def auth_request_password_reset_post(
    password_reset_request_request: PasswordResetRequestRequest = Body(None, description=""),
) -> None:
    """Sends a password-reset token to the specified email-address, if an account exists for that email address. """
    authManger = Depends(get_auth_manager())

    return await authManger.initiatePasswordRecovery(password_reset_request_request)


@router.post(
    "/auth/submit-password-reset",
    responses={
        204: {"description": "Password successfully reset (no content)"},
        400: {"description": "Invalid request"},
        401: {"description": "Reset token invalid or expired"},
    },
    tags=["Authentication"],
    summary="Submit password-reset token and set a new password",
    response_model_by_alias=True,
)
async def auth_submit_password_reset_post(
    password_reset_submit_request: PasswordResetSubmitRequest = Body(None, description=""),
) -> None:
    """Accepts the password-reset token sent via email and a new password. Does not require the user to be logged in. """
    authManger = Depends(get_auth_manager())

    return await authManger.completePasswordRecovery(password_reset_submit_request)


@router.post(
    "/auth/request-email-verification",
    responses={
        204: {"description": "Verification email sent"},
        401: {"description": "User not authenticated"},
        409: {"description": "Email is already verified"},
    },
    tags=["Authentication"],
    summary="Request an email-verification token",
    response_model_by_alias=True,
)
async def auth_request_email_verification_post(
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> None:
    """Sends an email-verification token to the authenticated user&#39;s email. """
    authManger = Depends(get_auth_manager())

    return await authManger.generateEmailVerification(token_JWT)


@router.post(
    "/auth/submit-email-verification",
    responses={
        204: {"description": "Email successfully verified"},
        400: {"description": "Invalid request"},
        401: {"description": "Verification token invalid or expired"},
    },
    tags=["Authentication"],
    summary="Submit an email-verification token",
    response_model_by_alias=True,
)
async def auth_submit_email_verification_post(
    email_verification_submit_request: EmailVerificationSubmitRequest = Body(None, description=""),
) -> None:
    """Accepts the email-verification token sent to the user&#39;s email. """
    authManger = Depends(get_auth_manager())

    return await authManger.verifyEmailToken(email_verification_submit_request)
