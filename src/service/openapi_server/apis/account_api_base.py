# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBytes, StrictStr
from typing import Any, Optional, Tuple, Union
from typing_extensions import Annotated
from service.openapi_server.models.account_response import AccountResponse
from service.openapi_server.models.llm_configuration_request import LLMConfigurationRequest
from service.openapi_server.models.llm_configuration_response import LLMConfigurationResponse
from service.openapi_server.models.update_account_request import UpdateAccountRequest
from service.openapi_server.security_api import get_token_JWT

class BaseAccountApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAccountApi.subclasses = BaseAccountApi.subclasses + (cls,)
    async def account_get(
        self,
    ) -> AccountResponse:
        """Returns the account information for the currently authenticated user."""
        ...


    async def account_put(
        self,
        update_account_request: UpdateAccountRequest,
    ) -> None:
        """Updates the authenticated user&#39;s email and username.  - **Both fields must be provided**.   - If the email is changed:   - User will be logged out from all sessions.   - Account will be set to unverified.   - A new email-verification email will be sent. """
        ...


    async def account_profile_picture_get(
        self,
    ) -> file:
        """Returns the profile picture for the authenticated user. The response is a binary image."""
        ...


    async def account_profile_picture_put(
        self,
        file: Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]],
    ) -> None:
        """Updates the profile picture of the user that is authenticated"""
        ...


    async def account_llm_configurations_post(
        self,
        llm_configuration_request: LLMConfigurationRequest,
    ) -> None:
        """Adds a new LLM configuration for the authenticated user."""
        ...


    async def account_llm_configurations_id_put(
        self,
        id: Annotated[StrictStr, Field(description="ID of the LLM configuration to update")],
        llm_configuration_request: LLMConfigurationRequest,
    ) -> LLMConfigurationResponse:
        """Updates an existing LLM configuration of the authenticated user by its id."""
        ...


    async def account_llm_configurations_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="ID of the LLM configuration to delete")],
    ) -> None:
        """Deletes an LLM configuration of the authenticated user by its id."""
        ...
