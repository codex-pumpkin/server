import datetime

from src.core.exceptions import UserConflictError
from src.persistence.impl.database.models import (
    UsersOrm,
    TokensOrm,
    MessagesOrm,
    LlmModelsOrm,
    ConversationsOrm
)
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
    get_token_by_id,
    invalidate_all_refresh
)

from src.persistence.impl.database.queries.quota import (
    get_quota,
    set_quota
)

from src.persistence.impl.database.queries.conversations import (
    get_chats,
    get_chat_messages,
    get_chat_by_id,
    update_conversation,
    update_conversation_update_time,
    get_messages_sent_today_by_user
)

from src.persistence.impl.database.queries.llm import (
    get_model_by_id,
    change_llm,
    delete_llm,
    get_all_llm_configs,
    get_api_by_conversation_id
)

from src.core.dtos import (
    AccountResponse,
    AccountResponse,
    TokenInfo,
    QuotaConfig,
    ConversationResponse,
    LLMConfigurationRequest,
    MessageResponse, 
    AnalyticsResponse
)

from src.persistence.impl.database.queries.analytics import get_analytics

from src.persistence.impl.database.conversation_utils import conversation_to_dto

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
                existing_user = await get_user_by_email_or_username(
                    session=session,
                    email=user_orm.email,
                    username=user_orm.username,
                )

                if existing_user:
                    if existing_user.is_verified:
                        if existing_user.email == user.email:
                            raise UserConflictError(field="email")
                        if existing_user.username == user.username:
                            raise UserConflictError(field="username")

                    existing_user.email = user.email
                    existing_user.username = user.username
                    existing_user.hashed_password = hash_password(user.password)

                    await session.commit()
                    await session.refresh(existing_user)
                    return existing_user.to_dto()

                session.add(user_orm)
                await session.commit()
                await session.refresh(user_orm)
                return user_orm.to_dto()

            except IntegrityError as e:
                await session.rollback()
                error_msg = str(e.orig).lower()
                field = "email" if "email" in error_msg else "username"
                raise UserConflictError(field=field)

    async def update_user(self, user_id: str, email: str, username: str) -> bool:
        async with async_session_factory() as session:
            user = await get_user_by_id(session=session, user_id=user_id)
            user.email = email
            user.username = username
            await session.commit()
            return True

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

    async def unverify_user(self, user_id:str) -> bool:
        async with async_session_factory() as session:
            user = await get_user_by_id(session=session, user_id=user_id)
            if user is None:
                return False
            user.is_verified = False
            await session.commit()
            return True

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
    async def get_chats(self, user_id: str) -> List[ConversationResponse]:
        async with async_session_factory() as session:
            chat_list = await get_chats(
                session=session,
                user_id=user_id
            )
            return [await conversation_to_dto(
                session=session, conversation=orm
            ) for orm in chat_list]


    async def get_chat_by_id(self, chat_id: str) -> Optional[ConversationResponse]:
        async with async_session_factory() as session:
            chat = await get_chat_by_id(session=session, conversation_id=chat_id)
            if chat is None:
                return None
            return await conversation_to_dto(session=session, conversation=chat)


    async def create_chat(self, user_id: str, request: ConversationRequest) -> str:
        async with async_session_factory() as session:
            chat_orm = ConversationsOrm(
                name=request.name,
                llm_id=request.llm_model_config_id,
                target_language=request.target_language,
                user_id=user_id
            )
            session.add(chat_orm)
            await session.commit()
            await session.refresh(chat_orm)
            return chat_orm.id

    async def update_chat(self, chat_id: str, name: str, is_pinned: bool) -> bool:
        async with async_session_factory() as session:
            chat = await get_chat_by_id(
                session=session,
                conversation_id=chat_id
            )
            if chat is None:
                return False

            await update_conversation(
                session=session,
                conversation_id=chat_id,
                name=name,
                is_pinned=is_pinned
            )
            return True

    async def delete_chat(self, chat_id:str) -> bool:
        async with async_session_factory() as session:
            chat = await get_chat_by_id(
                session=session,
                conversation_id=chat_id
            )
            if chat is None:
                return False

            await session.delete(chat)
            await session.commit()
            return True

    # --------------------
    # Message-related
    # --------------------
    async def add_message(self, chat_id: str, message: Message) -> bool:
        async with async_session_factory() as session:
            orm = MessagesOrm(
                prompt=message.message,
                response=message.response,
                graph=message.graph,
                generation_ms=message.generation_millis,
                conversation_id=message.conversation_id
            )
            session.add(orm)
            await session.commit()

            await update_conversation_update_time(
                session=session,
                conversation_id=chat_id
            )
            return True

    async def get_messages(self, chat_id: str) -> List[MessageResponse]:
        async with async_session_factory() as session:
            messages_orm = await get_chat_messages(session=session, conversation_id=chat_id)
            messages_dto = [message.to_dto() for message in messages_orm]
            return messages_dto


    async def delete_last_message(self, chat_id: str) -> bool:
        async with async_session_factory() as session:
            messages = await get_chat_messages(session=session, conversation_id=chat_id)
            last = messages[-1]
            last.conversation_id = None
            await session.commit()
            return True

    # --------------------
    # LLM Model-related
    # --------------------
    async def add_model(self, name:str, url:str, key:str) -> str:
        async with async_session_factory() as session:
            orm = LlmModelsOrm(
                name=name,
                url=url,
                api_key=key
            )
            session.add(orm)
            await session.commit()
            await session.refresh(orm)
            return orm.id

    async def remove_model(self, model_id: str) -> None:
        async with async_session_factory() as session:
            await delete_llm(session=session, llm_id=model_id)

    async def change_model(self, model_id: str, name:str, url:str, key:Optional[str]) -> None:
        async with async_session_factory() as session:
            await change_llm(
                session=session,
                llm_id=model_id,
                name=name,
                url=url,
                key=key
            )

    async def get_model(self, model_id: str) -> Optional[LLMConfigurationResponse]:
        async with async_session_factory() as session:
            llm_config = await get_model_by_id(session=session, llm_id=model_id)
            if llm_config is None:
                return llm_config
            return llm_config.to_dto()

    async def get_key_of_model(self, model_id:str) -> Optional[str]:
        async with async_session_factory() as session:
            llm_config = await get_model_by_id(session=session, llm_id=model_id)
            if llm_config is None:
                return None
            return llm_config.api_key

    async def get_llm_configs(self) -> List[LLMConfigurationResponse]:
        async with async_session_factory() as session:
            orm_configs = await get_all_llm_configs(session)
            dto_configs = [config.to_dto() for config in orm_configs]
            return dto_configs

    async def get_llm_by_chat_id(self, chat_id:str) -> Optional[LLMConfigurationRequest]:
        async with async_session_factory() as session:
            llm_model = await get_api_by_conversation_id(
                session=session,
                conversation_id=chat_id
            )
            if llm_model is None:
                return None
            return llm_model.to_dto_request()


    # --------------------
    # Quota-related
    # --------------------
    async def change_quota(self, quota: QuotaConfig) -> None:
        async with async_session_factory() as session:
            await set_quota(
                session=session,
                admin_limit=quota.admin,
                member_limit=quota.member
            )

    async def get_quota(self) -> QuotaConfig:
        async with async_session_factory() as session:
            quota_orm = await get_quota(session=session)
            return quota_orm.to_dto()

    async def get_user_quota_remaining(self, user_id: str) -> int:
        async with async_session_factory() as session:
            res = await get_messages_sent_today_by_user(session=session, user_id=user_id)
            user = await self.get_user_by_id(user_id=user_id)
            quota = await self.get_quota()
            daily_quota = quota.admin if user.is_admin else quota.member
            return max(0, daily_quota - res)

    async def is_quota_exceeded(self, user_id: str) -> bool:
        return (await self.get_user_quota_remaining(user_id=user_id)) == 0

    # --------------------
    # Analytics / Usage-related
    # --------------------
    async def get_usage_data(self) -> AnalyticsResponse:
        async with async_session_factory() as session:
            return await get_analytics(session=session)

    # --------------------
    # Profile Picture
    # --------------------
    async def save_profile_picture(self, user_id: str, file_data: bytes) -> None: ...
    async def get_profile_picture(self, user_id: str) -> bytes: ...
    async def delete_profile_picture(self, user_id: str) -> None: ...
