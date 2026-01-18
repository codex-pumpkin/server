from typing import Annotated
from pydantic import Field, StrictInt, StrictStr

from src.core.dtos import (
    TokenModel,
    MessageRequest,
    ConversationRequest,
    UpdateConversationRequest
)

from src.business.interfaces import IInferenceManager


class InferenceManager(IInferenceManager):

    async def get_conversations_by_user(self, token_jwt: TokenModel):
        pass

    async def post_message_to_conversation(self, id: Annotated[StrictInt, Field(
        description="Id of the target conversation")], message_request: MessageRequest, token_jwt: TokenModel):
        pass

    async def message_regeneration(self, id: Annotated[StrictInt, Field(
        description="Id of the target conversation")], message_request: MessageRequest, token_jwt: TokenModel):
        pass

    async def remove_conversation(self, id: Annotated[
        StrictStr, Field(description="Id of the conversation to delete")], token_jwt: TokenModel):
        pass

    async def start_conversation(self, token_jwt: TokenModel, conversation_request: ConversationRequest):
        pass

    async def update_conversation(self, id: Annotated[StrictStr, Field(
        description="ID of the conversation to update")], update_conversation_request: UpdateConversationRequest, token_jwt: TokenModel):
        pass