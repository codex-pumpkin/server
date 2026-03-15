import pytest
import uuid
from datetime import timedelta
import datetime
import dotenv
dotenv.load_dotenv()

from src.persistence.impl.database.models import  (
    UsersOrm, LlmModelsOrm, ConversationsOrm, MessagesOrm
)

from src.persistence.impl.database.EntityRepository import EntityRepository
from src.core.dtos import AnalyticsResponse
from src.persistence.impl.database.database import Base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


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
async def create_user(async_session_factory_fixture):
    user_id = str(uuid.uuid4())

    async with async_session_factory_fixture() as session:
        user = UsersOrm(
            id=user_id,
            created_at=datetime.datetime.now(datetime.UTC).replace(tzinfo=None),
            username=f"user_{user_id[:6]}",
            email=f"{user_id[:6]}@test.com",
            hashed_password="hashed",
            is_admin=False,
            is_verified=True,
            google_id=None
        )
        session.add(user)
        await session.commit()

    return user_id


async def create_llm(async_session_factory_fixture):
    llm_id = str(uuid.uuid4())

    async with async_session_factory_fixture() as session:
        llm = LlmModelsOrm(
            id=llm_id,
            name="TestLLM",
            model_name="gpt-4",
            url="http://localhost",
            api_key="secret"
        )
        session.add(llm)
        await session.commit()

    return llm_id


async def create_conversation(async_session_factory_fixture, user_id, llm_id):
    conversation_id = str(uuid.uuid4())

    async with async_session_factory_fixture() as session:
        conversation = ConversationsOrm(
            id=conversation_id,
            created_at=datetime.datetime.now(datetime.UTC).replace(tzinfo=None),
            updated_at=datetime.datetime.now(datetime.UTC).replace(tzinfo=None),
            name="Analytics Test",
            is_pinned=False,
            llm_id=llm_id,
            user_id=user_id
        )
        session.add(conversation)
        await session.commit()

    return conversation_id


async def create_message_at_time(async_session_factory_fixture, conversation_id, timestamp):
    async with async_session_factory_fixture() as session:
        msg = MessagesOrm(
            id=str(uuid.uuid4()),
            created_at=timestamp,
            prompt="hi",
            response="hello",
            graph="{}",
            simulation_result="{}",
            generation_ms=10,
            conversation_id=conversation_id
        )
        session.add(msg)
        await session.commit()


@pytest.mark.asyncio
async def test_get_usage_data_empty(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    result = await repo.get_usage_data(period=24, interval=15)

    assert isinstance(result, AnalyticsResponse)
    assert isinstance(result.start_time, datetime.datetime)
    assert result.interval_minutes == 15
    assert isinstance(result.usage, list)
    assert all(isinstance(x, int) for x in result.usage)


@pytest.mark.asyncio
async def test_get_usage_data_with_messages(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    user_id = await create_user(async_session_factory_fixture)
    llm_id = await create_llm(async_session_factory_fixture)
    conversation_id = await create_conversation(
        async_session_factory_fixture,
        user_id,
        llm_id
    )

    now = datetime.datetime.now(datetime.UTC).replace(tzinfo=None)

    # Create messages in different intervals
    await create_message_at_time(async_session_factory_fixture, conversation_id, now - timedelta(minutes=5))
    await create_message_at_time(async_session_factory_fixture, conversation_id, now - timedelta(minutes=10))
    await create_message_at_time(async_session_factory_fixture, conversation_id, now - timedelta(minutes=40))

    result = await repo.get_usage_data(period=1, interval=15)

    assert isinstance(result, AnalyticsResponse)
    assert result.interval_minutes == 15
    assert sum(result.usage) >= 3  # At least 3 messages counted


@pytest.mark.asyncio
async def test_get_usage_data_different_interval(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    user_id = await create_user(async_session_factory_fixture)
    llm_id = await create_llm(async_session_factory_fixture)
    conversation_id = await create_conversation(
        async_session_factory_fixture,
        user_id,
        llm_id
    )

    now = datetime.datetime.now(datetime.UTC).replace(tzinfo=None)

    await create_message_at_time(async_session_factory_fixture, conversation_id, now - timedelta(minutes=5))
    await create_message_at_time(async_session_factory_fixture, conversation_id, now - timedelta(minutes=30))

    result = await repo.get_usage_data(period=1, interval=30)

    assert result.interval_minutes == 30
    assert sum(result.usage) >= 2


@pytest.mark.asyncio
async def test_get_usage_data_period_filter(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    user_id = await create_user(async_session_factory_fixture)
    llm_id = await create_llm(async_session_factory_fixture)
    conversation_id = await create_conversation(
        async_session_factory_fixture,
        user_id,
        llm_id
    )

    now = datetime.datetime.now(datetime.UTC).replace(tzinfo=None)

    # Inside period
    await create_message_at_time(async_session_factory_fixture, conversation_id, now - timedelta(minutes=10))

    # Outside period
    await create_message_at_time(async_session_factory_fixture, conversation_id, now - timedelta(hours=33))

    result = await repo.get_usage_data(period=1, interval=15)

    assert sum(result.usage) == 1