
from typing import Protocol
from typing_extensions import runtime_checkable
from abc import abstractmethod, ABC

class IAIClient(ABC):
    @abstractmethod
    async def get_response(
        self,
        user_question: str,
        retrieved_context: str,
        conversation_history: str,
        api_key: str,
        model: str,
        api_url: str
    ) -> str:
        """Get response."""
        ...

    @abstractmethod
    async def regenerate(
        self,
        user_question: str,
        regeneration_context: str,
        code: str,
        api_key: str,
        model: str,
        api_url:str
    ) -> str:
        """Regenerate."""
        ...    
