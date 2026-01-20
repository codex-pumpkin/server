from src.core.exceptions import UserConflictError
from src.persistence.impl.database.models import UsersOrm
from src.persistence.interfaces.IEntityRepository import *
from src.persistence.impl.database.database import async_session_factory
from sqlalchemy.exc import IntegrityError
from typing import Optional
from src.persistence.impl.database.hash_util import hash_password, validate_password
from src.persistence.impl.database.queries.user import (
    get_user_by_email_or_username,
    get_user_by_email,
    get_user_by_username,
)

from src.persistence.impl.database.queries.tokens import (
    create_token

)

from src.core.dtos import (
    AccountInfo
)

class EntityRepository(IEntityRepository):

    # --------------------
    # User-related
    # --------------------
    async def get_user(self, user_id: str) -> User: ...
    async def get_user_by_email(self, email: str) -> User: ...


    async def create_user(self, user: SignupRequest) -> AccountInfo:
        user_orm = UsersOrm(
            email=user.email,
            hashed_password=hash_password(user.password),
            username=user.username
        )
        async with async_session_factory() as session:
            try:
                user = await get_user_by_email_or_username(
                    session=session,
                    email=user_orm.email,
                    username=user_orm.username
                )
                if user is not None:
                    field = "email" if user.email == user_orm.email else "username"
                    raise UserConflictError(field=field)

                session.add(user_orm)
                await session.commit()
                await session.refresh(user_orm)
                return user_orm.to_dto()

            except IntegrityError as e:
                await session.rollback()
                error_msg = str(e.orig).lower()
                field = "email" if "email" in error_msg else "username"
                raise UserConflictError(field=field)

    async def update_user(self, user_id: str, email: str, username: str) -> None: ...

    # --------------------
    # Authentication & validation
    # --------------------
    async def authenticate(self, username:Optional[str], email: Optional[str], password: str) -> Optional[AccountResponse]:

        async with async_session_factory() as session:
            user = None
            if email is not None:
                user = await get_user_by_email(session, email)
            if user is None and username is not None:
                user = await get_user_by_username(session, username)
            if user is None:
                return None
            if not validate_password(str(user.hashed_password), password=password):
                return None
            return user.to_dto()


    async def is_user_verified(self, user_id: str) -> bool: ...

    async def is_user_admin(self, user_id: str) -> bool: ...

    async def is_email_taken(self, email: str) -> bool:
        async with async_session_factory() as session:
            user = get_user_by_email(session, email)
            if user is None:
                return False
            return True

    async def is_username_taken(self, username: str) -> bool:
        async with async_session_factory() as session:
            user = get_user_by_username(session, username)
            if user is None:
                return False
            return True

    # --------------------
    # Token-related
    # --------------------
    async def get_token(self, token_id: str) -> str: ...

    async def create_token(self, user_id: str) -> str:
        async with async_session_factory() as session:
            token = await create_token(session=session, user_id=user_id)
            return token.id

    async def change_token(self, token_id: str, token: str) -> None: ...
    async def invalidate_token(self, token_id: str) -> None: ...
    async def is_token_valid(self, token_id: str) -> bool: ...

    # --------------------
    # Chat / Conversation-related
    # --------------------
    async def get_chats(self, user_id: str) -> List[ChatMetaData]: ...
    async def get_chat(self, chat_id: str) -> ChatMetaData: ...
    async def create_chat(self, chat: ChatMetaData) -> str: ...
    async def update_chat(self, chat_id: str, chat: ChatMetaData) -> None: ...

    # --------------------
    # Message-related
    # --------------------
    async def add_message(self, chat_id: str, message: str) -> str: ...
    async def get_messages(self, chat_id: str) -> List[str]: ...
    async def change_last_message(self, chat_id: str, message: str) -> None: ...

    # --------------------
    # LLM Model-related
    # --------------------
    async def add_model(self, model_data: ModelData) -> str: ...
    async def remove_model(self, model_id: str) -> None: ...
    async def change_model(self, model_id: str, model_data: ModelData) -> None: ...
    async def get_model(self, model_id: str) -> ModelData: ...

    # --------------------
    # Quota-related
    # --------------------
    async def change_quota(self, quota: QuotaConfig) -> None: ...
    async def get_quota(self) -> QuotaConfig: ...
    async def get_user_quota_remaining(self, user_id: str, period: date) -> int: ...
    async def is_quota_exceeded(self, user_id: str) -> bool: ...

    # --------------------
    # Analytics / Usage-related
    # --------------------
    async def get_usage_data(self) -> UsageData: ...

    # --------------------
    # Profile Picture
    # --------------------
    async def save_profile_picture(self, user_id: str, file_data: bytes) -> None: ...
    async def get_profile_picture(self, user_id: str) -> bytes: ...
    async def delete_profile_picture(self, user_id: str) -> None: ...
