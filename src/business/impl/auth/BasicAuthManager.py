

from src.business.interfaces import IBasicAuthManager

from src.core.dtos import (
    AccountInfo,
    TokenModel,
    EmailVerificationSubmitRequest,
    PasswordResetSubmitRequest,
    PasswordResetRequestRequest,
    RefreshRequest,
    SignupRequest,
    LoginRequest,
    TokenResponse
)

from src.core.exceptions import (
    AuthError,
    VerificationError,
)

from typing import Annotated, Optional
from uuid import UUID
from pydantic import Field

from src.business.impl.auth.tokens import encode_jwt
from src.persistence import PersistenceFactory

class BasicAuthManager(IBasicAuthManager):

    async def authenticate_with_google(self, token_jwt: TokenModel):
        pass

    async def google_callback(self, token_jwt: TokenModel):
        pass

    async def verify_email_token(self, request: EmailVerificationSubmitRequest):
        mail = request.email
        token = request.verification_token
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.get_user_by_email(mail)
        if user is None:
            raise VerificationError("User with such email was not found!")
        if user.is_verified:
            raise VerificationError("User is already verified!")
        if user.verification_code != token:
            raise VerificationError("Code is not correct!")
        return await repo.verify_user(user.id)

    async def generate_email_verification(self, user: AccountInfo):
        mail_sender = await PersistenceFactory.get_mail_sender()
        print(f"{user.verification_code=}")
        await mail_sender.send_confirmation_email(user.email, user.verification_code)

    async def complete_password_recovery(self, request: PasswordResetSubmitRequest):
        pass

    async def initiate_password_recovery(self, request: PasswordResetRequestRequest):
        pass

    async def user_logout(self, token_jwt: TokenModel, refresh_token: Annotated[Optional[UUID], Field(
        description="The refresh token to invalidate. If omitted, all sessions will be terminated.")]):
        pass

    async def refresh_access_token(self, request: RefreshRequest):
        pass

    async def register(self, request: SignupRequest):
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.create_user(request)
        await self.generate_email_verification(user)


    async def authenticate(self, request: LoginRequest) -> TokenResponse:
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.authenticate(
            username=request.username,
            email=request.email,
            password=request.password
        )
        if user is None:
            raise AuthError("User is not found!")

        if not user.is_verified:
            raise AuthError("Users email is not verified!")

        refresh_token = await repo.create_token(user.id)
        access_token = encode_jwt(
            payload=
                {
                    "sub":user.id,
                    "refresh":refresh_token
                }
        )
        token_response = TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token
        )
        return token_response