# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from service.openapi_server.apis.quota_api_base import BaseQuotaApi
#TODO: replace impl with business package
import service.openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from service.openapi_server.models.extra_models import TokenModel  # noqa: F401
from typing import Any
from service.openapi_server.models.quota_config import QuotaConfig
from service.openapi_server.security_api import get_token_JWT

router = APIRouter()

#TODO: replace impl with business package
ns_pkg = service.openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/quota",
    responses={
        200: {"model": QuotaConfig, "description": "Quota configuration retrieved successfully"},
    },
    tags=["Quota"],
    summary="Get current quota configuration",
    response_model_by_alias=True,
)
async def quota_get(
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> QuotaConfig:
    """Returns the current quota configuration."""
    if not BaseQuotaApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseQuotaApi.subclasses[0]().quota_get()


@router.put(
    "/quota",
    responses={
        200: {"model": QuotaConfig, "description": "Quota configuration updated successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated or authorized"},
    },
    tags=["Quota"],
    summary="Update quota configuration",
    response_model_by_alias=True,
)
async def quota_put(
    quota_config: QuotaConfig = Body(None, description=""),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> QuotaConfig:
    """Updates the quota limits for members and admins. Only for admins."""
    if not BaseQuotaApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseQuotaApi.subclasses[0]().quota_put(quota_config)
