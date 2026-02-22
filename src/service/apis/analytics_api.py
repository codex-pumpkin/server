# coding: utf-8

from typing import Dict, List  # noqa: F401

from src.business.interfaces import ISystemManager

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

from src.core.dtos import AnalyticsResponse, AnalyticsRequest, TokenModel
from src.service.security_api import get_token_jwt, get_token_jwt_mandatory_admin

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
    analytics_request: AnalyticsRequest = Depends(),
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory_admin
    ),
    system_manger: ISystemManager = Depends(get_system_manager)
) -> AnalyticsResponse:
    """
    Return aggregated analytics data for administrators.

    @param
        token_jwt (TokenModel): Admin-authenticated token payload from security dependency.
        system_manger (ISystemManager): Business manager used to load analytics.

    @return
        AnalyticsResponse: Aggregated usage analytics for the system.
    """
    return await system_manger.get_analytics(analytics_request)
