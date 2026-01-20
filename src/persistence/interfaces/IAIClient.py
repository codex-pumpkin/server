
from typing import Protocol
from typing_extensions import runtime_checkable
from abc import abstractmethod, ABC

class IAIClient(ABC):
    @abstractmethod
    async def get_response(self, user_question: str, retrieved_context: str, api_key: str, model: str) -> str:
        ...