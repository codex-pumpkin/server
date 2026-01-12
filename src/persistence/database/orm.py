from src.persistence.database.database import Base, sync_engine, session_factory, async_engine
from src.persistence.database.models import UsersOrm
from sqlalchemy.orm import Session
from src.persistence.database.queries import AsyncOrm
import asyncio

def create_tables():
    sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True

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
    print(await AsyncOrm.get_user_by_email("asd"))
    print(await AsyncOrm.get_user_by_email("sad@gmail.com"))
    await async_engine.dispose()


if __name__ == "__main__":
    create_tables()
    create_user()

    asyncio.run(test())

