import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, and_

from src.persistence.database.models import AuthTokensOrm
from typing import  Optional
from src.core.settings import settings

async def create_token(session:AsyncSession, user_id:str) -> AuthTokensOrm:
    now = datetime.datetime.now(datetime.UTC)
    exp = now + datetime.timedelta(settings.refresh_settings.expire_time)
    token = AuthTokensOrm(
        expires_at=exp,
        user_id=user_id
    )
    session.add(token)
    await session.commit()
    await session.refresh(token)
    return token