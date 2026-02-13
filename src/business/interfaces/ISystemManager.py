from abc import ABC, abstractmethod

from typing import Annotated
from pydantic import Field
from uuid import UUID

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
    async def get_analytics(self):
        pass

    @abstractmethod
    async def validate_and_persist_llm_config(self, llm_configuration_request: LLMConfigurationRequest):
        pass

    @abstractmethod
    async def update_llm_config(
        self,
        llm_id: Annotated[
            UUID,
            Field(description="ID of the LLM configuration to update")
        ],
        llm_configuration_request: LLMConfigurationRequest
    ):
        pass

    @abstractmethod
    async def process_llm_removal(
        self,
        llm_id: Annotated[
            UUID,
            Field(description="ID of the LLM configuration to delete")
        ]
    ):
        pass
