# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr
from typing import Any, List
from typing_extensions import Annotated
from service.openapi_server.models.conversation_request import ConversationRequest
from service.openapi_server.models.conversation_response import ConversationResponse
from service.openapi_server.models.message_request import MessageRequest
from service.openapi_server.models.message_response import MessageResponse
from service.openapi_server.models.update_conversation_request import UpdateConversationRequest
from service.openapi_server.security_api import get_token_JWT

class BaseConversationsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseConversationsApi.subclasses = BaseConversationsApi.subclasses + (cls,)
    async def conversations_get(
        self,
    ) -> List[ConversationResponse]:
        """Returns a list of all conversations for the current user. """
        ...


    async def conversations_post(
        self,
        conversation_request: ConversationRequest,
    ) -> ConversationResponse:
        """Starts a new conversation with the given message, LLM configuration, and target language. """
        ...


    async def conversations_id_put(
        self,
        id: Annotated[StrictStr, Field(description="ID of the conversation to update")],
        update_conversation_request: UpdateConversationRequest,
    ) -> ConversationResponse:
        """Updates the &#x60;name&#x60; and &#x60;pinned&#x60; attributes of a conversation. """
        ...


    async def conversations_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="Id of the conversation to delete")],
    ) -> None:
        """Deletes the conversation with the given Id. """
        ...


    async def conversations_id_messages_put(
        self,
        id: Annotated[StrictInt, Field(description="Id of the target conversation")],
        message_request: MessageRequest,
    ) -> MessageResponse:
        """Resend a message by providing a new prompt."""
        ...


    async def conversations_id_messages_post(
        self,
        id: Annotated[StrictInt, Field(description="Id of the target conversation")],
        message_request: MessageRequest,
    ) -> MessageResponse:
        """Adds a new message to an existing conversation. """
        ...
