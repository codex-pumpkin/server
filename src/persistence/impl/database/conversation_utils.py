import uuid

from src.core.dtos import ConversationResponse
from src.persistence.impl.database.queries.conversations import get_chat_messages
from src.persistence.impl.database.models import ConversationsOrm
from sqlalchemy.ext.asyncio import AsyncSession

async def conversation_to_dto(session:AsyncSession, conversation:ConversationsOrm) -> ConversationResponse:
    """Conversation to dto."""
    messages = await get_chat_messages(
        session=session,
        conversation_id=conversation.id,
    )
    messages = [message.to_dto() for message in messages]

    return ConversationResponse(
        id=uuid.UUID(conversation.id),
        name=conversation.name,
        created_at=conversation.created_at.timestamp(),
        updated_at=conversation.updated_at.timestamp(),
        pinned=conversation.is_pinned,
        user_id=uuid.UUID(conversation.user_id),
        llm_model_config_id=conversation.llm_id,
        messages=messages,
        target_language=conversation.target_language
    )