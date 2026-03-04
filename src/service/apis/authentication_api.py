# coding: utf-8

from typing import Dict, List  # noqa: F401

from src.business.interfaces import IBasicAuthManager
from src.core.dtos.google_login_request import GoogleLoginRequest

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

from src.service.security_api import get_token_jwt, get_token_jwt_mandatory

from src.core.settings import settings

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
import httpx

@router.post(
    "/auth/google/login",
    responses={
        200: {
            "model": TokenResponse,
            "description": "Successfully authenticated with Google and returned application tokens."
        },
        401: {
            "description": "Authentication failed or the token exchange was unsuccessful."
        },
    },
    tags=["Authentication"],
    summary="Handle Google OAuth callback and return application tokens.",
    response_model_by_alias=True,
)
async def google_callback(
    google_request: GoogleLoginRequest = Body(None, description=""),
    auth_manager: IBasicAuthManager = Depends(get_auth_manager)
) -> TokenResponse:

    """
    Process Google OAuth callback and exchange code for application tokens.

    @param
        code (str): Authorization code returned by Google after user consent.
        auth_manager (IBasicAuthManager): Business manager used to resolve/create user and issue tokens.

    @return
        TokenResponse: Access and refresh tokens for the authenticated application session.
    """
    token_url = settings.google_settings.token_url

    data = {
        "code": google_request.id_token,
        "client_id": settings.google_settings.client_id,
        "client_secret": settings.google_settings.client_secret,
        "grant_type": "authorization_code",
        "redirect_uri": "postmessage",
    }

    async with httpx.AsyncClient() as client:
        token_response = await client.post(token_url, data=data)

        if token_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Token exchange failed")

        tokens = token_response.json()

        access_token = tokens["access_token"]
        user_info_response = await client.get(
            settings.google_settings.user_info_url,
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
    """
    Authenticate user with username/email and password.

    @param
        login_request (LoginRequest): Login payload containing credentials.
        auth_manager (IBasicAuthManager): Business manager used for authentication flow.

    @return
        TokenResponse: Access and refresh tokens for a successful login.
    """
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
    """
    Register a new user account.

    @param
        signup_request (SignupRequest): Registration payload for creating a user.
        auth_manger (IBasicAuthManager): Business manager used to create account and verification flow.

    @return
        None: Creates account and triggers verification process.
    """
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
    """
    Refresh access token using an existing refresh token.

    @param
        refresh_request (RefreshRequest): Payload containing refresh token reference.
        auth_manager (IBasicAuthManager): Business manager used to validate and refresh tokens.

    @return
        TokenResponse: New access token and refresh token data.
    """
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
        get_token_jwt_mandatory
    ),
    auth_manager: IBasicAuthManager = Depends(get_auth_manager)
) -> None:
    """
    Log out user session by invalidating a refresh token.

    @param
        refresh_token (UUID): Refresh token to invalidate.
        token_jwt (TokenModel): Authenticated user token payload from security dependency.
        auth_manager (IBasicAuthManager): Business manager used to execute logout logic.

    @return
        None: Invalidates the target refresh token.
    """
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
    """
    Initiate password reset flow for a user email.

    @param
        password_reset_request_request (PasswordResetRequestRequest): Payload with account email address.
        auth_manager (IBasicAuthManager): Business manager used to create and deliver reset token.

    @return
        None: Sends password-reset email when account exists.
    """

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
    """
    Complete password reset using submitted reset token and new password.

    @param
        password_reset_submit_request (PasswordResetSubmitRequest): Payload with reset token and new password.
        auth_manager (IBasicAuthManager): Business manager used to validate token and update password.

    @return
        None: Applies password update when token is valid.
    """

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
    """
    Confirm user email verification with submitted verification token.

    @param
        email_verification_submit_request (EmailVerificationSubmitRequest): Payload with verification token.
        auth_manager (IBasicAuthManager): Business manager used to validate and consume token.

    @return
        None: Marks user as verified when token is valid.
    """

    return await auth_manager.verify_email_token(email_verification_submit_request)
