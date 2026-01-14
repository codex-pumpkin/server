# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from business.logic_interfaces.ISystemManger import ISystemManger

from service.openapi_server.dependencies import get_system_manager

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
from service.openapi_server.models.analytics_response import AnalyticsResponse
from service.openapi_server.security_api import get_token_JWT

router = APIRouter()



@router.get(
    "/analytics",
    responses={
        200: {"model": AnalyticsResponse, "description": "Analytics retrieved successfully"},
        401: {"description": "User not authenticatedor authorized"},
    },
    tags=["Analytics"],
    summary="Get current analytics",
    response_model_by_alias=True,
)
async def analytics_get(
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> AnalyticsResponse:
    """Returns the analytics. Only for Admins."""
    system_manger : ISystemManger = Depends(get_system_manager())
    return await system_manger.get_analytics(token_JWT)
