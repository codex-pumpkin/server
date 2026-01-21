import datetime

from src.business.interfaces import IBasicAuthManager

from src.core.dtos import (
    AccountResponse,
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
        token = request.verification_token
        repo = await PersistenceFactory.get_entity_repository()

        token_info = await repo.get_token(str(token))
        if token_info is None:
            raise VerificationError("Token doesn't exist!")
        if token_info.token_type != "email":
            raise VerificationError("Token isn't email token!")
        if token_info.expires_at.timestamp() < datetime.datetime.now(datetime.UTC).timestamp():
            raise VerificationError("Token is already expired!")
        if not token_info.valid:
            raise VerificationError("Token is invalidated!")

        await repo.invalidate_token(str(token_info.id))
        await repo.verify_user(str(token_info.user_id))

    async def generate_email_verification(self, user: AccountResponse):
        repo = await PersistenceFactory.get_entity_repository()
        token = await repo.create_token(user.id, "email")
        mail_sender = await PersistenceFactory.get_mail_sender()
        print(f"token={str(token.id)}")
        await mail_sender.send_confirmation_email(user.email, str(token.id))

    async def complete_password_recovery(self, request: PasswordResetSubmitRequest):
        pass

    async def initiate_password_recovery(self, request: PasswordResetRequestRequest):
        pass

    async def user_logout(self, token_jwt: TokenModel, refresh_token: Annotated[Optional[UUID], Field(
        description="The refresh token to invalidate. If omitted, all sessions will be terminated.")]):
        pass

    async def refresh_access_token(self, request: RefreshRequest):
        token = str(request.refresh_token)


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

        refresh_token = await repo.create_token(user.id, "refresh")
        refresh_token = str(refresh_token.id)
        access_token = encode_jwt(
            payload=
                {
                    "sub":user.id,
                }
        )
        token_response = TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token
        )
        return token_response