from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.persistence.impl.database.models import QuotaOrm


async def get_quota(session:AsyncSession) -> QuotaOrm:
    query = select(QuotaOrm)
    res = await session.execute(query)
    return res.scalars().first()

async def set_quota(session:AsyncSession, member_limit, admin_limit):
    stmt = update(QuotaOrm).values(
        member_limit=member_limit,
        admin_limit=admin_limit
    )
    await session.execute(stmt)
    await session.commit()


