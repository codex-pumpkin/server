
from src.core.dtos import ConversationResponse
from src.persistence.impl.database.queries.conversations import get_chat
from src.persistence.impl.database.models import ConversationsOrm
from sqlalchemy.ext.asyncio import AsyncSession

async def conversation_to_dto(session:AsyncSession, conversation:ConversationsOrm) -> ConversationResponse:
    messages = await get_chat(
        session=session,
        conversation_id=conversation.id,
    )
    messages = [message.to_dto() for message in messages]

    return ConversationResponse(
        id=conversation.id,
        created_at=conversation.created_at,
        updated_at=conversation.updated_at,
        pinned=conversation.is_pined,
        llm_model_config_id=conversation.llm_id,
        messages=messages,
        target_language=conversation.target_language
    )