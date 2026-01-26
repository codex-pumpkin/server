from src.persistence.factory.PersistenceFactory import PersistenceFactory

from src.business.interfaces import IPromptManager


class PromptManager(IPromptManager):
    async def retrieve_context(self, user_input: str, top_k: int = 3) -> str:
        """Return top-k matching documents as a single newline-separated string."""
        repo = await PersistenceFactory.get_semantic_repository()
        chunks = repo.get_similar_chunks(user_input, top_k)
        return "\n".join(chunks)

    def make_regeneration_context(self, exit_code: int, raw_output: str) -> str:
        context = "Ngspice exited with code: {} .Ngspice output is: {}".format(exit_code, raw_output)
        return context