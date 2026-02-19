from abc import ABC, abstractmethod
from typing import List, Tuple

class IPromptManager(ABC):

    @abstractmethod
    async def retrieve_context(self, user_input: str, top_k: int) -> str:
        """Retrieve context."""
        pass
    
    @abstractmethod
    def make_regeneration_context(self, exit_code: int, raw_output: str) -> str:
        """Make regeneration context."""
        pass

    @abstractmethod
    def get_conversation_context(self, conversation_history: List[Tuple[str, str]]) -> str:
        """Get conversation context."""
        pass
