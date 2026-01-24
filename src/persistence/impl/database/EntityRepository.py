import datetime

from src.core.exceptions import UserConflictError
from src.persistence.impl.database.models import UsersOrm, TokensOrm
from src.persistence.interfaces.IEntityRepository import *
from src.persistence.impl.database.database import async_session_factory
from sqlalchemy.exc import IntegrityError
from typing import Optional, Literal, Union
from src.persistence.impl.database.hash_util import hash_password, validate_password
from src.persistence.impl.database.queries.user import (
    get_user_by_email_or_username,
    get_user_by_email,
    get_user_by_username,
    get_user_by_id
)

from src.persistence.impl.database.queries.tokens import (
    create_token,
    get_token_by_id, invalidate_all_refresh
)

from src.core.dtos import (
    AccountResponse,
    AccountResponse, TokenInfo,
)

class EntityRepository(IEntityRepository):

    # --------------------
    # User-related
    # --------------------
    async def get_user_by_id(self, user_id: str) -> Optional[AccountResponse]:
        async with async_session_factory() as session:
            user = await get_user_by_id(session, user_id)
            if user is None:
                return None
            return user.to_dto()

    async def get_user_by_email(self, email: str) -> Optional[AccountResponse]:
        async with async_session_factory() as session:
            user = await get_user_by_email(session, email)
            if user is None:
                return None
            return user.to_dto()

    async def create_user(self, user: SignupRequest) -> AccountResponse:
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
                user = await get_user_by_email(session=session, email=email)
            if user is None and username is not None:
                user = await get_user_by_username(session=session, username=username)
            if user is None:
                return None
            if not validate_password(hashed=str(user.hashed_password), password=password):
                return None
            return user.to_dto()


    async def is_user_verified(self, user_id: str) -> bool:
        async with async_session_factory() as session:
            user = await get_user_by_id(session=session, user_id=user_id)
            if user is None:
                return False
            return user.is_verified

    async def verify_user(self, user_id: str) -> bool:
        async with async_session_factory() as session:
            user = await get_user_by_id(session=session, user_id=user_id)
            if not user:
                return False
            user.is_verified = True
            await session.commit()
            return True

    async def is_user_admin(self, user_id: str) -> bool:
        async with async_session_factory() as session:
            user = await get_user_by_id(session=session, user_id=user_id)
            if user is None:
                return False
            return user.is_admin

    async def is_email_taken(self, email: str) -> bool:
        async with async_session_factory() as session:
            user = await get_user_by_email(session=session, email=email)
            if user is None:
                return False
            return True

    async def is_username_taken(self, username: str) -> bool:
        async with async_session_factory() as session:
            user = await get_user_by_username(session=session, username=username)
            if user is None:
                return False
            return True

    async def change_password(self, user_id: str, new_password: str) -> bool:
        async with async_session_factory() as session:
            user = await get_user_by_id(session=session, user_id=user_id)
            if user is None:
                return False
            user.hashed_password = hash_password(password=new_password)
            await session.commit()
            return True

    # --------------------
    # Token-related
    # --------------------
    async def get_token(self, token_id: str) -> Optional[TokenInfo]:
        async with async_session_factory() as session:
            token = await get_token_by_id(session=session, token_id=token_id)
            if token is None:
                return None
            return token.to_dto()

    async def create_token(self, user_id: str, token_type:Union[Literal["refresh"], Literal["email"], Literal["password"]]) -> TokenInfo:
        async with async_session_factory() as session:
            token = await create_token(session=session, user_id=user_id, token_type=token_type)
            return token.to_dto()

    async def change_token(self, token_id: str) -> Optional[TokenInfo]:
        async with async_session_factory() as session:
            token = await get_token_by_id(session=session, token_id=token_id)
            if token is None:
                return None
            token.valid = False
            new_token = TokensOrm(
                type=token.type,
                expires_at=token.expires_at,
                valid=True,
                user_id=token.user_id
            )
            session.add(new_token)
            await session.commit()
            await session.refresh(new_token)
            return new_token.to_dto()

    async def invalidate_all_refresh_tokens(self, user_id:str):
        async with async_session_factory() as session:
            await invalidate_all_refresh(session=session, user_id=user_id)

    async def invalidate_token(self, token_id: str) -> bool:
        async with async_session_factory() as session:
            token = await get_token_by_id(session=session, token_id=token_id)
            if token is None:
                return False
            token.valid = False
            await session.commit()
            return True

    async def is_token_valid(self, token_id: str) -> bool:
        async with async_session_factory() as session:
            token = await get_token_by_id(session=session, token_id=token_id)
            if token is None:
                return False
            if not token.valid or token.expires_at.timestamp() < datetime.datetime.now(datetime.UTC).timestamp():
                return False
            return True

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
