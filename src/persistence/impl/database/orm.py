from src.persistence.impl.database.database import Base, sync_engine, session_factory, async_engine
from src.persistence.impl.database.models import UsersOrm, QuotaOrm
import asyncio
from src.persistence.impl.database.hash_util import hash_password

def create_tables():
    sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True
    create_quota()
    create_user()

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
        email="123",
        username="123",
        hashed_password=hash_password("123"),
        is_verified=True,
        is_admin=True,
    )
    user1 = UsersOrm(
        email="string",
        username="string",
        hashed_password=hash_password("string"),
        is_verified=True,
        is_admin=False,
    )
    with session_factory() as session:
        session.add(user)
        session.add(user1)
        session.commit()

async def test():
    await async_engine.dispose()


if __name__ == "__main__":
    create_tables()
    create_user()

    asyncio.run(test())

