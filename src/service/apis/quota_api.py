# coding: utf-8

from typing import Dict, List  # noqa: F401

#TODO: implement business logic interface
from src.business.interfaces.ISystemManager import ISystemManger

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
from src.service.security_api import get_token_JWT

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
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> QuotaConfig:
    """Returns the current quota configuration."""
    system_manger : ISystemManger = Depends(get_system_manager())
    return await system_manger.getQuotaSettings(token_JWT)


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
    system_manger: ISystemManger = Depends(get_system_manager())
    return await system_manger.applyQuotaAdjustment(token_JWT,quota_config)
