
from src.core.dtos import (
    TokenModel,
    UpdateAccountRequest,
)

from src.business.interfaces import IUserInfoManager



class UserInfoManager(IUserInfoManager):

    async def update_user_name_email(self, token_jwt: TokenModel, update_account_request: UpdateAccountRequest):
        pass

    async def get_profile_picture(self, token_jwt: TokenModel):
        pass

    async def update_profile_picture(self, user_id: str, image_data: bytes):
        pass