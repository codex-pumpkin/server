import datetime
from token import tok_name

from sqlalchemy.ext.asyncio import AsyncSession

from src.persistence.impl.database.models import (
    TokensOrm,
    TokenType
)

from sqlalchemy import select, update
from src.core.settings import settings
from typing import Optional


async def create_token(session:AsyncSession, user_id:str, token_type:str) -> TokensOrm:
    """Create token."""
    now = datetime.datetime.now(datetime.UTC)
    exp = now + datetime.timedelta(minutes=settings.refresh_settings.expire_time)
    token = TokensOrm(
        expires_at=exp,
        user_id=user_id,
        type=TokenType(token_type)
    )
    session.add(token)
    await session.commit()
    await session.refresh(token)
    return token

async def get_token_by_id(session:AsyncSession, token_id:str) -> Optional[TokensOrm]:
    """Get token by id."""
    query = select(TokensOrm).where(TokensOrm.id == token_id)
    result = await session.execute(query)
    token = result.scalar_one_or_none()
    return token


async def invalidate_all_refresh(session:AsyncSession, user_id:str) -> None:
    """Invalidate all refresh."""
    stmt = (
        update(TokensOrm)
        .where(TokensOrm.user_id == user_id and TokensOrm.type == TokenType.REFRESH)
        .values(valid=False)
    )
    await session.execute(stmt)
    await session.commit()