
from typing import Annotated, List
from pydantic import StrictStr, Field

from src.core.dtos import (
    TokenModel,
    QuotaConfig,
    LLMConfigurationRequest,
    LLMConfigurationResponse
)

from src.core.exceptions import (
    NotFoundError
)


from src.business.interfaces import ISystemManager
from src.persistence import PersistenceFactory
from uuid import UUID

class SystemManager(ISystemManager):

    async def get_llm_configs(self) -> List[LLMConfigurationResponse]:
        """Get llm configs."""
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.get_llm_configs()

    async def get_quota_settings(self):
        """Get quota settings."""
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.get_quota()

    async def apply_quota_adjustment(self, quota_config: QuotaConfig) -> None:
        """Apply quota adjustment."""
        repo = await PersistenceFactory.get_entity_repository()
        await repo.change_quota(quota_config)

    async def get_analytics(self):
        """Get analytics."""
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.get_usage_data()

    async def validate_and_persist_llm_config(self, llm_configuration_request: LLMConfigurationRequest):
        """Validate and persist llm config."""
        repo = await PersistenceFactory.get_entity_repository()
        await repo.add_model(
            name=llm_configuration_request.name,
            url=llm_configuration_request.api_url,
            key=llm_configuration_request.api_key,
            model_name=llm_configuration_request.model_name
        )

    async def update_llm_config(
        self,
        llm_id: Annotated[
            UUID,
            Field(description="ID of the LLM configuration to update")
        ],
        llm_configuration_request: LLMConfigurationRequest
    ):
        """Update llm config."""
        repo = await PersistenceFactory.get_entity_repository()
        model = await repo.get_model(model_id=str(llm_id))
        if model is None:
            raise NotFoundError(
                type_of="model",
                id_of=str(llm_id)
            )
        await repo.change_model(
            model_id=str(llm_id),
            name=llm_configuration_request.name,
            url=llm_configuration_request.api_url,
            key=llm_configuration_request.api_key,
            model_name=llm_configuration_request.model_name
        )

    async def process_llm_removal(
        self,
        llm_id: Annotated[
            UUID,
            Field(description="ID of the LLM configuration to delete")
        ]
    ):
        """Process llm removal."""
        repo = await PersistenceFactory.get_entity_repository()
        model = await repo.get_model(model_id=str(llm_id))
        if model is None:
            raise NotFoundError(
                type_of="model",
                id_of=str(llm_id)
            )

        await repo.remove_model(model_id=str(llm_id))
