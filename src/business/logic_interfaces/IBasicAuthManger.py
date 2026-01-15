from abc import ABC, abstractmethod
#TODO add imports for datatyps

class IBasicAuthManger(ABC):

    @abstractmethod
    async def authenticateWithGoogle(token_JWT: TokenModel):
        pass

    @abstractmethod
    async def google_callback(token_JWT: TokenModel):
        pass

    @abstractmethod
    async def verifyEmailToken(request: EmailVerificationSubmitRequest):
        pass

    @abstractmethod
    async def generateEmailVerification(token_JWT: TokenModel):
        pass

    @abstractmethod
    async def completePasswordRecovery(request: PasswordResetSubmitRequest):
        pass

    @abstractmethod
    async def initiatePasswordRecovery(request: PasswordResetRequestRequest):
        pass

    @abstractmethod
    async def user_logout(token_JWT: TokenModel, refresh_token: Annotated[Optional[UUID], Field(
        description="The refresh token to invalidate. If omitted, all sessions will be terminated.")]):
        pass

    @abstractmethod
    async def refreshAccessToken(request: RefreshRequest):
        pass

    @abstractmethod
    async def register(request: SignupRequestRequest):
        pass

    @abstractmethod
    async def authenticate(request: LoginRequest):
        pass