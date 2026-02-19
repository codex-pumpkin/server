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

from src.core.dtos import TokenModel  # noqa: F401
from pydantic import Field
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
    """
    Return all conversations for the authenticated user.

    @param
        token_jwt (TokenModel): Authenticated user token payload.
        inference_manger (IInferenceManager): Business manager used to load conversations.

    @return
        List[ConversationResponse]: Conversation list for the current user.
    """
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
    """
    Start a new conversation for authenticated or guest flow.

    @param
        conversation_request (ConversationRequest): Payload containing initial message and model metadata.
        token_jwt (Optional[TokenModel]): Optional authenticated token payload.
        inference_manger (IInferenceManager): Business manager used to create conversation.

    @return
        ConversationResponse: Created conversation with initial response message.
    """
    return await inference_manger.start_conversation(
        token_jwt=token_jwt,
        conversation_request=conversation_request
    )


@router.put(
    "/conversations/{conversation_id}",
    responses={
        200: {"description": "Conversation updated successfully"},
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
) -> None:
    """
    Update conversation metadata such as name and pinned state.

    @param
        conversation_id (UUID): Identifier of conversation to update.
        update_conversation_request (UpdateConversationRequest): Payload with editable fields.
        token_jwt (TokenModel): Authenticated user token payload.
        inference_manger (IInferenceManager): Business manager used to apply update.

    @return
        None: Persists conversation metadata changes.
    """
    return await inference_manger.update_conversation(
        conversation_id=conversation_id,
        update_conversation_request=update_conversation_request,
        token_jwt=token_jwt
    )


@router.delete(
    "/conversations/{conversation_id}",
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
    """
    Delete a specific conversation for the authenticated user.

    @param
        conversation_id (UUID): Identifier of conversation to delete.
        token_jwt (TokenModel): Authenticated user token payload.
        inference_manger (IInferenceManager): Business manager used to remove conversation.

    @return
        None: Deletes the target conversation.
    """
    return await inference_manger.remove_conversation(
        conversation_id=conversation_id,
        token_jwt=token_jwt
    )

@router.put(
    "/conversations/{conversation_id}/messages",
    responses={
        200: {"model": MessageResponse, "description": "Message changed successfully"},
        401: {"description": "User not authenticated"},
        403: {"description": "User does not have permission to delete this conversation or conversation not found"},
    },
    tags=["Conversations"],
    summary="Regenerate a message.",
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
    """
    Regenerate the last assistant response in a conversation.

    @param
        conversation_id (UUID): Identifier of target conversation.
        message_request (MessageRequest): Payload with prompt used for regeneration.
        token_jwt (TokenModel): Authenticated user token payload.
        inference_manger (IInferenceManager): Business manager used to regenerate message.

    @return
        MessageResponse: Regenerated message response saved to conversation.
    """
    return await inference_manger.message_regeneration(
        token_jwt=token_jwt,
        conversation_id=conversation_id,
        message_request=message_request
    )


@router.post(
    "/conversations/{conversation_id}/messages",
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
    conversation_id: UUID = Path(
        ...,
        description="Id of the target conversation"
    ),
    message_request: MessageRequest = Body(None, description=""),
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory
    ),
    inference_manger: IInferenceManager = Depends(get_inference_manager)
) -> MessageResponse:
    """
    Add a follow-up message to an existing conversation.

    @param
        conversation_id (UUID): Identifier of target conversation.
        message_request (MessageRequest): Payload with user message content.
        token_jwt (TokenModel): Authenticated user token payload.
        inference_manger (IInferenceManager): Business manager used to generate and store response.

    @return
        MessageResponse: Newly created message response pair.
    """
    return await inference_manger.post_message_to_conversation(
        token_jwt=token_jwt,
        conversation_id=conversation_id,
        message_request=message_request
    )

