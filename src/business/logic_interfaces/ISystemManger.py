from abc import ABC, abstractmethod
#TODO add imports for datatyps

class ISystemManager(ABC):

    async def getQuotaSettings(token_JWT: TokenModel):
        pass

    async def applyQuotaAdjustment(token_JWT: TokenModel, quota_config: QuotaConfig):
        pass

    async def get_analytics(token_JWT: TokenModel):
        pass

    async def validateAndPersistLLMConfig(token_JWT: TokenModel, llm_configuration_request: LLMConfigurationRequest):
        pass

    async def updateLLMConfig(token_JWT: TokenModel, id: Annotated[StrictStr, Field(
        description="ID of the LLM configuration to update")], llm_configuration_request: LLMConfigurationRequest):
        pass

    async def processLLMRemoval(token_JWT: TokenModel, id: Annotated[
        StrictStr, Field(description="ID of the LLM configuration to delete")]):
        pass
