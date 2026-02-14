
from typing import Annotated, List
from pydantic import StrictStr, Field

from src.core.dtos import (
    TokenModel,
    QuotaConfig,
    LLMConfigurationRequest,
    LLMConfigurationResponse
)

from src.business.interfaces import ISystemManager
from src.persistence import PersistenceFactory
from uuid import UUID

class SystemManager(ISystemManager):

    async def get_llm_configs(self) -> List[LLMConfigurationResponse]:
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.get_llm_configs()

    async def get_quota_settings(self):
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.get_quota()

    async def apply_quota_adjustment(self, quota_config: QuotaConfig) -> None:
        repo = await PersistenceFactory.get_entity_repository()
        await repo.change_quota(quota_config)

    async def get_analytics(self):
        pass

    async def validate_and_persist_llm_config(self, llm_configuration_request: LLMConfigurationRequest):
        repo = await PersistenceFactory.get_entity_repository()
        await repo.add_model(
            name=llm_configuration_request.name,
            url=llm_configuration_request.api_url,
            key=llm_configuration_request.api_key
        )

    async def update_llm_config(
        self,
        llm_id: Annotated[
            UUID,
            Field(description="ID of the LLM configuration to update")
        ],
        llm_configuration_request: LLMConfigurationRequest
    ):
        repo = await PersistenceFactory.get_entity_repository()
        model = await repo.get_model(model_id=str(llm_id))
        if model is None:
            raise Exception("No model with such ID!")
        await repo.change_model(
            model_id=str(llm_id),
            name=llm_configuration_request.name,
            url=llm_configuration_request.api_url,
            key=llm_configuration_request.api_key
        )

    async def process_llm_removal(
        self,
        llm_id: Annotated[
            UUID,
            Field(description="ID of the LLM configuration to delete")
        ]
    ):
        repo = await PersistenceFactory.get_entity_repository()
        model = await repo.get_model(model_id=str(llm_id))
        if model is None:
            raise Exception("model with such index doesnt exist")

        await repo.remove_model(model_id=str(llm_id))
