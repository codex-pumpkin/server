from src.business.factory import BusinessFactory
from src.core.dtos import (
    TokenModel,
    UpdateAccountRequest,
    AccountResponse
)

from src.business.interfaces import IUserInfoManager
from src.persistence import PersistenceFactory


class UserInfoManager(IUserInfoManager):

    async def get_account_info(self, token_jwt: TokenModel) -> AccountResponse:
        """Get account info."""
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.get_user_by_id(str(token_jwt.sub))

    async def update_user_name_email(self, token_jwt: TokenModel, update_account_request: UpdateAccountRequest):
        """Update user name email."""
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.get_user_by_id(str(token_jwt.sub))

        flag = False
        if user.email != update_account_request.email:
            flag = True

        await repo.update_user(
            user_id=str(token_jwt.sub),
            email=update_account_request.email,
            username=update_account_request.username
        )
        if flag:
            await repo.invalidate_all_refresh_tokens(user_id=str(token_jwt.sub))
            await repo.unverify_user(user_id=str(token_jwt.sub))
            auth_manager = await BusinessFactory.get_basic_auth_manager()
            user = await repo.get_user_by_id(user_id=str(token_jwt.sub))
            await auth_manager.generate_email_verification(user.id, user.email)

    async def get_profile_picture(self, token_jwt: TokenModel):
        """Get profile picture."""
        pass

    async def update_profile_picture(self, token_jwt: TokenModel, image_data: bytes):
        """Update profile picture."""
        pass