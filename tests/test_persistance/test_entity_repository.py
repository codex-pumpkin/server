import pytest
import dotenv
dotenv.load_dotenv()

from src.persistence.impl.database import EntityRepository
from src.persistence.impl.database.database import Base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.core.dtos import SignupRequest
from src.core.exceptions import UserConflictError

@pytest.fixture(scope="module")
async def async_engine_fixture():
    """Module-scoped engine for all tests."""
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        connect_args={"check_same_thread": False},
        echo=False
    )
    yield engine
    await engine.dispose()


@pytest.fixture(scope="module")
async def async_session_factory_fixture(async_engine_fixture):
    """Provide session factory bound to the engine."""
    session_factory = async_sessionmaker(
        bind=async_engine_fixture,
        autoflush=False,
        expire_on_commit=False
    )
    yield session_factory


@pytest.fixture(autouse=True)
async def reset_tables(async_engine_fixture):
    """Drop and recreate all tables before each test."""
    async with async_engine_fixture.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

@pytest.mark.asyncio
async def test_create_user_single(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    assert 0 == len(await repo._get_all_users())

    user_dto = SignupRequest(
        email="asda@gmail.com",
        username="bro",
        password="asagkASD124.a!"
    )
    await repo.create_user(user=user_dto)

    user = await repo.get_user_by_email("asda@gmail.com")
    assert user is not None

@pytest.mark.asyncio
async def test_create_user_same_email_or_username_verified(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    assert 0 == len(await repo._get_all_users())

    user_dto1 = SignupRequest(
        email="asda@gmail.com",
        username="bro",
        password="asagkASD124.a!"
    )
    user = await repo.create_user(user=user_dto1)
    await repo.verify_user(str(user.id))

    user_dto2 = SignupRequest(
        email="asda@gmail.com",
        username="bro2",
        password="asagkASD124.a!"
    )
    with pytest.raises(UserConflictError):
        await repo.create_user(user=user_dto2)


    user_dto3 = SignupRequest(
        email="asda1@gmail.com",
        username="bro",
        password="asagkASD124.a!"
    )
    with pytest.raises(UserConflictError):
        await repo.create_user(user=user_dto3)

@pytest.mark.asyncio
async def test_create_user_same_email_or_username_unverified(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    user_dto1 = SignupRequest(
        email="asda@gmail.com",
        username="bro",
        password="asagkASD124.a!"
    )
    await repo.create_user(user=user_dto1)

    user_dto2 = SignupRequest(
        email="asda@gmail.com",
        username="bro2",
        password="asagkASD124.a!"
    )
    await repo.create_user(user=user_dto2)


    user_dto3 = SignupRequest(
        email="asda1@gmail.com",
        username="bro",
        password="asagkASD124.a!"
    )
    await repo.create_user(user=user_dto3)