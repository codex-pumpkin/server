# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

#TODO: businesslogic needs to implement IInterface Manager
from src.business.logic_interfaces.IInferenceManger import IInferenceManger

from src.service.openapi_server.dependencies import get_inference_manager


from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictInt, StrictStr
from typing import Any, List
from typing_extensions import Annotated
from service.openapi_server.models.conversation_request import ConversationRequest
from service.openapi_server.models.conversation_response import ConversationResponse
from service.openapi_server.models.message_request import MessageRequest
from service.openapi_server.models.message_response import MessageResponse
from service.openapi_server.models.update_conversation_request import UpdateConversationRequest
from service.openapi_server.security_api import get_token_JWT

router = APIRouter()



@router.get(
    "/conversations",
    responses={
        200: {"model": List[ConversationResponse], "description": "List of conversations retrieved successfully"},
        401: {"description": "User not authenticated"},
    },
    tags=["Conversations"],
    summary="Get all conversations for the authenticated user",
    response_model_by_alias=True,
)
async def conversations_get(
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> List[ConversationResponse]:
    """Returns a list of all conversations for the current user. """
    inference_manger : IInferenceManger = Depends(get_inference_manager())
    return await inference_manger.getConversationsByUser(token_JWT)


@router.post(
    "/conversations",
    responses={
        201: {"model": ConversationResponse, "description": "Conversation created successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
        429: {"description": "Quota exceeded"},
    },
    tags=["Conversations"],
    summary="Create a new conversation",
    response_model_by_alias=True,
)
async def conversations_post(
    conversation_request: ConversationRequest = Body(None, description=""),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> ConversationResponse:
    """Starts a new conversation with the given message, LLM configuration, and target language. """
    inference_manger : IInferenceManger = Depends(get_inference_manager())
    return await inference_manger.startConversation(token_JWT, conversation_request)


@router.put(
    "/conversations/{id}",
    responses={
        200: {"model": ConversationResponse, "description": "Conversation updated successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
        403: {"description": "User does not have permission to update this conversation or conversation now found"},
    },
    tags=["Conversations"],
    summary="Update conversation metadata",
    response_model_by_alias=True,
)
async def conversations_id_put(
    id: Annotated[StrictStr, Field(description="ID of the conversation to update")] = Path(..., description="ID of the conversation to update"),
    update_conversation_request: UpdateConversationRequest = Body(None, description=""),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> ConversationResponse:
    """Alters metadata of a conversation, such as its name or pinned state."""
    inference_manger : IInferenceManger = Depends(get_inference_manager())
    return await inference_manger.update_conversation(token_JWT.user_id, id, update_conversation_request)


@router.delete(
    "/conversations/{id}",
    responses={
        204: {"description": "Conversation deleted successfully"},
        401: {"description": "User not authenticated"},
        403: {"description": "User does not have permission to delete this conversation or conversation not found"},
    },
    tags=["Conversations"],
    summary="Delete a conversation",
    response_model_by_alias=True,
)
async def conversations_id_delete(
    id: Annotated[StrictStr, Field(description="Id of the conversation to delete")] = Path(..., description="Id of the conversation to delete"),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> None:
    """Deletes the conversation with the given Id. """
    inference_manger : IInferenceManger = Depends(get_inference_manager())
    return await inference_manger.removeConversation(token_JWT, id)

@router.put(
    "/conversations/{id}/messages",
    responses={
        200: {"model": MessageResponse, "description": "Message changed successfully"},
    },
    tags=["Conversations"],
    summary="Regenerate a message.",
    response_model_by_alias=True,
)
async def conversations_id_messages_put(
    id: Annotated[StrictInt, Field(description="Id of the target conversation")] = Path(..., description="Id of the target conversation"),
    message_request: MessageRequest = Body(None, description=""),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> MessageResponse:
    """Resend a message by providing a new prompt."""
    inference_manger : IInferenceManger = Depends(get_inference_manager())
    return await inference_manger.message_regeneration(token_JWT, id, message_request)


@router.post(
    "/conversations/{id}/messages",
    responses={
        200: {"model": MessageResponse, "description": "Message added successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
        403: {"description": "User does not have access to this conversation or conversation was not found"},
        429: {"description": "Quota exceeded"},
    },
    tags=["Conversations"],
    summary="Add a follow-up message to an existing conversation",
    response_model_by_alias=True,
)
async def conversations_id_messages_post(
    id: Annotated[StrictInt, Field(description="Id of the target conversation")] = Path(..., description="Id of the target conversation"),
    message_request: MessageRequest = Body(None, description=""),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> MessageResponse:
    """Adds a new message to an existing conversation. """
    inference_manger : IInferenceManger = Depends(get_inference_manager())
    return await inference_manger.post_message_to_conversation(token_JWT, id, message_request)

