

from src.core.dtos.account_response import AccountResponse
from pydantic import StrictStr, Field

class AccountInfo(AccountResponse):
    verification_code:StrictStr = Field(description="Verification code")