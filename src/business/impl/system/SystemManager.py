
from typing import Annotated
from pydantic import StrictStr, Field

from src.core.dtos import (
    TokenModel,
    QuotaConfig,
    LLMConfigurationRequest
)

from src.business.interfaces import ISystemManager
from src.persistence import PersistenceFactory


class SystemManager(ISystemManager):
    async def get_quota_settings(self):
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.get_quota()

    async def apply_quota_adjustment(self, quota_config: QuotaConfig) -> None:
        repo = await PersistenceFactory.get_entity_repository()
        await repo.change_quota(quota_config)

    async def get_analytics(self, token_jwt: TokenModel):
        pass

    async def validate_and_persist_llm_config(self, token_jwt: TokenModel, llm_configuration_request: LLMConfigurationRequest):
        pass

    async def update_llm_config(self, token_jwt: TokenModel, id: Annotated[StrictStr, Field(
        description="ID of the LLM configuration to update")], llm_configuration_request: LLMConfigurationRequest):
        pass

    async def process_llm_removal(self, token_jwt: TokenModel, id: Annotated[
        StrictStr, Field(description="ID of the LLM configuration to delete")]):
        pass
