# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from business.api_interfaces.IUserInfoMange import IUserInfoMange
from business.api_interfaces.ISystemManger import ISystemManger

from service.openapi_server.dependencies import get_user_info_manager, get_system_manager

import business
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
    UploadFile,
    File
)

from service.openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictBytes, StrictStr
from typing import Any, Optional, Tuple, Union
from typing_extensions import Annotated
from service.openapi_server.models.account_response import AccountResponse
from service.openapi_server.models.llm_configuration_request import LLMConfigurationRequest
from service.openapi_server.models.llm_configuration_response import LLMConfigurationResponse
from service.openapi_server.models.update_account_request import UpdateAccountRequest
from service.openapi_server.security_api import get_token_JWT

router = APIRouter()

#TODO: import will be reduced to necessary files
ns_pkg = business
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/account",
    responses={
        200: {"model": AccountResponse, "description": "Account data retrieved successfully"},
        401: {"description": "User not authenticated"},
    },
    tags=["Account"],
    summary="Get current authenticated user&#39;s account data",
    response_model_by_alias=True,
)
async def account_get(
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> AccountResponse:
    """Returns the account information for the currently authenticated user."""
    #TODO: call business logic


@router.put(
    "/account",
    responses={
        204: {"description": "Account updated successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
        409: {"description": "Email or username already taken"},
    },
    tags=["Account"],
    summary="Update account email and username",
    response_model_by_alias=True,
)
async def account_put(
    update_account_request: UpdateAccountRequest = Body(None, description=""),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> None:
    """Updates the authenticated user&#39;s email and username.  - **Both fields must be provided**.   - If the email is changed:   - User will be logged out from all sessions.   - Account will be set to unverified.   - A new email-verification email will be sent. """
    user_info: IUserInfoMange = Depends(get_user_info_manager())
    return await user_info.update_user_name_email(token_JWT,update_account_request)

#TODO: set file type for image
@router.get(
    "/account/profile-picture",
    responses={
        200: {"model": file, "description": "Profile picture returned successfully."},
        401: {"description": "User not authenticated"},
    },
    tags=["Account"],
    summary="Get the authenticated user&#39;s profile picture",
    response_model_by_alias=True,
)
async def account_profile_picture_get(
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> file:
    """Returns the profile picture for the authenticated user. The response is a binary image."""
    user_info: IUserInfoMange = Depends(get_user_info_manager())
    return await user_info.get_profile_picture(token_JWT)


@router.put(
    "/account/profile-picture",
    responses={
        204: {"description": "Profile Picture updated successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
    },
    tags=["Account"],
    summary="Updates the profile picture of the user that is authenticated",
    response_model_by_alias=True,
)
async def account_profile_picture_put(
    file: Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]] = Form(None, description=""),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> None:
    """Updates the profile picture of the user that is authenticated"""
    user_info: IUserInfoMange = Depends(get_user_info_manager())
    return await user_info.updateProfilePicture(file)


@router.post(
    "/account/llm-configurations",
    responses={
        201: {"description": "LLM configuration added successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
    },
    tags=["Account"],
    summary="Add a new LLM configuration to the account",
    response_model_by_alias=True,
)
async def account_llm_configurations_post(
    llm_configuration_request: LLMConfigurationRequest = Body(None, description=""),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> None:
    """Adds a new LLM configuration for the authenticated user."""
    system_manager: ISystemManger = Depends(get_user_info_manager())
    return await system_manager.validateAndPersistLLMConfig(token_JWT,llm_configuration_request)


@router.put(
    "/account/llm-configurations/{id}",
    responses={
        200: {"model": LLMConfigurationResponse, "description": "LLM configuration updated successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
        404: {"description": "LLM configuration not found"},
    },
    tags=["Account"],
    summary="Update a specific LLM configuration",
    response_model_by_alias=True,
)
async def account_llm_configurations_id_put(
    id: Annotated[StrictStr, Field(description="ID of the LLM configuration to update")] = Path(..., description="ID of the LLM configuration to update"),
    llm_configuration_request: LLMConfigurationRequest = Body(None, description=""),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> LLMConfigurationResponse:
    """Updates an existing LLM configuration of the authenticated user by its id."""
    system_manager: ISystemManger = Depends(get_user_info_manager())
    return await system_manager.updateLLMConfig(token_JWT,id, llm_configuration_request)


@router.delete(
    "/account/llm-configurations/{id}",
    responses={
        204: {"description": "LLM configuration deleted successfully"},
        401: {"description": "User not authenticated"},
        404: {"description": "LLM configuration not found"},
    },
    tags=["Account"],
    summary="Delete a specific LLM configuration",
    response_model_by_alias=True,
)
async def account_llm_configurations_id_delete(
    id: Annotated[StrictStr, Field(description="ID of the LLM configuration to delete")] = Path(..., description="ID of the LLM configuration to delete"),
    token_JWT: TokenModel = Security(
        get_token_JWT
    ),
) -> None:
    """Deletes an LLM configuration of the authenticated user by its id."""
    system_manager: ISystemManger = Depends(get_user_info_manager())
    return await system_manager.processLLMRemoval(token_JWT,id)
