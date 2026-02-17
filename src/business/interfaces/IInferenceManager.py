from abc import ABC, abstractmethod
from typing import Annotated
from pydantic import Field, StrictInt, StrictStr

from src.core.dtos import (
    TokenModel,
    MessageRequest,
    ConversationRequest,
    ConversationResponse,
    UpdateConversationRequest,
    MessageResponse
)
from uuid import UUID

from typing import List

class IInferenceManager(ABC):

    @abstractmethod
    async def get_conversations_by_user(self, token_jwt: TokenModel) -> List[ConversationResponse]:
        """Get conversations by user."""
        pass

    @abstractmethod
    async def post_message_to_conversation(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="Id of the target conversation")
        ],
        message_request: MessageRequest,
        token_jwt: TokenModel
    ) -> MessageResponse:
        """Post message to conversation."""
        pass

    @abstractmethod
    async def message_regeneration(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="Id of the target conversation")
        ],
        message_request: MessageRequest,
        token_jwt: TokenModel
    ) -> MessageResponse:
        """Message regeneration."""
        pass

    @abstractmethod
    async def remove_conversation(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="Id of the conversation to delete")
        ],
        token_jwt: TokenModel
    ):
        """Remove conversation."""
        pass

    @abstractmethod
    async def start_conversation(
        self,
        token_jwt: TokenModel,
        conversation_request: ConversationRequest
    ) -> ConversationResponse:
        """Start conversation."""
        pass

    @abstractmethod
    async def update_conversation(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="ID of the conversation to update")
        ],
        update_conversation_request: UpdateConversationRequest,
        token_jwt: TokenModel
    ):
        """Update conversation."""
        pass