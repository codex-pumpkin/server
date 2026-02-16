import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from src.persistence.impl.database.models import (
    LlmModelsOrm,
    ConversationsOrm
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


async def change_llm(
    session:AsyncSession,
    llm_id:str,
    model_name:str,
    name:str,
    url:str,
    key:Optional[str]
):
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
            .values(name=name, url=url, api_key=key, model_name=model_name)
        )
    await session.execute(stmt)
    await session.commit()

async def delete_llm(session:AsyncSession, llm_id:str):
    orm = await get_model_by_id(session=session, llm_id=llm_id)
    if orm is not None:
        await session.delete(orm)
        await session.commit()

async def get_all_llm_configs(session:AsyncSession) -> List[LlmModelsOrm]:
    query = (
        select(LlmModelsOrm)
    )
    result = await session.execute(query)
    return result.scalars().all()

async def get_api_by_conversation_id(
    session: AsyncSession,
    conversation_id: str
) -> Optional[LlmModelsOrm]:
    query = (
        select(LlmModelsOrm)
        .join(
            ConversationsOrm,
            ConversationsOrm.llm_id == LlmModelsOrm.id
        )
        .where(ConversationsOrm.id == conversation_id)
    )
    result = await session.execute(query)
    return result.scalar_one_or_none()

if __name__ == "__main__":
    import asyncio
    from src.persistence.impl.database.database import async_session_factory
    async def main():
        async with async_session_factory() as session:
            llm_configs = await get_api_by_conversation_id(session=session, conversation_id="d14f8a04-229a-4e6e-bd63-8b2d16261235")
            print(llm_configs)

    asyncio.run(main())