from pydantic import BaseModel, Field, StrictStr, StrictBool
from uuid import UUID
import datetime


class TokenInfo(BaseModel):
    id: UUID
    token_type: StrictStr
    valid: StrictBool
    created_at: datetime.datetime
    expires_at: datetime.datetime
    user_id: UUID