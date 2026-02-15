# coding: utf-8

from typing import Dict, List  # noqa: F401

from src.business.interfaces import IBasicAuthManager

from src.service.dependencies import get_auth_manager


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

from pydantic import Field
from typing_extensions import Annotated
from uuid import UUID

from src.service.security_api import get_token_jwt

from src.core.dtos import (
    EmailVerificationSubmitRequest,
    LoginRequest,
    PasswordResetRequestRequest,
    PasswordResetSubmitRequest,
    RefreshRequest,
    SignupRequest,
    TokenResponse,
    TokenModel
)

router = APIRouter()

from fastapi.responses import RedirectResponse
import urllib.parse
import httpx



@router.get(
    "/auth/google/login",
    responses={
        200: {"description": "Login successful"},
        401: {"description": "Could not authenticate"},
    },
    tags=["Authentication"],
    summary="Login via the google identity provider.",
    response_model_by_alias=True,
)
async def auth_google_login_get():
    params = {
        "client_id": "720310987371-5rrnoedva7eq2lva8c0vdqtr2stsdq34.apps.googleusercontent.com",
        "redirect_uri": "http://localhost:8000/auth/google/callback",
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent",
    }

    url = "https://accounts.google.com/o/oauth2/auth?" + urllib.parse.urlencode(params)

    return RedirectResponse(url)


@router.get(
    "/auth/google/callback",
    responses={
        200: {"model":TokenResponse, "description": "Login successful"},
        401: {"description": "Could not authenticate"},
    },
    tags=["Authentication"],
    summary="Callback for the google identity provider.",
    response_model_by_alias=True,
)
@router.get("/auth/google/callback")
async def google_callback(
    code: str,
    auth_manager: IBasicAuthManager = Depends(get_auth_manager)
) -> TokenResponse:

    token_url = "https://oauth2.googleapis.com/token"

    data = {
        "code": code,
        "client_id": "720310987371-5rrnoedva7eq2lva8c0vdqtr2stsdq34.apps.googleusercontent.com",
        "client_secret": "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",
        "redirect_uri": "http://localhost:8000/auth/google/callback",
        "grant_type": "authorization_code",
    }

    async with httpx.AsyncClient() as client:
        token_response = await client.post(token_url, data=data)

        if token_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Token exchange failed")

        tokens = token_response.json()

        access_token = tokens["access_token"]
        user_info_response = await client.get(
            "https://www.googleapis.com/oauth2/v3/userinfo",
            headers={"Authorization": f"Bearer {access_token}"}
        )

        user_info = user_info_response.json()

    tokens = await auth_manager.google_callback(
        username=user_info["name"],
        email=user_info["email"],
        picture=user_info["picture"]
    )
    return tokens



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
    auth_manager: IBasicAuthManager = Depends(get_auth_manager)
) -> TokenResponse:
    return await auth_manager.authenticate(login_request)


@router.post(
    "/auth/signup",
    status_code=201,
    responses={
        201: {"description": "User created successfully"},
        400: {"description": "Invalid request input"},
        409: {"description": "Email or username already exists"},
    },
    tags=["Authentication"],
    summary="Create a new account",
    response_model_by_alias=True,
)
async def auth_signup_post(
    signup_request: SignupRequest = Body(None, description=""),
    auth_manger: IBasicAuthManager = Depends(get_auth_manager)
) -> None:
    await auth_manger.register(signup_request)


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
    auth_manager: IBasicAuthManager = Depends(get_auth_manager)
) -> TokenResponse:
    return await auth_manager.refresh_access_token(refresh_request)


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
    refresh_token: Annotated[UUID, Field(description="The refresh token to invalidate. If omitted, all sessions will be terminated.")] = Query(None, description="The refresh token to invalidate. If omitted, all sessions will be terminated.", alias="refresh_token"),
    token_jwt: TokenModel = Security(
        get_token_jwt
    ),
    auth_manager: IBasicAuthManager = Depends(get_auth_manager)
) -> None:
    """If a refresh token is provided as a query parameter, only that session is logged out. If none is provided, **all** sessions for the user are logged out. """
    return await auth_manager.user_logout(refresh_token)


@router.post(
    "/auth/request-password-reset",
    responses={
        204: {"description": "Password-reset token sent"},
        401: {"description": "No user with such email"}
    },
    tags=["Authentication"],
    summary="Request a password-reset token to a specified email address.",
    response_model_by_alias=True,
)
async def auth_request_password_reset_post(
    password_reset_request_request: PasswordResetRequestRequest = Body(None, description=""),
    auth_manager: IBasicAuthManager = Depends(get_auth_manager)
) -> None:
    """Sends a password-reset token to the specified email-address, if an account exists for that email address. """

    return await auth_manager.initiate_password_recovery(password_reset_request_request)


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
    auth_manager: IBasicAuthManager = Depends(get_auth_manager)
) -> None:
    """Accepts the password-reset token sent via email and a new password. Does not require the user to be logged in. """

    return await auth_manager.complete_password_recovery(password_reset_submit_request)


@router.post(
    "/auth/submit-email-verification",
    responses={
        204: {"description": "Email successfully verified"},
        400: {"description": "Invalid request"},
        401: {"description": "Verification token invalid"},
    },
    tags=["Authentication"],
    summary="Submit an email-verification token",
    response_model_by_alias=True,
)
async def auth_submit_email_verification_post(
    email_verification_submit_request: EmailVerificationSubmitRequest = Body(None),
    auth_manager:IBasicAuthManager = Depends(get_auth_manager)
) -> None:
    """Accepts the email-verification token sent to the user&#39;s email. """

    return await auth_manager.verify_email_token(email_verification_submit_request)
