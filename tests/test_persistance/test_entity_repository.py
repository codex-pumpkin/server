import pytest
import dotenv
dotenv.load_dotenv()

from src.persistence.impl.database import EntityRepository
from src.persistence.impl.database.database import Base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import select, update

from src.core.dtos import (
    SignupRequest,
    ConversationRequest,
    TargetLanguage,
    Message,
    QuotaConfig
)

from src.core.exceptions import UserConflictError
import uuid
import datetime
from src.persistence.impl.database.models import (
    TokensOrm,
    LlmModelsOrm,
    ConversationsOrm,
    QuotaOrm,
    MessagesOrm,
    UsersOrm
)

import asyncio

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


async def create_base_user(repo) -> str:
    """Helper to create a user since tokens require a valid user_id."""
    user = await repo.create_user(
        SignupRequest(email=f"{uuid.uuid4()}@test.com", username=str(uuid.uuid4()), password="Password1!")
    )
    return str(user.id)


@pytest.mark.asyncio
@pytest.mark.parametrize("token_type", ["refresh", "email", "password"])
async def test_create_and_get_token_success(async_session_factory_fixture, token_type):
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    user_id = await create_base_user(repo)

    # Test Creation
    created_token = await repo.create_token(user_id=user_id, token_type=token_type)
    assert created_token is not None
    assert created_token.token_type == token_type
    assert str(created_token.user_id) == user_id
    assert created_token.valid is True

    # Test Retrieval
    fetched_token = await repo.get_token(str(created_token.id))
    assert fetched_token is not None
    assert str(fetched_token.id) == str(created_token.id)
    assert fetched_token.token_type == token_type


@pytest.mark.asyncio
async def test_get_token_not_found(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    fake_id = str(uuid.uuid4())
    token = await repo.get_token(fake_id)
    assert token is None


@pytest.mark.asyncio
@pytest.mark.parametrize("token_type", ["refresh", "password"])
async def test_change_token(async_session_factory_fixture, token_type):
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    user_id = await create_base_user(repo)
    old_token = await repo.create_token(user_id=user_id, token_type=token_type)

    new_token = await repo.change_token(str(old_token.id))

    # Assert new token is valid and different
    assert new_token is not None
    assert str(new_token.id) != str(old_token.id)
    assert new_token.token_type == old_token.token_type
    assert str(new_token.user_id) == user_id
    assert new_token.valid is True

    # Assert old token is now invalid in the DB
    updated_old_token = await repo.get_token(str(old_token.id))
    assert updated_old_token.valid is False


@pytest.mark.asyncio
async def test_change_token_not_found(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    fake_id = str(uuid.uuid4())
    new_token = await repo.change_token(fake_id)
    assert new_token is None


@pytest.mark.asyncio
async def test_invalidate_single_token(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    user_id = await create_base_user(repo)
    token = await repo.create_token(user_id=user_id, token_type="email")

    assert await repo.is_token_valid(str(token.id)) is True

    result = await repo.invalidate_token(str(token.id))
    assert result is True
    assert await repo.is_token_valid(str(token.id)) is False


@pytest.mark.asyncio
async def test_invalidate_token_not_found(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    assert await repo.invalidate_token(str(uuid.uuid4())) is False


@pytest.mark.asyncio
async def test_invalidate_all_refresh_tokens(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    user_id_1 = await create_base_user(repo)
    user_id_2 = await create_base_user(repo)

    # User 1 tokens
    u1_refresh_1 = await repo.create_token(user_id=user_id_1, token_type="refresh")
    u1_refresh_2 = await repo.create_token(user_id=user_id_1, token_type="refresh")
    u1_email_1 = await repo.create_token(user_id=user_id_1, token_type="email")

    # User 2 token (Control group)
    u2_refresh_1 = await repo.create_token(user_id=user_id_2, token_type="refresh")

    # Execute bulk invalidation for User 1
    await repo.invalidate_all_refresh_tokens(user_id_1)

    # Assert User 1's refresh tokens are invalid
    assert await repo.is_token_valid(str(u1_refresh_1.id)) == False
    assert await repo.is_token_valid(str(u1_refresh_2.id)) == False

    # Assert User 1's email token is STILL VALID
    assert await repo.is_token_valid(str(u1_email_1.id)) == True

    # Assert User 2's refresh token is STILL VALID
    assert await repo.is_token_valid(str(u2_refresh_1.id)) == True


@pytest.mark.asyncio
async def test_is_token_valid_not_found(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    assert await repo.is_token_valid(str(uuid.uuid4())) is False


@pytest.mark.asyncio
async def test_is_token_valid_manually_invalidated(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    user_id = await create_base_user(repo)
    token = await repo.create_token(user_id=user_id, token_type="password")

    await repo.invalidate_token(str(token.id))
    assert await repo.is_token_valid(str(token.id)) is False


@pytest.mark.asyncio
async def test_is_token_valid_time_expired(async_session_factory_fixture):
    """A token whose valid flag is True, but expires_at is in the past, should return False."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    user_id = await create_base_user(repo)
    token = await repo.create_token(user_id=user_id, token_type="email")

    assert await repo.is_token_valid(str(token.id)) is True

    past_date = (datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=1)).replace(tzinfo=None)

    async with async_session_factory_fixture() as session:
        await session.execute(
            update(TokensOrm)
            .where(TokensOrm.id == str(token.id))
            .values(expires_at=past_date)
        )
        await session.commit()

    token = await repo.get_token(str(token.id))
    assert token.expires_at < datetime.datetime.now(datetime.UTC).replace(tzinfo=None)

    assert await repo.is_token_valid(str(token.id)) is False


async def setup_dependencies(async_session_factory_fixture):
    """Creates a user and an LLM model config to satisfy foreign keys."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    # Create User
    user = await repo.create_user(SignupRequest(
        email=f"user_{uuid.uuid4()}@test.com",
        username=f"user_{uuid.uuid4()}",
        password="Password123!"
    ))

    # Create LLM Model (Directly via session since we aren't testing this part yet)
    llm_id = str(uuid.uuid4())
    async with async_session_factory_fixture() as session:
        llm = LlmModelsOrm(
            id=llm_id,
            name="GPT-4",
            model_name="gpt-4",
            url="https://api.openai.com",
            api_key="sk-test"
        )
        session.add(llm)
        await session.commit()

    return str(user.id), llm_id


@pytest.mark.asyncio
async def test_create_chat_and_verify_persistence(async_session_factory_fixture):
    """Test creating a chat and verifying it exists in the DB with correct data."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    user_id, llm_id = await setup_dependencies(async_session_factory_fixture)

    chat_name = "Netlist Analysis"
    request = ConversationRequest(
        message="Analyze this circuit",
        llm_model_config_id=llm_id,
        target_language=TargetLanguage("spice_netlist"),
        name=chat_name
    )

    # Action
    chat_id = await repo.create_chat(user_id=user_id, request=request)
    assert chat_id is not None

    # Verification: Fetch fresh from DB using a new session
    async with async_session_factory_fixture() as session:
        stmt = select(ConversationsOrm).where(ConversationsOrm.id == chat_id)
        result = await session.execute(stmt)
        db_chat = result.scalar_one()

        assert db_chat.name == chat_name
        assert db_chat.target_language == "spice_netlist"
        assert str(db_chat.user_id) == user_id


@pytest.mark.asyncio
async def test_update_chat_and_verify_change(async_session_factory_fixture):
    """Test updating a chat and verifying the name and pinned status actually changed."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    user_id, llm_id = await setup_dependencies(async_session_factory_fixture)

    chat_id = await repo.create_chat(user_id, ConversationRequest(
        message="init", llm_model_config_id=llm_id,
        target_language=TargetLanguage("spice_netlist"), name="Old Name"
    ))

    # Action: Update
    new_name = "Refined Netlist"
    update_success = await repo.update_chat(chat_id, name=new_name, is_pinned=True)
    assert update_success is True

    # Verification: Check DB state
    updated_chat = await repo.get_chat_by_id(chat_id)
    assert updated_chat.name == new_name
    assert updated_chat.pinned is True


@pytest.mark.asyncio
async def test_delete_chat_and_verify_removal(async_session_factory_fixture):
    """Test deleting a chat and verifying it is no longer reachable."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    user_id, llm_id = await setup_dependencies(async_session_factory_fixture)

    chat_id = await repo.create_chat(user_id, ConversationRequest(
        message="...", llm_model_config_id=llm_id,
        target_language=TargetLanguage("spice_netlist"), name="Temporary"
    ))

    # Verify it exists first
    assert await repo.get_chat_by_id(chat_id) is not None

    # Action: Delete
    delete_success = await repo.delete_chat(chat_id)
    assert delete_success is True

    # Verification: Check it's gone
    assert await repo.get_chat_by_id(chat_id) is None

    # Deep Verification: Raw SQL check
    async with async_session_factory_fixture() as session:
        res = await session.execute(select(ConversationsOrm).where(ConversationsOrm.id == chat_id))
        assert res.scalar() is None


@pytest.mark.asyncio
async def test_get_chats_list_filtering(async_session_factory_fixture):
    """Test that get_chats only returns conversations for the specific user."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    u1, llm_id = await setup_dependencies(async_session_factory_fixture)
    u2, _ = await setup_dependencies(async_session_factory_fixture)

    # Create 2 chats for User 1, 1 chat for User 2
    for i in range(2):
        await repo.create_chat(u1, ConversationRequest(
            message="p", llm_model_config_id=llm_id,
            target_language=TargetLanguage("spice_netlist"), name=f"U1 Chat {i}"
        ))
    await repo.create_chat(u2, ConversationRequest(
        message="p", llm_model_config_id=llm_id,
        target_language=TargetLanguage("spice_netlist"), name="U2 Chat"
    ))

    # Verification for User 1
    u1_chats = await repo.get_chats(u1)
    assert len(u1_chats) == 2
    for c in u1_chats:
        assert str(c.user_id) == u1
        assert "U1 Chat" in c.name

    # Verification for User 2
    u2_chats = await repo.get_chats(u2)
    assert len(u2_chats) == 1
    assert u2_chats[0].name == "U2 Chat"


@pytest.mark.asyncio
async def test_get_chat_by_id_with_messages(async_session_factory_fixture):
    """Verify that get_chat_by_id correctly populates the message list (dto check)."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    user_id, llm_id = await setup_dependencies(async_session_factory_fixture)

    chat_id = await repo.create_chat(user_id, ConversationRequest(
        message="Start", llm_model_config_id=llm_id,
        target_language=TargetLanguage("spice_netlist"), name="Message Test"
    ))

    # Action: Get via Repo
    chat_dto = await repo.get_chat_by_id(chat_id)

    # Verification
    assert chat_dto.id == uuid.UUID(chat_id)
    assert isinstance(chat_dto.messages, list)
    # Even with no messages added yet, the DTO should have an empty list, not None
    assert len(chat_dto.messages) == 0


@pytest.mark.asyncio
async def test_update_chat_returns_false_when_not_found(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    fake_chat_id = str(uuid.uuid4())

    result = await repo.update_chat(
        chat_id=fake_chat_id,
        name="Should Not Work",
        is_pinned=True
    )

    assert result is False


@pytest.mark.asyncio
async def test_delete_chat_returns_false_when_not_found(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    fake_chat_id = str(uuid.uuid4())
    result = await repo.delete_chat(chat_id=fake_chat_id)
    assert result is False


async def setup_chat(async_session_factory_fixture):
    """Setup User, LLM, and one Chat."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    user = await repo.create_user(SignupRequest(
        email=f"u_{uuid.uuid4()}@test.com",
        username=f"u_{uuid.uuid4()}",
        password="Password123!"
    ))

    llm_id = str(uuid.uuid4())
    async with async_session_factory_fixture() as session:
        llm = LlmModelsOrm(
            id=llm_id, name="Spice-GPT", model_name="v1",
            url="http://test", api_key="key"
        )
        session.add(llm)
        await session.commit()

    chat_id = await repo.create_chat(str(user.id), ConversationRequest(
        message="init", llm_model_config_id=llm_id,
        target_language=TargetLanguage("spice_netlist"), name="Message Test Chat"
    ))
    return chat_id


@pytest.mark.asyncio
async def test_add_message_and_verify_persistence(async_session_factory_fixture):
    """Verify message is saved and conversation update time changes."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    chat_id = await setup_chat(async_session_factory_fixture)

    # Get initial update time
    initial_chat = await repo.get_chat_by_id(chat_id)
    initial_updated_at = initial_chat.updated_at

    # Ensure a small delay so timestamps differ (SQLite resolution)
    await asyncio.sleep(0.1)

    msg_data = Message(
        conversation_id=chat_id,
        message="* spice netlist example",
        generation_millis=150,
        response="Success",
        graph="{}"
    )

    # Action
    result = await repo.add_message(chat_id, msg_data)
    assert result is True

    # Verification 1: Message content
    messages = await repo.get_messages(chat_id)
    assert len(messages) == 1
    assert messages[0].message == "* spice netlist example"
    assert messages[0].generation_millis == 150

    # Verification 2: Chat updated_at timestamp changed
    updated_chat = await repo.get_chat_by_id(chat_id)
    assert updated_chat.updated_at > initial_updated_at


@pytest.mark.asyncio
async def test_get_messages_order(async_session_factory_fixture):
    """Verify messages are retrieved in the order they were added."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    chat_id = await setup_chat(async_session_factory_fixture)

    for i in range(3):
        msg = Message(
            conversation_id=chat_id,
            message=f"Prompt {i}",
            generation_millis=10,
            response=f"Resp {i}",
            graph="{}"
        )
        await repo.add_message(chat_id, msg)
        await asyncio.sleep(0.01)  # Ensure unique timestamps

    # Action
    messages = await repo.get_messages(chat_id)

    # Verification
    assert len(messages) == 3
    assert messages[0].message == "Prompt 0"
    assert messages[1].message == "Prompt 1"
    assert messages[2].message == "Prompt 2"


@pytest.mark.asyncio
async def test_delete_last_message_logic(async_session_factory_fixture):
    """Verify the last message is unlinked from the conversation."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    chat_id = await setup_chat(async_session_factory_fixture)

    # Add two messages
    for i in ["First", "Last"]:
        await repo.add_message(chat_id, Message(
            conversation_id=chat_id, message=i,
            generation_millis=5, response="ok", graph="{}"
        ))

    # Action: Delete last
    success = await repo.delete_last_message(chat_id)
    assert success is True

    # Verification: Only "First" remains in the chat list
    remaining_messages = await repo.get_messages(chat_id)
    assert len(remaining_messages) == 1
    assert remaining_messages[0].message == "First"


@pytest.mark.asyncio
async def test_delete_last_message_on_empty_chat_fails(async_session_factory_fixture):
    """Verifies that calling delete on an empty chat raises an IndexError."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    chat_id = await setup_chat(async_session_factory_fixture)

    # Action & Verification: messages[-1] on empty list raises IndexError
    with pytest.raises(IndexError):
        await repo.delete_last_message(chat_id)


@pytest.mark.asyncio
async def test_get_messages_non_existent_chat(async_session_factory_fixture):
    """Verify that get_messages returns an empty list for a fake chat id."""
    repo = EntityRepository(async_factory=async_session_factory_fixture)
    fake_id = str(uuid.uuid4())

    messages = await repo.get_messages(fake_id)
    assert messages == []


@pytest.mark.asyncio
async def test_add_model_persists(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    model_id = await repo.add_model(
        name="TestModel",
        model_name="gpt-4",
        url="http://localhost",
        key="secret"
    )

    assert model_id is not None

    # verify persisted
    model = await repo.get_model(model_id)
    assert model is not None
    assert model.name == "TestModel"
    assert model.model_name == "gpt-4"
    assert model.api_url == "http://localhost"
    assert model.api_key_set is True




@pytest.mark.asyncio
async def test_remove_model_deletes(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    model_id = await repo.add_model(
        name="ToDelete",
        model_name="gpt-3.5",
        url="http://localhost",
        key="secret"
    )

    await repo.remove_model(model_id)

    model = await repo.get_model(model_id)
    assert model is None



@pytest.mark.asyncio
async def test_change_model_updates_all_fields(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    model_id = await repo.add_model(
        name="Old",
        model_name="gpt-3",
        url="http://old",
        key="secret"
    )

    await repo.change_model(
        model_id=model_id,
        name="NewName",
        model_name="gpt-4",
        url="http://new",
        key="new-secret"
    )

    model = await repo.get_model(model_id)

    assert model.name == "NewName"
    assert model.model_name == "gpt-4"
    assert model.api_url == "http://new"
    assert model.api_key_set is True

    key = await repo.get_key_of_model(model_id)
    assert key == "new-secret"


@pytest.mark.asyncio
async def test_change_model_without_key_keeps_existing(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    model_id = await repo.add_model(
        name="Initial",
        model_name="gpt-3",
        url="http://url",
        key="original-key"
    )

    await repo.change_model(
        model_id=model_id,
        name="Updated",
        model_name="gpt-4",
        url="http://new",
        key=None
    )

    key = await repo.get_key_of_model(model_id)

    assert key == "original-key"



@pytest.mark.asyncio
async def test_get_model_non_existent(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    fake_id = str(uuid.uuid4())

    model = await repo.get_model(fake_id)

    assert model is None


@pytest.mark.asyncio
async def test_get_key_of_model_non_existent(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    fake_id = str(uuid.uuid4())

    key = await repo.get_key_of_model(fake_id)

    assert key is None


@pytest.mark.asyncio
async def test_get_llm_configs_empty(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    configs = await repo.get_llm_configs()

    assert configs == []


@pytest.mark.asyncio
async def test_get_llm_configs_returns_all(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    await repo.add_model("A", "gpt-3", "http://a", "k1")
    await repo.add_model("B", "gpt-4", "http://b", "k2")

    configs = await repo.get_llm_configs()

    assert len(configs) == 2
    names = {c.name for c in configs}
    assert names == {"A", "B"}


@pytest.mark.asyncio
async def test_get_llm_by_chat_id_non_existent(async_session_factory_fixture):
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    fake_chat_id = str(uuid.uuid4())

    result = await repo.get_llm_by_chat_id(fake_chat_id)

    assert result is None

# =====================================================
# Helpers
# =====================================================

async def ensure_quota(async_session_factory_fixture):
    async with async_session_factory_fixture() as session:
        existing = await session.execute(select(QuotaOrm))
        if existing.scalars().first() is None:
            quota = QuotaOrm(
                admin_limit=100,
                member_limit=20
            )
            session.add(quota)
            await session.commit()


async def create_user(async_session_factory_fixture, is_admin=False):
    user_id = str(uuid.uuid4())

    async with async_session_factory_fixture() as session:
        user = UsersOrm(
            id=user_id,
            created_at=datetime.datetime.now(datetime.UTC).replace(tzinfo=None),
            username=f"user_{user_id[:6]}",
            email=f"{user_id[:6]}@test.com",
            hashed_password="hashed",
            is_admin=is_admin,
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
            name="Test Conversation",
            is_pinned=False,
            llm_id=llm_id,
            user_id=user_id,
        )
        session.add(conversation)
        await session.commit()

    return conversation_id


async def create_message(async_session_factory_fixture, conversation_id):
    async with async_session_factory_fixture() as session:
        msg = MessagesOrm(
            id=str(uuid.uuid4()),
            created_at=datetime.datetime.now(datetime.UTC).replace(tzinfo=None),
            prompt="hi",
            response="hello",
            graph="{}",
            generation_ms=10,
            conversation_id=conversation_id
        )
        session.add(msg)
        await session.commit()


@pytest.mark.asyncio
async def test_change_quota(async_session_factory_fixture):
    await ensure_quota(async_session_factory_fixture)
    repo = EntityRepository(async_factory=async_session_factory_fixture)

    await repo.change_quota(QuotaConfig(admin=50, member=5))

    quota = await repo.get_quota()

    assert quota.admin == 50
    assert quota.member == 5


@pytest.mark.asyncio
async def test_member_quota_remaining(async_session_factory_fixture):
    await ensure_quota(async_session_factory_fixture)

    repo = EntityRepository(async_factory=async_session_factory_fixture)

    user_id = await create_user(async_session_factory_fixture, is_admin=False)

    remaining = await repo.get_user_quota_remaining(user_id)

    assert remaining == 20  # default member_limit


@pytest.mark.asyncio
async def test_admin_quota_remaining(async_session_factory_fixture):
    await ensure_quota(async_session_factory_fixture)

    repo = EntityRepository(async_factory=async_session_factory_fixture)

    user_id = await create_user(async_session_factory_fixture, is_admin=True)

    remaining = await repo.get_user_quota_remaining(user_id)

    assert remaining == 100  # default admin_limit


@pytest.mark.asyncio
async def test_quota_subtraction(async_session_factory_fixture):
    await ensure_quota(async_session_factory_fixture)

    repo = EntityRepository(async_factory=async_session_factory_fixture)

    user_id = await create_user(async_session_factory_fixture)
    llm_id = await create_llm(async_session_factory_fixture)
    conversation_id = await create_conversation(async_session_factory_fixture, user_id, llm_id)

    for _ in range(5):
        await create_message(async_session_factory_fixture, conversation_id)

    remaining = await repo.get_user_quota_remaining(user_id)

    assert remaining == 15


@pytest.mark.asyncio
async def test_quota_clamped_to_zero(async_session_factory_fixture):
    await ensure_quota(async_session_factory_fixture)

    repo = EntityRepository(async_factory=async_session_factory_fixture)

    user_id = await create_user(async_session_factory_fixture)
    llm_id = await create_llm(async_session_factory_fixture)
    conversation_id = await create_conversation(async_session_factory_fixture, user_id, llm_id)

    for _ in range(25):  # exceed 20
        await create_message(async_session_factory_fixture, conversation_id)

    remaining = await repo.get_user_quota_remaining(user_id)

    assert remaining == 0



async def test_is_quota_exceeded_false(async_session_factory_fixture):
    await ensure_quota(async_session_factory_fixture)

    repo = EntityRepository(async_factory=async_session_factory_fixture)

    user_id = await create_user(async_session_factory_fixture)

    exceeded = await repo.is_quota_exceeded(user_id)

    assert exceeded is False


@pytest.mark.asyncio
async def test_is_quota_exceeded_true(async_session_factory_fixture):
    await ensure_quota(async_session_factory_fixture)

    repo = EntityRepository(async_factory=async_session_factory_fixture)

    user_id = await create_user(async_session_factory_fixture)
    llm_id = await create_llm(async_session_factory_fixture)
    conversation_id = await create_conversation(async_session_factory_fixture, user_id, llm_id)

    for _ in range(20):  # exactly limit
        await create_message(async_session_factory_fixture, conversation_id)

    exceeded = await repo.is_quota_exceeded(user_id)

    assert exceeded is True