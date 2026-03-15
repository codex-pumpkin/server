import datetime

from src.business.interfaces import IBasicAuthManager
from src.core import settings

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
        """
        Generates a temporary random password for externally created accounts.

        The password is composed of lowercase letters, digits, and selected
        punctuation characters. The generated password length is fixed to 12 characters.

        @return a randomly generated 12-character password string
        """
        letters = "qwertyuiopasdghklzxcvbnm1234567890<>,.:;!@#$%^*(){}[]"
        password = ""
        for i in range(12):
            password += random.choice(letters)
        return password

    async def google_callback(self, username:str, email:str, picture:str) -> TokenResponse:
        """
                Handles Google OAuth callback authentication.

                If a user with the given email already exists, all previous refresh tokens
                are invalidated and a new token pair is issued.

                If the user does not exist, a new account is created with a generated
                temporary password and a unique username. The temporary password is sent
                via email.

                @param username the username retrieved from Google profile
                @param email the email retrieved from Google profile
                @param picture the profile picture URL (currently unused)
                @return TokenResponse containing new access and refresh tokens
                """
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.get_user_by_email(email=email)
        if user is not None:
            # Enforce single-session semantics by invalidating old refresh tokens
            # before issuing a fresh token pair for this login.
            await repo.verify_user(str(user.id))
            await repo.invalidate_all_refresh_tokens(user_id=str(user.id))
            tokens = await self._generate_tokens_pair(
                user=user,
                repo=repo
            )
            return tokens
        addition = 0
        while True:
            # Find the first available username variant by appending an incrementing
            # suffix until the generated name is not already used.
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
        user = await repo.create_user(user=request, verified=True)
        mail_sender = await PersistenceFactory.get_mail_sender()
        # Newly created OAuth users receive a generated temporary password via email
        # so they still have a recoverable credential path.
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
        """
                Verifies an email confirmation token.

                <p>
                The token must:
                <ul>
                    <li>Exist in the system</li>
                    <li>Be of type "email"</li>
                    <li>Be valid and not expired</li>
                </ul>
                After successful validation, the token is invalidated and
                the corresponding user account is marked as verified.
                </p>

                @param request object containing the verification token
                @throws NotFoundError if the token does not exist
                @throws VerificationError if the token is invalid, expired, or incorrect type
                """

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
        if token_info.expires_at.timestamp() < datetime.datetime.now(datetime.UTC).replace(tzinfo=None).timestamp():
            raise VerificationError("Token is already expired!")
        if not token_info.valid:
            raise VerificationError("Token is invalidated!")

        # Verification tokens are single-use; invalidate first, then mark the
        # related account as verified.
        await repo.invalidate_token(str(token_info.id))
        await repo.verify_user(str(token_info.user_id))

    async def generate_email_verification(self, user_id:UUID, user_email:str):
        """
                Generates and sends an email verification token.

                <p>
                A new token of type "email" is created and sent to the specified email address.
                </p>

                @param user_id the unique identifier of the user
                @param user_email the user's email address
                """
        repo = await PersistenceFactory.get_entity_repository()
        token = await repo.create_token(str(user_id), "email")
        mail_sender = await PersistenceFactory.get_mail_sender()
        print(f"token={str(token.id)}")
        await mail_sender.send_confirmation_email(user_email, str(token.id))

    async def complete_password_recovery(self, request: PasswordResetSubmitRequest):
        """
                Completes the password reset process.

                <p>
                Validates the provided reset token and, if valid, invalidates it and
                updates the user's password.
                </p>

                @param request object containing reset token and new password
                @throws NotFoundError if the token does not exist
                @throws AuthError if the token is invalid, expired, or not of type "password"
                """
        repo = await PersistenceFactory.get_entity_repository()
        token = await repo.get_token(request.reset_token)
        if token is None:
            raise NotFoundError(
                type_of="token",
                id_of=str(token)
            )
        if token.token_type != "password":
            raise AuthError("Token isn't of type recover password!")
        if not token.valid or token.expires_at.timestamp() < datetime.datetime.now(datetime.UTC).replace(tzinfo=None).timestamp():
            raise AuthError("Token isn't valid!")
        await repo.invalidate_token(str(token.id))
        await repo.change_password(str(token.user_id), request.new_password)

    async def initiate_password_recovery(self, request: PasswordResetRequestRequest):
        """
               Initiates password recovery process.

               <p>
               If a user with the given email exists, a password reset token is created
               and sent to the user's email address.
               </p>

               @param request object containing the email address
               @throws AuthError if the email is not associated with any user
               """
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.get_user_by_email(request.email)
        if user is None:
            raise AuthError("Such email is not used!")
        token = await repo.create_token(str(user.id), "password")
        mail_sender = await PersistenceFactory.get_mail_sender()
        print(f"token={str(token.id)}")
        await mail_sender.send_password_reset_email(user.email, str(token.id))

    async def user_logout(self, refresh_token: UUID):
        """
               Logs out the user by invalidating the specified refresh token.

               @param refresh_token the refresh token identifier to invalidate
               @throws AuthError if token invalidation fails
        """
        repo = await PersistenceFactory.get_entity_repository()
        success = await repo.invalidate_token(str(refresh_token))
        if not success:
            raise AuthError()

    async def refresh_access_token(self, request: RefreshRequest) -> TokenResponse:
        """
                Refreshes an access token using a valid refresh token.

                <p>
                The refresh token must:
                <ul>
                    <li>Exist</li>
                    <li>Be of type "refresh"</li>
                    <li>Be valid and not expired</li>
                </ul>
                A new access token is issued after rotating the refresh token state.
                </p>

                @param request object containing the refresh token
                @return TokenResponse containing new access token and refresh token
                @throws NotFoundError if token does not exist
                @throws AuthError if token is invalid, expired, or incorrect type
                """
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
        if not refresh_token.valid or refresh_token.expires_at.timestamp() < datetime.datetime.now(datetime.UTC).replace(tzinfo=None).timestamp():
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
        """
                Registers a new user account.

                <p>
                Persists the new user in storage and sends an email verification token.
                </p>

                @param request registration payload containing username, email, and password
                """
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.create_user(request)
        await self.generate_email_verification(user.id, user.email)


    async def authenticate(self, request: LoginRequest) -> TokenResponse:
        """
                Authenticates a user using provided credentials.

                <p>
                If authentication succeeds and the user is verified,
                all previous refresh tokens are invalidated and a new token pair is issued.
                </p>
                <p>
                If the user is not verified, a new verification email is sent
                and authentication fails.
                </p>

                @param request login payload containing username/email and password
                @return TokenResponse containing access and refresh tokens
                @throws AuthError if authentication fails or user is not verified
                """
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.authenticate(
            username=request.username,
            email=request.email,
            password=request.password
        )
        if user is None:
            raise AuthError("User is not found!")

        if (not user.is_verified) and settings.mail_settings.verification_required:
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
        """
                Generates a new access and refresh token pair.

                <p>
                A refresh token is persisted in storage and an access JWT is generated
                containing the user ID and administrative flag.
                </p>

                @param user authenticated user information
                @param repo repository used to create refresh token
                @return TokenResponse containing access and refresh tokens
                """
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
