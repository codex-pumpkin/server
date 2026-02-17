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
    NotFoundError
)

from typing import Annotated, Optional
from uuid import UUID
from pydantic import Field

from src.business.impl.auth.tokens import encode_jwt
from src.persistence import PersistenceFactory, IEntityRepository
import random


class BasicAuthManager(IBasicAuthManager):

    def _generate_password(self) -> str:
        """Generate password."""
        letters = "qwertyuiopasdghklzxcvbnm1234567890<>,.:;!@#$%^*(){}[]"
        password = ""
        for i in range(12):
            password += random.choice(letters)
        return password

    async def google_callback(self, username:str, email:str, picture:str) -> TokenResponse:
        """Google callback."""
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.get_user_by_email(email=email)
        if user is not None:
            await repo.invalidate_all_refresh_tokens(user_id=str(user.id))
            tokens = await self._generate_tokens_pair(
                user=user,
                repo=repo
            )
            return tokens
        addition = 0
        while True:
            if addition == 0:
                new_user_name = username
            else:
                new_user_name = username + str(addition)
            taken = await repo.is_username_taken(new_user_name)
            addition += 1
            if not taken:
                username = new_user_name
                break
        password = self._generate_password()
        request = SignupRequest(
            email=email,
            password=password,
            username=username
        )
        user = await repo.create_user(user=request)
        mail_sender = await PersistenceFactory.get_mail_sender()
        await mail_sender.send_temporary_password_email(
            to_email=email,
            password=password
        )
        tokens = await self._generate_tokens_pair(
            user=user,
            repo=repo
        )
        return tokens


    async def verify_email_token(self, request: EmailVerificationSubmitRequest):
        """Verify email token."""
        token = request.verification_token
        repo = await PersistenceFactory.get_entity_repository()

        token_info = await repo.get_token(str(token))
        if token_info is None:
            raise NotFoundError(
                type_of="token",
                id_of=str(token)
            )
        if token_info.token_type != "email":
            raise VerificationError("Token isn't email token!")
        if token_info.expires_at.timestamp() < datetime.datetime.now(datetime.UTC).timestamp():
            raise VerificationError("Token is already expired!")
        if not token_info.valid:
            raise VerificationError("Token is invalidated!")

        await repo.invalidate_token(str(token_info.id))
        await repo.verify_user(str(token_info.user_id))

    async def generate_email_verification(self, user_id:UUID, user_email:str):
        """Generate email verification."""
        repo = await PersistenceFactory.get_entity_repository()
        token = await repo.create_token(str(user_id), "email")
        mail_sender = await PersistenceFactory.get_mail_sender()
        print(f"token={str(token.id)}")
        await mail_sender.send_confirmation_email(user_email, str(token.id))

    async def complete_password_recovery(self, request: PasswordResetSubmitRequest):
        """Complete password recovery."""
        repo = await PersistenceFactory.get_entity_repository()
        token = await repo.get_token(request.reset_token)
        if token is None:
            raise NotFoundError(
                type_of="token",
                id_of=str(token)
            )
        if token.token_type != "password":
            raise AuthError("Token isn't of type recover password!")
        if not token.valid or token.expires_at.timestamp() < datetime.datetime.now(datetime.UTC).timestamp():
            raise AuthError("Token isn't valid!")
        await repo.invalidate_token(str(token.id))
        await repo.change_password(str(token.user_id), request.new_password)

    async def initiate_password_recovery(self, request: PasswordResetRequestRequest):
        """Initiate password recovery."""
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.get_user_by_email(request.email)
        if user is None:
            raise AuthError("Such email is not used!")
        token = await repo.create_token(str(user.id), "password")
        mail_sender = await PersistenceFactory.get_mail_sender()
        print(f"token={str(token.id)}")
        await mail_sender.send_password_reset_email(user.email, str(token.id))

    async def user_logout(self, refresh_token: UUID):
        """User logout."""
        repo = await PersistenceFactory.get_entity_repository()
        success = await repo.invalidate_token(str(refresh_token))
        if not success:
            raise AuthError()

    async def refresh_access_token(self, request: RefreshRequest) -> TokenResponse:
        """Refresh access token."""
        token = str(request.refresh_token)
        repo = await PersistenceFactory.get_entity_repository()
        refresh_token = await repo.get_token(token)
        if refresh_token is None:
            raise NotFoundError(
                type_of="token",
                id_of=str(token)
            )
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
        """Register."""
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.create_user(request)
        await self.generate_email_verification(user.id, user.email)


    async def authenticate(self, request: LoginRequest) -> TokenResponse:
        """Authenticate."""
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.authenticate(
            username=request.username,
            email=request.email,
            password=request.password
        )
        if user is None:
            raise AuthError("User is not found!")

        if not user.is_verified:
            # If a user that is not email-verified tries to login,
            # the request fails but we send the verification email.
            await self.generate_email_verification(user.id, user.email)
            raise AuthError("Users email is not verified!")

        await repo.invalidate_all_refresh_tokens(str(user.id))
        tokens = await self._generate_tokens_pair(
            user=user,
            repo=repo
        )
        return tokens


    async def _generate_tokens_pair(
        self,
        user: AccountResponse,
        repo: IEntityRepository
    ) -> TokenResponse:
        """Generate tokens pair."""
        refresh_token = await repo.create_token(str(user.id), "refresh")
        refresh_token = str(refresh_token.id)
        access_token = encode_jwt(
            payload=
                {
                    "sub":str(user.id),
                    "is_admin": user.is_admin
                }
        )
        token_response = TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token
        )
        return token_response
