import os
import shutil
import logging
from sqlalchemy import inspect
from src.core import settings
from src.persistence.impl.database.database import Base, sync_engine, session_factory
from src.persistence.impl.database.models import UsersOrm, QuotaOrm
from src.persistence.impl.database.hash_util import hash_password


def tables_exist(engine) -> bool:
    """Check if 'users' table exists in the given engine."""
    inspector = inspect(engine)
    return inspector.has_table("users")


def create_tables(engine=sync_engine, sessionmaker=session_factory):
    engine.echo = False

    if tables_exist(engine):
        logging.info("Tables already exist. Skipping creation.")
        engine.echo = True
        return

    logging.info("Creating tables...")
    Base.metadata.create_all(engine)

    # Use provided sessionmaker
    with sessionmaker() as session:
        create_quota(session)
        create_user(session)

    engine.echo = True


def create_quota(session):
    """Create default quota."""
    quota = QuotaOrm(admin_limit=100, member_limit=20)
    session.add(quota)
    session.commit()


def create_user(session):
    """Create default admin user."""
    admin = UsersOrm(
        email=settings.admin_settings.email,
        username=settings.admin_settings.username,
        hashed_password=hash_password(settings.admin_settings.password),
        is_verified=True,
        is_admin=True,
    )
    session.add(admin)
    session.commit()

    user_id = admin.id
    static_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),
        "static",
        "admin_pp.jpeg"
    )
    dest_path = f"/app/pictures/{user_id}.jpg"
    if os.path.exists(static_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy(static_path, dest_path)