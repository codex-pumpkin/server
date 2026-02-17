from abc import ABC, abstractmethod

from src.core.dtos import (
    TokenModel,
    UpdateAccountRequest, AccountResponse,
)

from uuid import UUID


class IUserInfoManager(ABC):

    @abstractmethod
    async def get_account_info(self, token_jwt: TokenModel) -> AccountResponse:
        """Get account info."""
        pass

    @abstractmethod
    async def update_user_name_email(self, token_jwt: TokenModel, update_account_request: UpdateAccountRequest):
        """Update user name email."""
        pass

    @abstractmethod
    async def get_profile_picture(self, token_jwt: TokenModel):
        """Get profile picture."""
        pass

    @abstractmethod
    async def update_profile_picture(self, user_id: UUID, image_data: bytes):
        """Update profile picture."""
        pass