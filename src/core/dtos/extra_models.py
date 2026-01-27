# coding: utf-8

from pydantic import BaseModel, StrictBool
from uuid import UUID


class TokenModel(BaseModel):
    """Defines a token model."""

    sub: UUID
    is_admin: StrictBool
