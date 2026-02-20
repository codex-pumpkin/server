from typing import Protocol, List, Optional
from datetime import date
from typing_extensions import runtime_checkable
from abc import ABC, abstractmethod

from src.core.dtos import (
    SignupRequest,
    AccountResponse,
    TokenInfo,
    QuotaConfig,
    ConversationResponse,
    MessageResponse,
    Message,
    LLMConfigurationRequest,
    LLMConfigurationResponse,
    ConversationRequest
)
from typing import Literal, Union

class UsageData:
    ...

class IEntityRepository(ABC):
    # --------------------
    # User-related
    # --------------------
    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> Optional[AccountResponse]: ...
    @abstractmethod
    async def get_user_by_email(self, email: str) -> Optional[AccountResponse]: ...
    @abstractmethod
    async def create_user(self, user: SignupRequest) -> AccountResponse: ...
    @abstractmethod
    async def update_user(self, user_id: str, email: str, username: str) -> None: ...

    # --------------------
    # Authentication & validation
    # --------------------
    @abstractmethod
    async def authenticate(self, username:Optional[str], email: Optional[str], password: str) -> Optional[AccountResponse]: ...
    @abstractmethod
    async def is_user_verified(self, user_id: str) -> bool: ...
    @abstractmethod
    async def verify_user(self, user_id: str) -> bool: ...
    @abstractmethod
    async def unverify_user(self, user_id: str) -> bool: ...
    @abstractmethod
    async def is_user_admin(self, user_id: str) -> bool: ...
    @abstractmethod
    async def is_email_taken(self, email: str) -> bool: ...
    @abstractmethod
    async def is_username_taken(self, username: str) -> bool: ...
    @abstractmethod
    async def change_password(self, user_id: str, new_password: str) -> bool: ...


    # --------------------
    # Token-related
    # --------------------
    @abstractmethod
    async def get_token(self, token_id: str) -> Optional[TokenInfo]: ...
    @abstractmethod
    async def create_token(self, user_id: str, token_type:Union[Literal["refresh"], Literal["email"], Literal["password"]]) -> TokenInfo: ...
    @abstractmethod
    async def change_token(self, token_id: str) -> Optional[TokenInfo]: ...
    @abstractmethod
    async def invalidate_all_refresh_tokens(self, user_id: str): ...
    @abstractmethod
    async def invalidate_token(self, token_id: str) -> bool: ...
    @abstractmethod
    async def is_token_valid(self, token_id: str) -> bool: ...

    # --------------------
    # Chat / Conversation-related
    # --------------------
    @abstractmethod
    async def get_chats(self, user_id: str) -> List[ConversationResponse]: ...
    @abstractmethod
    async def get_chat_by_id(self, chat_id: str) -> Optional[ConversationResponse]: ...
    @abstractmethod
    async def create_chat(self, user_id: str, request: ConversationRequest) -> str: ...
    @abstractmethod
    async def update_chat(self, chat_id: str, name: str, is_pinned: bool) -> bool: ...
    @abstractmethod
    async def delete_chat(self, chat_id:str) -> bool: ...

    # --------------------
    # Message-related
    # --------------------
    @abstractmethod
    async def add_message(self, chat_id: str, message: Message) -> bool: ...
    @abstractmethod
    async def get_messages(self, chat_id: str) -> List[MessageResponse]: ...
    @abstractmethod
    async def delete_last_message(self, chat_id: str) -> bool: ...

    # --------------------
    # LLM Model-related
    # --------------------
    @abstractmethod
    async def add_model(self, name: str, model_name: str, url: str, key: str) -> str: ...
    @abstractmethod
    async def remove_model(self, model_id: str) -> None: ...
    @abstractmethod
    async def change_model(self, model_id: str, name: str, model_name: str, url: str, key: Optional[str]) -> None: ...
    @abstractmethod
    async def get_model(self, model_id: str) -> Optional[LLMConfigurationResponse]: ...
    @abstractmethod
    async def get_llm_configs(self) -> List[LLMConfigurationResponse]: ...
    @abstractmethod
    async def get_llm_by_chat_id(self, chat_id:str) -> Optional[LLMConfigurationRequest]: ...
    @abstractmethod
    async def get_key_of_model(self, model_id:str) -> Optional[str]: ...

    # --------------------
    # Quota-related
    # --------------------
    @abstractmethod
    async def change_quota(self, quota: QuotaConfig) -> None: ...
    @abstractmethod
    async def get_quota(self) -> QuotaConfig: ...
    @abstractmethod
    async def get_user_quota_remaining(self, user_id: str) -> int: ...
    @abstractmethod
    async def is_quota_exceeded(self, user_id: str) -> bool: ...

    # --------------------
    # Analytics / Usage-related
    # --------------------
    @abstractmethod
    async def get_usage_data(self) -> UsageData: ...
