# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from src.business.interfaces import ISystemManager

from src.service.openapi_server.dependencies import get_system_manager

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
from typing import Any
from src.core.dtos.analytics_response import AnalyticsResponse
from src.service.openapi_server.security_api import get_token_jwt

router = APIRouter()



@router.get(
    "/analytics",
    responses={
        200: {"model": AnalyticsResponse, "description": "Analytics retrieved successfully"},
        401: {"description": "User not authenticator authorized"},
    },
    tags=["Analytics"],
    summary="Get current analytics",
    response_model_by_alias=True,
)
async def analytics_get(
    token_jwt: TokenModel = Security(
        get_token_jwt
    ),
) -> AnalyticsResponse:
    """Returns the analytics. Only for Admins."""
    system_manger : ISystemManager = Depends(get_system_manager())
    return await system_manger.get_analytics(token_jwt)
