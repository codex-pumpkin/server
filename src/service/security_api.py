# coding: utf-8

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

def get_token_jwt(
    access_token: str = Security(
        APIKeyHeader(name="access_token", auto_error=False)
    )
) -> TokenModel:
    if not check_if_jwt_valid(access_token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="access_token isnt valid!",
        )

    payload = decode_jwt(access_token)
    token_data = TokenModel(**payload)
    return token_data

