import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dtos import AnalyticsResponse
from src.persistence.impl.database.models import (
    MessagesOrm,
)

from sqlalchemy import select, update, func
from src.core.settings import settings
from typing import Optional, List


async def get_analytics(session: AsyncSession) -> AnalyticsResponse:
    """Get analytics."""
    end_time = datetime.datetime.now(datetime.UTC).replace(tzinfo=None)
    start_time = end_time - datetime.timedelta(hours=24)

    stmt = (
        select(MessagesOrm.created_at)
        .where(MessagesOrm.created_at >= start_time)
        .where(MessagesOrm.created_at < end_time)
    )

    result = await session.execute(stmt)
    timestamps = result.scalars().all()

    usage = [0] * 96

    for created_at in timestamps:
        if created_at is None:
            continue

        delta = created_at - start_time
        seconds = delta.total_seconds()

        if seconds < 0:
            continue

        index = int(seconds // (15 * 60))

        if 0 <= index < 96:
            usage[index] += 1

    return AnalyticsResponse(
        start_time=start_time,
        interval_minutes=15,
        usage=usage
    )
