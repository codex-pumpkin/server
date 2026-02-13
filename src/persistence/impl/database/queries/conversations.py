import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from src.persistence.impl.database.models import (
    ConversationsOrm,
    MessagesOrm,
)

from sqlalchemy import select, update
from src.core.settings import settings
from typing import Optional, List


async def get_chats(session:AsyncSession, user_id:str) -> List[ConversationsOrm]:
    query = (
        select(ConversationsOrm)
        .where(ConversationsOrm.user_id == user_id)
        .order_by(ConversationsOrm.is_pined.desc(), ConversationsOrm.updated_at.desc())
    )
    result = await session.execute(query)
    return list(result.scalars().all())

async def get_chat(session:AsyncSession, conversation_id:str) -> List[MessagesOrm]:
    query = (
        select(MessagesOrm)
        .where(MessagesOrm.conversation_id == conversation_id)
        .order_by(MessagesOrm.created_at.desc())
    )
    result = await session.execute(query)
    return list(result.scalars().all())