# coding: utf-8
import datetime
from typing import List

from fastapi import Depends, Security  # noqa: F401
from fastapi.openapi.models import OAuthFlowImplicit, OAuthFlows  # noqa: F401
from fastapi.security import (  # noqa: F401
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
    OAuth2,
    OAuth2AuthorizationCodeBearer,
    OAuth2PasswordBearer,
    SecurityScopes,
)
from fastapi.security.api_key import APIKeyCookie, APIKeyHeader, APIKeyQuery  # noqa: F401
from fastapi import HTTPException, status
from src.core.dtos.extra_models import TokenModel
from src.business.impl.auth import check_if_jwt_valid, decode_jwt
from typing import Optional
from uuid import UUID

def get_token_jwt(
    access_token: Optional[UUID] = Security(
        APIKeyHeader(name="access_token", auto_error=False)
    )
) -> Optional[TokenModel]:
    if not access_token:
        return None

    if not check_if_jwt_valid(str(access_token)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="access_token isnt valid!",
        )

    payload = decode_jwt(str(access_token))
    token_data = TokenModel(**payload)

    if token_data.exp < datetime.datetime.now(datetime.UTC):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="access_token is expired!",
        )

    return token_data

def get_token_jwt_mandatory(
    access_token: UUID = Security(
        APIKeyHeader(name="access_token", auto_error=False)
    )
) -> TokenModel:
    token = get_token_jwt(access_token=access_token)
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="logging in is required"
        )
    return token

def get_token_jwt_mandatory_admin(
    access_token: UUID = Security(
        APIKeyHeader(name="access_token", auto_error=False)
    )
) -> TokenModel:
    token_data = get_token_jwt_mandatory(access_token=access_token)

    if not token_data.is_admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="admin status is requiered!"
        )

    return token_data
