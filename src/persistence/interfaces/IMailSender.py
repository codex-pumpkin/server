

from typing import Protocol
from typing_extensions import runtime_checkable
from abc import ABC, abstractmethod

class IMailSender(ABC):
    @abstractmethod
    async def send_confirmation_email(self, to_email: str, confirmation_code: str) -> None:
        """Send confirmation email."""
        ...

    @abstractmethod
    async def send_password_reset_email(self, to_email: str, reset_link: str) -> None:
        """Send password reset email."""
        ...

    @abstractmethod
    async def send_temporary_password_email(self, to_email: str, password: str) -> None:
        """Send temporary password email."""
        ...
