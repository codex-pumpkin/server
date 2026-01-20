from src.persistence.factory.PersistenceFactory import PersistenceFactory

from src.business.interfaces import IPromptManager


class PromptManager(IPromptManager):

    async def __init__(self) -> None:
        self.SemanticRepository = PersistenceFactory.get_semantic_repository()

    async def retrieve_context(self, user_input: str, top_k: int = 3) -> str:
        """Return top-k matching documents as a single newline-separated string."""
        chunks = await self.SemanticRepository.get_similar_chunks(user_input, top_k)
        return "\n".join(chunks)