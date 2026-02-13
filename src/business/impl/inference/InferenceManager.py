from typing import Annotated
from pydantic import Field, StrictInt, StrictStr

from src.core.dtos import (
    TokenModel,
    MessageRequest,
    ConversationRequest,
    UpdateConversationRequest
)

from src.business.interfaces import IInferenceManager
from src.persistence.factory.PersistenceFactory import PersistenceFactory
from src.business.factory.BusinessFactory import BusinessFactory
from src.core.settings import settings


class InferenceManager(IInferenceManager):

    async def get_conversations_by_user(self, token_jwt: TokenModel):
        pass

    async def post_message_to_conversation(self, id: Annotated[StrictInt, Field(
        description="Id of the target conversation")], message_request: MessageRequest, token_jwt: TokenModel):
        pass

    async def message_regeneration(self, id: Annotated[StrictInt, Field(
        description="Id of the target conversation")], message_request: MessageRequest, token_jwt: TokenModel):
        pass

    async def remove_conversation(self, id: Annotated[
        StrictStr, Field(description="Id of the conversation to delete")], token_jwt: TokenModel):
        pass

    async def start_conversation(self, token_jwt: TokenModel, conversation_request: ConversationRequest):
        pass

    async def update_conversation(self, id: Annotated[StrictStr, Field(
        description="ID of the conversation to update")], update_conversation_request: UpdateConversationRequest, token_jwt: TokenModel):
        pass


    async def _get_llm_response_and_validate(self, user_input: str) -> str:
        """
        Generate code based on user input, validate it, and regenerate if necessary.
        user_input: The user's input prompt.
        Returns the valid generated code as a string.
        """
        prompt_manager = await BusinessFactory.get_prompt_manager()
        validator = await PersistenceFactory.get_code_validator()
        aiclient = await PersistenceFactory.get_ai_client()
        api_key = settings.llm_settings.api_key

        doc_context = await prompt_manager.retrieve_context(user_input)

        code = await aiclient.get_response(user_input, doc_context, api_key)
        code = await self._clean_markdown(code)

        validation_result = await validator.validate_code(code)

        if not validation_result.is_valid:
            for i in range(settings.llm_settings.num_of_regenerations):
                context = prompt_manager.make_regeneration_context(
                    validation_result.exitCode, validation_result.rawOutput)
                
                code = await aiclient.regenerate(user_input, context, code, api_key)
                code = await self._clean_markdown(code)
                
                validation_result = await validator.validate_code(code)
                if validation_result.isValid:
                    return code
        else:
            return code       

        return "Failed to generate valid code after multiple attempts."
    
    
    async def _clean_markdown(self, code: str) -> str:
        """Remove markdown formatting from the generated code."""
        if code.startswith("```") and code.endswith("```"):
            code = "\n".join(code.split("\n")[1:-1])
        return code