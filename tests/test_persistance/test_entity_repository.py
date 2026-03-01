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

async def test_get_user_by_id(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    user_dto1 = SignupRequest(
        email="asda@gmail.com",
        username="bro",
        password="asagkASD124.a!"
    )
    user = await repo.create_user(user=user_dto1)
    user = await repo.get_user_by_id(user_id=str(user.id))
    assert user is not None


async def test_get_user_by_email_doesnt_exist(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    res = await repo.get_user_by_email("asd")
    assert res is None

async def test_get_user_by_id_doesnt_exist(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())
    user = await repo.get_user_by_id(user_id="asd")
    assert user is None

async def test_update_user(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())
    user_dto = SignupRequest(
        email="asda@gmail.com",
        username="bro",
        password="asagkASD124.a!"
    )
    user = await repo.create_user(user_dto)
    res = await repo.update_user(str(user.id), "asfg@gmail.com", "babka")
    assert res == True

    user = await repo.get_user_by_id(str(user.id))
    assert user is not None
    assert user.username == "babka"
    assert await repo.get_user_by_email("asfg@gmail.com") is not None


async def test_update_not_exist(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())
    res = await repo.update_user("adsa", "asfg@gmail.com", "babka")
    assert res == False


async def test_verification(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())
    user_dto = SignupRequest(
        email="asda@gmail.com",
        username="bro",
        password="asagkASD124.a!"
    )
    user = await repo.create_user(user_dto)

    assert user.is_verified == False
    res = await repo.verify_user(user_id=str(user.id))
    assert res == True
    assert (await repo.is_user_verified(user_id=str(user.id))) == True


async def test_verification_doesnt_exist(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())
    res = await repo.verify_user(user_id="asfas")
    assert res == False

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "email,username,password,should_succeed",
    [
        # Wrong password
        ("asda@gmail.com", None, "wrong", False),
        (None, "bro", "wrong", False),

        # Correct password
        ("asda@gmail.com", None, "asagkASD124.a!", True),
        (None, "bro", "asagkASD124.a!", True),

        # Both provided
        ("asda@gmail.com", "bro", "asagkASD124.a!", True),
        ("asda@gmail.com", "bro", "wrong", False),

        # Non-existent
        ("notfound@gmail.com", None, "whatever", False),
        (None, None, "whatever", False),
    ],
)
async def test_authenticate_user(
    async_session_factory_fixture,
    email,
    username,
    password,
    should_succeed,
):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    user = await repo.create_user(
        SignupRequest(
            email="asda@gmail.com",
            username="bro",
            password="asagkASD124.a!"
        )
    )

    result = await repo.authenticate(
        email=email,
        username=username,
        password=password,
    )

    assert (result is not None) == should_succeed


@pytest.mark.asyncio
async def test_user_doesnt_exist_is_verified(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    res = await repo.is_user_verified("adsasd")
    assert res == False


@pytest.mark.asyncio
async def test_is_user_admin(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    res = await repo.is_user_admin("asd")
    assert res == False

    user = await repo.create_user(
        SignupRequest(
            email="asda@gmail.com",
            username="bro",
            password="asagkASD124.a!"
        )
    )
    res = await repo.is_user_admin(str(user.id))
    assert res == False

@pytest.mark.asyncio
async def test_is_user_email_taken(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    user = await repo.create_user(
        SignupRequest(
            email="asda@gmail.com",
            username="bro",
            password="asagkASD124.a!"
        )
    )
    res = await repo.is_email_taken("asda@gmail.com")
    assert res == True
    res = await repo.is_email_taken("asadda@gmail.com")
    assert res == False


@pytest.mark.asyncio
async def test_is_username_taken(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    user = await repo.create_user(
        SignupRequest(
            email="asda@gmail.com",
            username="bro",
            password="asagkASD124.a!"
        )
    )
    res = await repo.is_username_taken("bro")
    assert res == True
    res = await repo.is_username_taken("asmad")
    assert res == False


@pytest.mark.asyncio
async def test_unverify_user(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    res = await repo.unverify_user("asd")
    assert res == False

    user = await repo.create_user(
        SignupRequest(
            email="asda@gmail.com",
            username="bro",
            password="asagkASD124.a!"
        )
    )

    res = await repo.unverify_user(str(user.id))
    assert res == True

    await repo.verify_user(user_id=str(user.id))
    res = await repo.is_user_verified(user_id=str(user.id))
    assert res == True

    await repo.unverify_user(user_id=str(user.id))
    res = await repo.is_user_verified(user_id=str(user.id))
    assert res == False


async def test_change_password(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    res = await repo.change_password("asd", "brodas")
    assert res == False

    user = await repo.create_user(
        SignupRequest(
            email="asda@gmail.com",
            username="bro",
            password="asagkASD124.a!"
        )
    )

    res = await repo.change_password(user_id=str(user.id), new_password="asdasd")
    assert res == True

    res = await repo.authenticate(
        username=None,
        email="asda@gmail.com",
        password="asdasd"
    )
    assert res is not None


async def test_create_token(async_session_factory_fixture):
    repo = EntityRepository(async_session_factory_fixture)
    assert 0 == len(await repo._get_all_users())

    user = await repo.create_user(
        SignupRequest(
            email="asda@gmail.com",
            username="bro",
            password="asagkASD124.a!"
        )
    )
