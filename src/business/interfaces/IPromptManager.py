from abc import ABC, abstractmethod


class IPromptManager(ABC):

    @abstractmethod
    async def retrieve_context(self, user_input: str, top_k: int) -> str:
        pass