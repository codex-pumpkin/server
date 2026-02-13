# coding: utf-8

from typing import Dict, List  # noqa: F401

#TODO: implement business logic interface
from src.business.interfaces.ISystemManager import ISystemManager

from src.service.dependencies import get_system_manager

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

from src.core.dtos.extra_models import TokenModel  # noqa: F401
from src.core.dtos.quota_config import QuotaConfig
from src.service.security_api import get_token_jwt

router = APIRouter()



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
    system_manger : ISystemManager = Depends(get_system_manager),
    token_jwt: TokenModel = Security(get_token_jwt)
) -> QuotaConfig:
    """Returns the current quota configuration."""
    return await system_manger.get_quota_settings()


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
    quota_config: QuotaConfig,
    token_jwt: TokenModel = Security(get_token_jwt),
    system_manger: ISystemManager = Depends(get_system_manager)
) -> None:
    """Updates the quota limits for members and admins. Only for admins."""
    return await system_manger.apply_quota_adjustment(quota_config=quota_config)
