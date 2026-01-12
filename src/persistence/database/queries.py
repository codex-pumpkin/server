from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from src.persistence.database.database import async_session_factory
from src.persistence.database.models import (
    UsersOrm, QuotaOrm, MessagesOrm, ConversationsOrm, LlmModelsOrm, AuthTokensOrm
)
from typing import Optional

class AsyncOrm:

    @staticmethod
    async def get_user_by_email(email:str) -> Optional[UsersOrm]:
        async with async_session_factory() as session:
            query = (
                select(UsersOrm).where(UsersOrm.email == email)
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()
