
# coding: utf-8

from typing import Dict, List  # noqa: F401

from src.business.interfaces import (
    IUserInfoManager,
    ISystemManager
)


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
    UploadFile,
    File,
)

from uuid import UUID

from src.core.dtos.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictBytes, StrictStr
from typing import Optional, Tuple, Union
from typing_extensions import Annotated
from src.core.dtos.account_response import AccountResponse
from src.core.dtos.llm_configuration_request import LLMConfigurationRequest
from src.core.dtos.llm_configuration_response import LLMConfigurationResponse
from src.core.dtos.update_account_request import UpdateAccountRequest
from src.service.security_api import get_token_jwt, get_token_jwt_mandatory_admin

router = APIRouter()


@router.get(
    "/llm-configurations",
    responses={
        201: {"description": "LLM configuration added successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
    },
    tags=["LLM"],
    summary="Gets all LLM configurations",
    response_model_by_alias=True,
)
async def llm_configurations_get(
    system_manager: ISystemManager = Depends(get_system_manager)
) -> List[LLMConfigurationResponse]:
    """
    Return all configured LLM model entries.

    @param
        system_manager (ISystemManager): Business manager used to fetch model configurations.

    @return
        List[LLMConfigurationResponse]: Persisted LLM configuration records.
    """
    return await system_manager.get_llm_configs()


@router.post(
    "/llm-configurations",
    responses={
        201: {"description": "LLM configuration added successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
    },
    tags=["LLM"],
    summary="Add a new LLM configuration to the account",
    response_model_by_alias=True,
)
async def llm_configurations_post(
    llm_configuration_request: LLMConfigurationRequest = Body(None, description=""),
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory_admin
    ),
    system_manager: ISystemManager = Depends(get_system_manager)
) -> None:
    """
    Create a new LLM configuration entry.

    @param
        llm_configuration_request (LLMConfigurationRequest): Payload with model endpoint and credentials.
        token_jwt (TokenModel): Admin-authenticated token payload.
        system_manager (ISystemManager): Business manager used to persist model config.

    @return
        None: Stores a new LLM configuration.
    """
    return await system_manager.validate_and_persist_llm_config(llm_configuration_request)


@router.put(
    "/llm-configurations/{llm_id}",
    responses={
        200: {"model": LLMConfigurationResponse, "description": "LLM configuration updated successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
        404: {"description": "LLM configuration not found"},
    },
    tags=["LLM"],
    summary="Update a specific LLM configuration",
    response_model_by_alias=True,
)
async def llm_configurations_id_put(
    llm_id: Annotated[
        UUID,
        Field(description="ID of the LLM configuration to update")
    ] = Path(..., description="ID of the LLM configuration to update"),
    llm_configuration_request: LLMConfigurationRequest = Body(None, description=""),
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory_admin
    ),
    system_manager: ISystemManager = Depends(get_system_manager)

) -> None:
    """
    Update an existing LLM configuration by identifier.

    @param
        llm_id (UUID): Identifier of LLM configuration to update.
        llm_configuration_request (LLMConfigurationRequest): Payload with updated model values.
        token_jwt (TokenModel): Admin-authenticated token payload.
        system_manager (ISystemManager): Business manager used to persist update.

    @return
        None: Applies requested LLM configuration changes.
    """
    return await system_manager.update_llm_config(
        llm_id=llm_id,
        llm_configuration_request=llm_configuration_request
    )


@router.delete(
    "/llm-configurations/{llm_id}",
    responses={
        204: {"description": "LLM configuration deleted successfully"},
        401: {"description": "User not authenticated"},
        404: {"description": "LLM configuration not found"},
    },
    tags=["LLM"],
    summary="Delete a specific LLM configuration",
    response_model_by_alias=True,
)
async def llm_configurations_id_delete(
    llm_id: Annotated[
        UUID,
        Field(description="ID of the LLM configuration to delete")
    ] = Path(..., description="ID of the LLM configuration to delete"),
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory_admin
    ),
    system_manager: ISystemManager = Depends(get_system_manager)

) -> None:
    """
    Delete an LLM configuration by identifier.

    @param
        llm_id (UUID): Identifier of LLM configuration to delete.
        token_jwt (TokenModel): Admin-authenticated token payload.
        system_manager (ISystemManager): Business manager used to remove model config.

    @return
        None: Removes the target LLM configuration.
    """
    return await system_manager.process_llm_removal(llm_id=llm_id)
