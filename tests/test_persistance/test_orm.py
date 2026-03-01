import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.persistence.impl.database.database import Base
from src.persistence.impl.database.orm import tables_exist, create_quota, create_tables, create_user
from src.persistence.impl.database.models import QuotaOrm, UsersOrm

@pytest.fixture(scope="function")
def test_engine():
    """Create a temporary SQLite in-memory engine."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.drop_all(engine)
    return engine

@pytest.fixture(scope="function")
def test_sessionmaker(test_engine):
    """Create a sessionmaker bound to the temporary engine."""
    return sessionmaker(bind=test_engine)


def test_tables_exist(test_engine, test_sessionmaker):
    # Tables don't exist yet
    assert not tables_exist(test_engine)

    # Create tables
    create_tables(test_engine, test_sessionmaker)
    assert tables_exist(test_engine)


def test_create_quota(test_engine, test_sessionmaker):
    create_tables(test_engine, test_sessionmaker)
    session = test_sessionmaker()
    create_quota(session)
    quota = session.query(QuotaOrm).first()
    assert quota is not None
    assert quota.admin_limit == 100
    assert quota.member_limit == 20
    session.close()


def test_create_tables_with_session(test_engine, test_sessionmaker):
    # Drop tables for fresh start
    Base.metadata.drop_all(test_engine)

    create_tables(test_engine, test_sessionmaker)
    session = test_sessionmaker()
    quota = session.query(QuotaOrm).first()
    user = session.query(UsersOrm).first()
    assert quota is not None
    assert user is not None
    session.close()