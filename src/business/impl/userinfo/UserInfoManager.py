from pathlib import Path
from typing import Optional

from src.business.factory import BusinessFactory
from src.core.dtos import (
    TokenModel,
    UpdateAccountRequest,
    AccountResponse
)

from src.business.interfaces import IUserInfoManager
from src.persistence import PersistenceFactory
from src.core.settings import settings

class UserInfoManager(IUserInfoManager):

    async def get_account_info(self, token_jwt: TokenModel) -> AccountResponse:
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.get_user_by_id(str(token_jwt.sub))

    async def update_user_name_email(self, token_jwt: TokenModel, update_account_request: UpdateAccountRequest):
        repo = await PersistenceFactory.get_entity_repository()
        user = await repo.get_user_by_id(str(token_jwt.sub))

        flag = False
        if user.email != update_account_request.email:
            flag = True

        await repo.change_mail_username(
            user_id=str(token_jwt.sub),
            email=update_account_request.email,
            username=update_account_request.username
        )
        if flag:
            await repo.invalidate_all_refresh_tokens(user_id=str(token_jwt.sub))
            await repo.unverify_user(user_id=str(token_jwt.sub))
            auth_manager = await BusinessFactory.get_basic_auth_manager()
            user = await repo.get_user_by_id(user_id=str(token_jwt.sub))
            await auth_manager.generate_email_verification(user=user)

    async def get_profile_picture(self, token_jwt: TokenModel) -> Optional[bytes]:
        path = Path(settings.pictures_settings.path) / f"{token_jwt.sub}.jpg"
        try:
            with open(path, "rb") as f:
                return f.read()
        except FileNotFoundError:
            return None

    async def update_profile_picture(self, token_jwt: TokenModel, image_data: bytes) -> None:
        path = Path(settings.pictures_settings.path) / f"{token_jwt.sub}.jpg"
        with open(path, "wb") as f:
            f.write(image_data)
            
        