from abc import ABC, abstractmethod
#TODO add imports for datatyps

class IUserInfoManager(ABC):

    @abstractmethod
    async def update_user_name_email(token_JWT: TokenModel, update_account_request: UpdateAccountRequest):
        pass

    @abstractmethod
    async def get_profile_picture(token_JWT: TokenModel):
        pass

    @abstractmethod
    async def updateProfilePicture(userId: UUID, imageData: Binary):
        pass