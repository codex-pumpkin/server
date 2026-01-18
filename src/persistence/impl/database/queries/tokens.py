import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from src.persistence.impl.database.models import AuthTokensOrm
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