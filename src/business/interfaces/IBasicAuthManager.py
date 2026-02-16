from abc import ABC, abstractmethod

from src.core.dtos import (
    TokenModel,
    EmailVerificationSubmitRequest,
    PasswordResetSubmitRequest,
    PasswordResetRequestRequest,
    RefreshRequest,
    SignupRequest,
    LoginRequest,
    TokenResponse,
    AccountResponse
)

from typing import Annotated, Optional
from uuid import UUID
from pydantic import Field

class IBasicAuthManager(ABC):

    @abstractmethod
    async def google_callback(self, username:str, email:str, picture:str) -> TokenResponse:
        pass

    @abstractmethod
    async def verify_email_token(self, request: EmailVerificationSubmitRequest):
        pass

    @abstractmethod
    async def generate_email_verification(self, user_id:UUID, user_email:str):
        pass

    @abstractmethod
    async def complete_password_recovery(self, request: PasswordResetSubmitRequest):
        pass

    @abstractmethod
    async def initiate_password_recovery(self, request: PasswordResetRequestRequest):
        pass

    @abstractmethod
    async def user_logout(
        self,
        refresh_token: Annotated[
            UUID,
            Field(
                description=
                "The refresh token to invalidate. "
                "If omitted, all sessions will be terminated."
            )
        ]
    ):
        pass

    @abstractmethod
    async def refresh_access_token(self, request: RefreshRequest) -> TokenResponse:
        pass

    @abstractmethod
    async def register(self, request: SignupRequest):
        pass

    @abstractmethod
    async def authenticate(self, request: LoginRequest) -> TokenResponse:
        pass