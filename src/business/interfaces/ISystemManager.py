from abc import ABC, abstractmethod

from typing import Annotated, List
from pydantic import Field
from uuid import UUID

from src.core.dtos import (
    TokenModel,
    QuotaConfig,
    LLMConfigurationRequest,
    LLMConfigurationResponse,
    AnalyticsRequest
)

class ISystemManager(ABC):
    @abstractmethod
    async def get_quota_settings(self):
        """Get quota settings."""
        pass

    @abstractmethod
    async def apply_quota_adjustment(self, quota_config: QuotaConfig):
        """Apply quota adjustment."""
        pass

    @abstractmethod
    async def get_analytics(self, analytics_request: AnalyticsRequest):
        """Get analytics."""
        pass

    @abstractmethod
    async def get_llm_configs(self) -> List[LLMConfigurationResponse]:
        """Get llm configs."""
        pass

    @abstractmethod
    async def validate_and_persist_llm_config(self, llm_configuration_request: LLMConfigurationRequest):
        """Validate and persist llm config."""
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
        """Update llm config."""
        pass

    @abstractmethod
    async def process_llm_removal(
        self,
        llm_id: Annotated[
            UUID,
            Field(description="ID of the LLM configuration to delete")
        ]
    ):
        """Process llm removal."""
        pass
