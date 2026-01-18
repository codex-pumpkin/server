from sqlalchemy import select
from src.persistence.impl.database.database import async_session_factory
from src.persistence.impl.database.models import (
    UsersOrm
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
