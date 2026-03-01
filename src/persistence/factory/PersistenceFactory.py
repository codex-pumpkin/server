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

T = TypeVar("T")


class PersistenceFactory:
    _singletons: Dict[Type, object] = {}
    _lock = asyncio.Lock()

    @classmethod
    async def _get_singleton(cls, interface: Type[T], implementation: Type[T]) -> T:
        """Get singleton."""
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
        """Get ai client."""
        from src.persistence.impl.llm import AIClient
        return await cls._get_singleton(IAIClient, AIClient)

    @classmethod
    async def get_code_validator(cls) -> ICodeValidator:
        """Get code validator."""
        from src.persistence.impl.validator import CodeValidator
        return await cls._get_singleton(ICodeValidator, CodeValidator)

    @classmethod
    async def get_entity_repository(cls) -> IEntityRepository:
        """Get entity repository."""
        from src.persistence.impl.database import EntityRepository
        return await cls._get_singleton(IEntityRepository, EntityRepository)

    @classmethod
    async def get_graph_generator(cls) -> IGraphGenerator:
        """Get graph generator."""
        from src.persistence.impl.generator import GraphGenerator
        return await cls._get_singleton(IGraphGenerator, GraphGenerator)

    @classmethod
    async def get_mail_sender(cls) -> IMailSender:
        """Get mail sender."""
        from src.persistence.impl.mail import MailSender
        return await cls._get_singleton(IMailSender, MailSender)

    @classmethod
    async def get_semantic_repository(cls, connect: bool = True) -> ISemanticRepository:
        """Get semantic repository."""
        from src.persistence.impl.chroma_database import SemanticRepository

        if ISemanticRepository not in cls._singletons:
            async with cls._lock:
                if ISemanticRepository not in cls._singletons:
                    # Pass 'connect' to constructor
                    cls._singletons[ISemanticRepository] = SemanticRepository(connect=connect)

        return cls._singletons[ISemanticRepository]
