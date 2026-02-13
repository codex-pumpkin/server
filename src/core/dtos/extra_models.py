# coding: utf-8
import datetime

from pydantic import BaseModel, StrictBool
from uuid import UUID


class TokenModel(BaseModel):
    """Defines a token model."""

    sub: UUID
    is_admin: StrictBool
    exp: datetime.datetime
    toc: datetime.datetime
