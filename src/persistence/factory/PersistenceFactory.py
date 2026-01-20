import asyncio
from typing import Dict, Type, TypeVar

from src.persistence.interfaces import (
    IAIClient,
    ICodeValidator,
    IEntityRepository,
    IGraphGenerator,
    IMailSender,
    ISemanticRepository,
)

from src.persistence.impl import (
    EntityRepository,
    SemanticRepository,
    MailSender,
    CodeValidator,
    GraphGenerator,
    AIClient
)

T = TypeVar("T")


class PersistenceFactory:
    _singletons: Dict[Type, object] = {}
    _lock = asyncio.Lock()

    @classmethod
    async def _get_singleton(cls, interface: Type[T], implementation: Type[T]) -> T:
        if interface not in cls._singletons:
            async with cls._lock:
                if interface not in cls._singletons:
                    cls._singletons[interface] = implementation()
        return cls._singletons[interface]  # type: ignore

    # ------------------------
    # Interface-based getters
    # ------------------------

    @classmethod
    async def get_ai_client(cls) -> IAIClient:
        return await cls._get_singleton(IAIClient, AIClient)

    @classmethod
    async def get_code_validator(cls) -> ICodeValidator:
        return await cls._get_singleton(ICodeValidator, CodeValidator)

    @classmethod
    async def get_entity_repository(cls) -> IEntityRepository:
        return await cls._get_singleton(IEntityRepository, EntityRepository)

    @classmethod
    async def get_graph_generator(cls) -> IGraphGenerator:
        return await cls._get_singleton(IGraphGenerator, GraphGenerator)

    @classmethod
    async def get_mail_sender(cls) -> IMailSender:
        return await cls._get_singleton(IMailSender, MailSender)

    @classmethod
    async def get_semantic_repository(cls) -> ISemanticRepository:
        return await cls._get_singleton(ISemanticRepository, SemanticRepository)
