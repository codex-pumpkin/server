import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from src.persistence.impl.database.models import (
    LlmModelsOrm
)

from sqlalchemy import select, update
from src.core.settings import settings
from typing import Optional, List

async def get_model_by_id(session:AsyncSession, llm_id:str) -> Optional[LlmModelsOrm]:
    query = (
        select(LlmModelsOrm)
        .where(LlmModelsOrm.id == llm_id)
    )
    result = await session.execute(query)
    llm_config = result.scalar_one_or_none()
    return llm_config


async def change_llm(session:AsyncSession, llm_id:str, name:str, url:str, key:Optional[str]):
    if key is None:
        stmt = (
            update(LlmModelsOrm)
            .where(LlmModelsOrm.id == llm_id)
            .values(name=name, url=url)
        )
    else:
        stmt = (
            update(LlmModelsOrm)
            .where(LlmModelsOrm.id == llm_id)
            .values(name=name, url=url, api_key=key)
        )
    await session.execute(stmt)

async def delete_llm(session:AsyncSession, llm_id:str):
    orm = get_model_by_id(session=session, llm_id=llm_id)
    if orm is not None:
        await session.delete(orm)