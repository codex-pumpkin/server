import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from src.persistence.impl.database.models import (
    ConversationsOrm,
    MessagesOrm,
)

from sqlalchemy import select, update, func
from src.core.settings import settings
from typing import Optional, List


async def get_chats(session:AsyncSession, user_id:str) -> List[ConversationsOrm]:
    query = (
        select(ConversationsOrm)
        .where(ConversationsOrm.user_id == user_id)
        .order_by(ConversationsOrm.is_pinned.desc(), ConversationsOrm.updated_at.desc())
    )
    result = await session.execute(query)
    return list(result.scalars().all())

async def get_chat_messages(session:AsyncSession, conversation_id:str) -> List[MessagesOrm]:
    query = (
        select(MessagesOrm)
        .where(MessagesOrm.conversation_id == conversation_id)
        .order_by(MessagesOrm.created_at.desc())
    )
    result = await session.execute(query)
    return list(result.scalars().all())

async def get_chat_by_id(session:AsyncSession, conversation_id:str) -> Optional[ConversationsOrm]:
    query = (
        select(ConversationsOrm)
        .where(ConversationsOrm.id == conversation_id)
    )
    result = await session.execute(query)
    chat = result.scalar_one_or_none()
    return chat


async def update_conversation(session:AsyncSession, conversation_id:str, name:str, is_pinned:bool) -> None:
    stmt = (
        update(ConversationsOrm)
        .where(ConversationsOrm.id == conversation_id)
        .values(name=name, is_pinned=is_pinned)
    )
    await session.execute(stmt)
    await session.commit()

async def update_conversation_update_time(session:AsyncSession, conversation_id:str) -> None:
    stmt = (
        update(ConversationsOrm)
        .where(ConversationsOrm.id == conversation_id)
        .values(updated_at=datetime.datetime.now(datetime.UTC))
    )
    await session.execute(stmt)
    await session.commit()


async def get_messages_sent_today_by_user(session:AsyncSession, user_id:str) -> int:
    now = datetime.datetime.now(datetime.UTC)
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)

    query = (
        select(func.count())
        .select_from(MessagesOrm)
        .join(ConversationsOrm, MessagesOrm.conversation_id == ConversationsOrm.id)
        .where(
            ConversationsOrm.user_id == user_id,
            MessagesOrm.created_at >= start_of_day,
        )
    )

    result = await session.execute(query)
    return result.scalar_one()