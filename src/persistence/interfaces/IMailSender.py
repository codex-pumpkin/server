

from typing import Protocol
from typing_extensions import runtime_checkable
from abc import ABC, abstractmethod

class IMailSender(ABC):
    @abstractmethod
    async def send_confirmation_email(self, to_email: str, confirmation_code: str) -> None:
        ...

    @abstractmethod
    async def send_password_reset_email(self, to_email: str, reset_link: str) -> None:
        ...

