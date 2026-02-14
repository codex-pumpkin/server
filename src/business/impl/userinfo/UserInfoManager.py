
from src.core.dtos import (
    TokenModel,
    UpdateAccountRequest,
    AccountResponse
)

from src.business.interfaces import IUserInfoManager
from src.persistence import PersistenceFactory


class UserInfoManager(IUserInfoManager):

    async def get_account_info(self, token_jwt: TokenModel) -> AccountResponse:
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.get_user_by_id(str(token_jwt.sub))

    async def update_user_name_email(self, token_jwt: TokenModel, update_account_request: UpdateAccountRequest):
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.change_mail_username(
            user_id=str(token_jwt.sub),
            email=update_account_request.email,
            username=update_account_request.username
        )

    async def get_profile_picture(self, token_jwt: TokenModel):
        pass

    async def update_profile_picture(self, token_jwt: TokenModel, image_data: bytes):
        pass