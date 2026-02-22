import os
import shutil

from src.core import settings
from src.persistence.impl.database.database import Base, sync_engine, session_factory, async_engine
from src.persistence.impl.database.models import UsersOrm, QuotaOrm
import asyncio
from src.persistence.impl.database.hash_util import hash_password
from sqlalchemy import inspect
import logging


def tables_exist() -> bool:
    """Tables exist."""
    inspector = inspect(sync_engine)
    return inspector.has_table("users")


def create_tables():
    """Create tables."""
    sync_engine.echo = False
    if tables_exist():
        logging.info("Tables already exist. Skipping creation.")
        sync_engine.echo = True
        return

    logging.info("Creating tables...")
    Base.metadata.create_all(sync_engine)
    create_quota()
    create_user()
    sync_engine.echo = True


def create_quota():
    """Create quota."""
    quota = QuotaOrm(
        admin_limit=100,
        member_limit=20
    )
    with session_factory() as session:
        session.add(quota)
        session.commit()

def create_user():
    """Create user."""
    admin = UsersOrm(
        email=settings.admin_settings.email,
        username=settings.admin_settings.username,
        hashed_password=hash_password(settings.admin_settings.password),
        is_verified=True,
        is_admin=True,
    )
    with session_factory() as session:
        session.add(admin)
        session.commit()
        id = admin.id
        shutil.copy(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + "/static/admin_pp.jpeg", f"/app/pictures/{id}.jpg")

async def test():
    """Test."""
    await async_engine.dispose()


if __name__ == "__main__":
    create_tables()
    create_user()

    asyncio.run(test())

