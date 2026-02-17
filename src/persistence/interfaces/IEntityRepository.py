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
    async def get_user_by_id(self, user_id: str) -> Optional[AccountResponse]:
        """Get user by id."""
        ...
    @abstractmethod
    async def get_user_by_email(self, email: str) -> Optional[AccountResponse]:
        """Get user by email."""
        ...
    @abstractmethod
    async def create_user(self, user: SignupRequest) -> AccountResponse:
        """Create user."""
        ...
    @abstractmethod
    async def update_user(self, user_id: str, email: str, username: str) -> None:
        """Update user."""
        ...

    # --------------------
    # Authentication & validation
    # --------------------
    @abstractmethod
    async def authenticate(self, username:Optional[str], email: Optional[str], password: str) -> Optional[AccountResponse]:
        """Authenticate."""
        ...
    @abstractmethod
    async def is_user_verified(self, user_id: str) -> bool:
        """Is user verified."""
        ...
    @abstractmethod
    async def verify_user(self, user_id: str) -> bool:
        """Verify user."""
        ...
    @abstractmethod
    async def unverify_user(self, user_id: str) -> bool:
        """Unverify user."""
        ...
    @abstractmethod
    async def is_user_admin(self, user_id: str) -> bool:
        """Is user admin."""
        ...
    @abstractmethod
    async def is_email_taken(self, email: str) -> bool:
        """Is email taken."""
        ...
    @abstractmethod
    async def is_username_taken(self, username: str) -> bool:
        """Is username taken."""
        ...
    @abstractmethod
    async def change_password(self, user_id: str, new_password: str) -> bool:
        """Change password."""
        ...


    # --------------------
    # Token-related
    # --------------------
    @abstractmethod
    async def get_token(self, token_id: str) -> Optional[TokenInfo]:
        """Get token."""
        ...
    @abstractmethod
    async def create_token(self, user_id: str, token_type:Union[Literal["refresh"], Literal["email"], Literal["password"]]) -> TokenInfo:
        """Create token."""
        ...
    @abstractmethod
    async def change_token(self, token_id: str) -> Optional[TokenInfo]:
        """Change token."""
        ...
    @abstractmethod
    async def invalidate_all_refresh_tokens(self, user_id: str):
        """Invalidate all refresh tokens."""
        ...
    @abstractmethod
    async def invalidate_token(self, token_id: str) -> bool:
        """Invalidate token."""
        ...
    @abstractmethod
    async def is_token_valid(self, token_id: str) -> bool:
        """Is token valid."""
        ...

    # --------------------
    # Chat / Conversation-related
    # --------------------
    @abstractmethod
    async def get_chats(self, user_id: str) -> List[ConversationResponse]:
        """Get chats."""
        ...
    @abstractmethod
    async def get_chat_by_id(self, chat_id: str) -> Optional[ConversationResponse]:
        """Get chat by id."""
        ...
    @abstractmethod
    async def create_chat(self, user_id: str, request: ConversationRequest) -> str:
        """Create chat."""
        ...
    @abstractmethod
    async def update_chat(self, chat_id: str, name: str, is_pinned: bool) -> bool:
        """Update chat."""
        ...
    @abstractmethod
    async def delete_chat(self, chat_id:str) -> bool:
        """Delete chat."""
        ...

    # --------------------
    # Message-related
    # --------------------
    @abstractmethod
    async def add_message(self, chat_id: str, message: Message) -> bool:
        """Add message."""
        ...
    @abstractmethod
    async def get_messages(self, chat_id: str) -> List[MessageResponse]:
        """Get messages."""
        ...
    @abstractmethod
    async def delete_last_message(self, chat_id: str) -> bool:
        """Delete last message."""
        ...

    # --------------------
    # LLM Model-related
    # --------------------
    @abstractmethod
    async def add_model(self, name: str, model_name: str, url: str, key: str) -> str:
        """Add model."""
        ...
    @abstractmethod
    async def remove_model(self, model_id: str) -> None:
        """Remove model."""
        ...
    @abstractmethod
    async def change_model(self, model_id: str, name: str, model_name: str, url: str, key: Optional[str]) -> None:
        """Change model."""
        ...
    @abstractmethod
    async def get_model(self, model_id: str) -> Optional[LLMConfigurationResponse]:
        """Get model."""
        ...
    @abstractmethod
    async def get_llm_configs(self) -> List[LLMConfigurationResponse]:
        """Get llm configs."""
        ...
    @abstractmethod
    async def get_llm_by_chat_id(self, chat_id:str) -> Optional[LLMConfigurationRequest]:
        """Get llm by chat id."""
        ...
    @abstractmethod
    async def get_key_of_model(self, model_id:str) -> Optional[str]:
        """Get key of model."""
        ...

    # --------------------
    # Quota-related
    # --------------------
    @abstractmethod
    async def change_quota(self, quota: QuotaConfig) -> None:
        """Change quota."""
        ...
    @abstractmethod
    async def get_quota(self) -> QuotaConfig:
        """Get quota."""
        ...
    @abstractmethod
    async def get_user_quota_remaining(self, user_id: str) -> int:
        """Get user quota remaining."""
        ...
    @abstractmethod
    async def is_quota_exceeded(self, user_id: str) -> bool:
        """Is quota exceeded."""
        ...

    # --------------------
    # Analytics / Usage-related
    # --------------------
    @abstractmethod
    async def get_usage_data(self) -> UsageData:
        """Get usage data."""
        ...

    # --------------------
    # Profile Picture
    # --------------------
    @abstractmethod
    async def save_profile_picture(self, user_id: str, file_data: bytes) -> None:
        """Save profile picture."""
        ...
    @abstractmethod
    async def get_profile_picture(self, user_id: str) -> bytes:
        """Get profile picture."""
        ...
    @abstractmethod
    async def delete_profile_picture(self, user_id: str) -> None:
        """Delete profile picture."""
        ...
