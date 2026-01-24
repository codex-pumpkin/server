from abc import ABC, abstractmethod


class IPromptManager(ABC):

    @abstractmethod
    async def retrieve_context(self, user_input: str, top_k: int) -> str:
        pass
    
    @abstractmethod
    def make_regeneration_context(self, exit_code: int, raw_output: str) -> str:
        pass