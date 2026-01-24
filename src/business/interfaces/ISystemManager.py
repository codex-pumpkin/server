from abc import ABC, abstractmethod

from typing import Annotated
from pydantic import StrictStr, Field

from src.core.dtos import (
    TokenModel,
    QuotaConfig,
    LLMConfigurationRequest
)

class ISystemManager(ABC):
    @abstractmethod
    async def get_quota_settings(self):
        pass

    @abstractmethod
    async def apply_quota_adjustment(self, quota_config: QuotaConfig):
        pass

    @abstractmethod
    async def get_analytics(self, token_jwt: TokenModel):
        pass

    @abstractmethod
    async def validate_and_persist_llm_config(self, token_jwt: TokenModel, llm_configuration_request: LLMConfigurationRequest):
        pass

    @abstractmethod
    async def update_llm_config(self, token_jwt: TokenModel, id: Annotated[StrictStr, Field(
        description="ID of the LLM configuration to update")], llm_configuration_request: LLMConfigurationRequest):
        pass

    @abstractmethod
    async def process_llm_removal(self, token_jwt: TokenModel, id: Annotated[
        StrictStr, Field(description="ID of the LLM configuration to delete")]):
        pass
