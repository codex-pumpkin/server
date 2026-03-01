import dotenv
dotenv.load_dotenv()

from src.persistence.factory import PersistenceFactory
from src.persistence.impl import (
    EntityRepository,
    SemanticRepository,
    GraphGenerator,
    AIClient,
    MailSender,
    CodeValidator
)

from src.persistence.interfaces import (
    IEntityRepository,
    IAIClient,
    ICodeValidator,
    IGraphGenerator,
    ISemanticRepository,
    IMailSender
)

import pytest


@pytest.mark.asyncio
async def test_entity_repository():
    repo1 = await PersistenceFactory.get_entity_repository()
    assert isinstance(repo1, EntityRepository)
    assert isinstance(repo1, IEntityRepository)

    repo2 = await PersistenceFactory.get_entity_repository()
    assert repo1 is repo2


@pytest.mark.asyncio
async def test_semantic_repository():
    repo1 = await PersistenceFactory.get_semantic_repository(connect=False)
    assert isinstance(repo1, SemanticRepository)
    assert isinstance(repo1, ISemanticRepository)

    repo2 = await PersistenceFactory.get_semantic_repository(connect=False)
    assert repo1 is repo2


@pytest.mark.asyncio
async def test_graph_generator():
    generator1 = await PersistenceFactory.get_graph_generator()
    assert isinstance(generator1, GraphGenerator)
    assert isinstance(generator1, IGraphGenerator)

    generator2 = await PersistenceFactory.get_graph_generator()
    assert generator1 is generator2


@pytest.mark.asyncio
async def test_ai_client():
    client1 = await PersistenceFactory.get_ai_client()
    assert isinstance(client1, AIClient)
    assert isinstance(client1, IAIClient)

    client2 = await PersistenceFactory.get_ai_client()
    assert client1 is client2


@pytest.mark.asyncio
async def test_mail_sender():
    sender1 = await PersistenceFactory.get_mail_sender()
    assert isinstance(sender1, MailSender)
    assert isinstance(sender1, IMailSender)

    sender2 = await PersistenceFactory.get_mail_sender()
    assert sender1 is sender2


@pytest.mark.asyncio
async def test_code_validator():
    validator1 = await PersistenceFactory.get_code_validator()
    assert isinstance(validator1, CodeValidator)
    assert isinstance(validator1, ICodeValidator)

    validator2 = await PersistenceFactory.get_code_validator()
    assert validator1 is validator2