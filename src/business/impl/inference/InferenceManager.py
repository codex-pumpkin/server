import time
from idlelib.window import add_windows_to_menu
from typing import Annotated
from typing import Tuple, List
from pydantic import Field, StrictInt, StrictStr

from src.core.dtos import (
    TokenModel,
    MessageRequest,
    ConversationRequest,
    ConversationResponse,
    UpdateConversationRequest,
    MessageResponse,
    Message
)

from typing import List

from src.business.interfaces import IInferenceManager
from src.persistence.factory.PersistenceFactory import PersistenceFactory
from src.business.factory.BusinessFactory import BusinessFactory
from src.core.settings import settings

from uuid import UUID

class InferenceManager(IInferenceManager):

    async def get_conversations_by_user(self, token_jwt: TokenModel) -> List[ConversationResponse]:
        repo = await PersistenceFactory.get_entity_repository()
        return await repo.get_chats(str(token_jwt.sub))

    async def post_message_to_conversation(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="Id of the target conversation")
        ],
        message_request: MessageRequest,
        token_jwt: TokenModel
    ):
        repo = await PersistenceFactory.get_entity_repository()
        chat = await repo.get_chat_by_id(chat_id=str(conversation_id))
        if chat is None:
            raise Exception("Conversation with such Id doesnt exist!")
        if chat.user_id != token_jwt.sub:
            raise Exception("Conversation doesnt belong to the user!")

        messages = [(message.message, message.response) for message in chat.messages]

        start = time.monotonic()
        result = await self._get_llm_response_and_validate(
            user_input=message_request.message,
            conversation_history=messages
        )
        end = time.monotonic()
        message = Message(
            conversation_id=conversation_id,
            response=result,
            message=message_request.message,
            response_secondary=result,
            generation_millis=int((end - start) * 1000)
        )
        await repo.add_message(
            chat_id=str(conversation_id),
            message=message
        )

    async def message_regeneration(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="Id of the target conversation")
        ],
        message_request: MessageRequest,
        token_jwt: TokenModel
    ):
        pass

    async def remove_conversation(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="Id of the conversation to delete")
        ],
        token_jwt: TokenModel
    ):
        pass

    async def start_conversation(self, token_jwt: TokenModel, conversation_request: ConversationRequest) -> ConversationResponse:
        ...


    async def update_conversation(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="ID of the conversation to update")
        ],
        update_conversation_request: UpdateConversationRequest,
        token_jwt: TokenModel
    ) -> None:
        repo = await PersistenceFactory.get_entity_repository()
        chat = await repo.get_chat_by_id(chat_id=str(token_jwt.sub))
        if chat.user_id != conversation_id:
            raise Exception("later")

        await repo.update_chat(
            chat_id=str(conversation_id),
            is_pinned=UpdateConversationRequest.pinned,
            name=UpdateConversationRequest.name
        )



    async def _get_llm_response_and_validate(self, user_input: str, conversation_history: List[Tuple[str, str]]) -> str:
        """
        Generate code based on user input, validate it, and regenerate if necessary.
        user_input: The user's input prompt.
        conversation_history: chat of user with LLM.
        Returns the valid generated code as a string.
        """
        prompt_manager = await BusinessFactory.get_prompt_manager()
        validator = await PersistenceFactory.get_code_validator()
        aiclient = await PersistenceFactory.get_ai_client()
        api_key = settings.llm_settings.api_key

        doc_context = await prompt_manager.retrieve_context(user_input)
        conversation_history = prompt_manager.get_conversation_context(conversation_history)

        code = await aiclient.get_response(user_input, doc_context, conversation_history, api_key)
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