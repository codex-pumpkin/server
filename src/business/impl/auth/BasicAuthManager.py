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
        token = await repo.create_token(str(user.id), "email")
        mail_sender = await PersistenceFactory.get_mail_sender()
        print(f"token={str(token.id)}")
        await mail_sender.send_confirmation_email(user.email, str(token.id))

    async def complete_password_recovery(self, request: PasswordResetSubmitRequest):
        repo = await PersistenceFactory.get_entity_repository()
        token = await repo.get_token(request.reset_token)
        if token is None:
            raise AuthError("Token doesn't exist!")
        if token.token_type != "password":
            raise AuthError("Token isn't of type recover password!")
        if not token.valid or token.expires_at.timestamp() < datetime.datetime.now(datetime.UTC).timestamp():
            raise AuthError("Token isn't valid!")
        await repo.invalidate_token(str(token.id))
        await repo.change_password(str(token.user_id), request.new_password)

    async def initiate_password_recovery(self, request: PasswordResetRequestRequest):
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.get_user_by_email(request.email)
        if user is None:
            raise AuthError("Such email is not used!")
        token = await repo.create_token(str(user.id), "password")
        mail_sender = await PersistenceFactory.get_mail_sender()
        print(f"token={str(token.id)}")
        await mail_sender.send_password_reset_email(user.email, str(token.id))

    async def user_logout(self, refresh_token: UUID):
        repo = await PersistenceFactory.get_entity_repository()
        success = await repo.invalidate_token(str(refresh_token))
        if not success:
            raise AuthError()

    async def refresh_access_token(self, request: RefreshRequest) -> TokenResponse:
        token = str(request.refresh_token)
        repo = await PersistenceFactory.get_entity_repository()
        refresh_token = await repo.get_token(token)
        if refresh_token is None:
            raise AuthError("Token doesn't exist!")
        if refresh_token.token_type != "refresh":
            raise AuthError("Token isn't of type refresh!")
        if not refresh_token.valid or refresh_token.expires_at.timestamp() < datetime.datetime.now(datetime.UTC).timestamp():
            raise AuthError("Token isn't valid!")

        refresh_token = await repo.change_token(token)
        user = await repo.get_user_by_id(str(refresh_token.user_id))
        access_token = encode_jwt(
            payload={
                "sub": str(refresh_token.user_id),
                "is_admin": user.is_admin
            }
        )
        return TokenResponse(
            access_token=access_token,
            refresh_token=token
        )

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

        await repo.invalidate_all_refresh_tokens(str(user.id))
        refresh_token = await repo.create_token(str(user.id), "refresh")
        refresh_token = str(refresh_token.id)
        access_token = encode_jwt(
            payload=
                {
                    "sub":str(user.id),
                }
        )
        token_response = TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token
        )
        return token_response