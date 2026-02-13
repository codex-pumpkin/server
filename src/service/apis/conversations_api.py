# coding: utf-8

from typing import Dict, List, Optional  # noqa: F401

from src.business.interfaces import IInferenceManager

from src.service.dependencies import get_inference_manager


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

from uuid import UUID

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictInt, StrictStr
from typing import List
from typing_extensions import Annotated
from src.service.security_api import (
    get_token_jwt,
    get_token_jwt_mandatory
)

from src.core.dtos import (
    ConversationRequest,
    ConversationResponse,
    MessageRequest,
    MessageResponse,
    UpdateConversationRequest
)
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
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory
    ),
    inference_manger : IInferenceManager = Depends(get_inference_manager)
) -> List[ConversationResponse]:
    """Returns a list of all conversations for the current user. """
    return await inference_manger.get_conversations_by_user(token_jwt)


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
    token_jwt: Optional[TokenModel] = Security(
        get_token_jwt
    ),
    inference_manger: IInferenceManager = Depends(get_inference_manager)
) -> ConversationResponse:
    """Starts a new conversation with the given message, LLM configuration, and target language. """
    return await inference_manger.start_conversation(
        token_jwt=token_jwt,
        conversation_request=conversation_request
    )


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
    conversation_id: Annotated[
        UUID,
        Field(description="Id of the conversation to modify")
    ] = Path(
        ...,
        description="Id of the conversation to modify"
    ),
    update_conversation_request: UpdateConversationRequest = Body(None, description=""),
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory
    ),
    inference_manger: IInferenceManager = Depends(get_inference_manager)
) -> ConversationResponse:
    """Alters metadata of a conversation, such as its name or pinned state."""
    return await inference_manger.update_conversation(
        id=conversation_id,
        update_conversation_request=update_conversation_request,
        token_jwt=token_jwt
    )


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
    conversation_id: Annotated[
        UUID,
        Field(description="Id of the conversation to delete")
    ] = Path(
        ...,
        description="Id of the conversation to delete"
    ),
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory
    ),
    inference_manger: IInferenceManager = Depends(get_inference_manager)
) -> None:
    """Deletes the conversation with the given Id. """
    return await inference_manger.remove_conversation(
        token_jwt=token_jwt,
        id=conversation_id
    )

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
    conversation_id: Annotated[
        UUID,
        Field(description="Id of the target conversation")
    ] = Path(
        ...,
        description="Id of the target conversation"
    ),
    message_request: MessageRequest = Body(None, description=""),
    token_jwt: TokenModel = Security(
        get_token_jwt
    ),
    inference_manger: IInferenceManager = Depends(get_inference_manager)

) -> MessageResponse:
    """Resend a message by providing a new prompt."""
    return await inference_manger.message_regeneration(
        token_jwt=token_jwt,
        id=conversation_id,
        message_request=message_request
    )


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
    conversation_id: Annotated[
        UUID,
        Field(description="Id of the target conversation")
    ] = Path(
        ...,
        description="Id of the target conversation"
    ),
    message_request: MessageRequest = Body(None, description=""),
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory
    ),
    inference_manger: IInferenceManager = Depends(get_inference_manager)
) -> MessageResponse:
    """Adds a new message to an existing conversation. """
    return await inference_manger.post_message_to_conversation(
        token_jwt=token_jwt,
        id=conversation_id,
        message_request=message_request
    )

