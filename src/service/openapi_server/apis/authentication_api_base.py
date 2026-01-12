# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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

class BaseAuthenticationApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAuthenticationApi.subclasses = BaseAuthenticationApi.subclasses + (cls,)
    async def auth_google_login_get(
        self,
    ) -> TokenResponse:
        ...


    async def auth_google_callback_get(
        self,
    ) -> TokenResponse:
        ...


    async def auth_login_post(
        self,
        login_request: LoginRequest,
    ) -> TokenResponse:
        ...


    async def auth_signup_post(
        self,
        signup_request: SignupRequest,
    ) -> TokenResponse:
        ...


    async def auth_refresh_post(
        self,
        refresh_request: RefreshRequest,
    ) -> TokenResponse:
        ...


    async def auth_logout_post(
        self,
        refresh_token: Annotated[Optional[UUID], Field(description="The refresh token to invalidate. If omitted, all sessions will be terminated.")],
    ) -> None:
        """If a refresh token is provided as a query parameter, only that session is logged out. If none is provided, **all** sessions for the user are logged out. """
        ...


    async def auth_request_password_reset_post(
        self,
        password_reset_request_request: PasswordResetRequestRequest,
    ) -> None:
        """Sends a password-reset token to the specified email-address, if an account exists for that email address. """
        ...


    async def auth_submit_password_reset_post(
        self,
        password_reset_submit_request: PasswordResetSubmitRequest,
    ) -> None:
        """Accepts the password-reset token sent via email and a new password. Does not require the user to be logged in. """
        ...


    async def auth_request_email_verification_post(
        self,
    ) -> None:
        """Sends an email-verification token to the authenticated user&#39;s email. """
        ...


    async def auth_submit_email_verification_post(
        self,
        email_verification_submit_request: EmailVerificationSubmitRequest,
    ) -> None:
        """Accepts the email-verification token sent to the user&#39;s email. """
        ...
