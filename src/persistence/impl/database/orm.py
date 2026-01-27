from src.persistence.impl.database.database import Base, sync_engine, session_factory, async_engine
from src.persistence.impl.database.models import UsersOrm, QuotaOrm
import asyncio

def create_tables():
    sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True
    create_quota()

def create_quota():
    quota = QuotaOrm(
        admin_limit=100,
        member_limit=20
    )
    with session_factory() as session:
        session.add(quota)
        session.commit()

def create_user():
    user = UsersOrm(
        email="sad@gmail.com",
        username="ad",
        hashed_password="wasya"
    )
    with session_factory() as session:
        session.add(user)
        session.commit()

async def test():
    await async_engine.dispose()


if __name__ == "__main__":
    create_tables()
    create_user()

    asyncio.run(test())

