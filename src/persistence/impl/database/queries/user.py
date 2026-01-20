
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_

from src.persistence.impl.database.models import UsersOrm
from typing import  Optional


async def get_user_by_email_or_username(session:AsyncSession, email:str, username:str) -> Optional[UsersOrm]:
    query = select(UsersOrm).where(or_(
        UsersOrm.email == email,
        UsersOrm.username == username
    ))
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user

async def get_user_by_email(session:AsyncSession, email:str) -> Optional[UsersOrm]:
    query = select(UsersOrm).where(
        UsersOrm.email == email,
    )
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user


async def get_user_by_username(session:AsyncSession, username:str) -> Optional[UsersOrm]:
    query = select(UsersOrm).where(
        UsersOrm.username == username,
    )
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user

async def get_user_by_id(session:AsyncSession, user_id:str) -> Optional[UsersOrm]:
    query = select(UsersOrm).where(
        UsersOrm.id == user_id,
    )
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user