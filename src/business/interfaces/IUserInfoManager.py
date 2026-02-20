from abc import ABC, abstractmethod
from typing import Optional

from src.core.dtos import (
    TokenModel,
    UpdateAccountRequest,
    AccountResponse,
)

class IUserInfoManager(ABC):

    @abstractmethod
    async def get_account_info(self, token_jwt: TokenModel) -> AccountResponse:
        pass

    @abstractmethod
    async def update_user_name_email(self, token_jwt: TokenModel, update_account_request: UpdateAccountRequest):
        pass

    @abstractmethod
    async def get_profile_picture(self, token_jwt: TokenModel) -> Optional[bytes]:
        pass

    @abstractmethod
    async def update_profile_picture(self, user_id: TokenModel, image_data: bytes) -> None:
        pass