import datetime
import time
import uuid
from pydantic import Field

from src.core.dtos import (
    TokenModel,
    MessageRequest,
    ConversationRequest,
    ConversationResponse,
    UpdateConversationRequest,
    MessageResponse,
    Message
)

from typing import List, Optional, Tuple, Annotated

from src.business.interfaces import IInferenceManager
from src.persistence import IEntityRepository
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

        message = await self._get_message(
            conversation_id=conversation_id,
            message_request=message_request,
            token_jwt=token_jwt,
            repo=repo,
            remove_last=False
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
        repo = await PersistenceFactory.get_entity_repository()
        message = await self._get_message(
            conversation_id=conversation_id,
            message_request=message_request,
            token_jwt=token_jwt,
            repo=repo,
            remove_last=True
        )

        await repo.delete_last_message(
            chat_id=str(conversation_id)
        )
        await repo.add_message(
            chat_id=str(conversation_id),
            message=message
        )

    async def remove_conversation(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="Id of the conversation to delete")
        ],
        token_jwt: TokenModel
    ):
        repo = await PersistenceFactory.get_entity_repository()
        chat = await repo.get_chat_by_id(chat_id=str(token_jwt.sub))
        if chat.user_id != conversation_id:
            raise Exception("later")

        await repo.delete_chat(str(conversation_id))


    async def _start_conversation_not_logged_in(
        self,
        request: ConversationRequest
    ) -> ConversationResponse:
        start = time.monotonic()
        result = await self._get_llm_response_and_validate(
            user_input=request.message,
            conversation_history=[]
        )
        end = time.monotonic()
        chat_id = uuid.uuid4()

        message = MessageResponse(
            id=uuid.uuid4(),
            created_at=datetime.datetime.now(datetime.UTC),
            message=request.message,
            response=result,
            response_secondary=result,
            generation_millis=int((end - start) / 1000)
        )
        res = ConversationResponse(
            id=chat_id,
            name=request.name,
            target_language=request.target_language,
            llm_model_config_id=request.llm_model_config_id,
            created_at=datetime.datetime.now(datetime.UTC),
            updated_at=datetime.datetime.now(datetime.UTC),
            user_id=uuid.uuid4(),
            messages=[message]
        )
        return res


    async def _start_conversation(
        self,
        token_jwt: TokenModel,
        request:ConversationRequest
    ) -> ConversationResponse:
        repo = await PersistenceFactory.get_entity_repository()
        result = await repo.create_chat(str(token_jwt.sub), request)

        await self.post_message_to_conversation(
            conversation_id=result.id,
            message_request=MessageRequest(message=request.message),
            token_jwt=token_jwt
        )
        return await repo.get_chat_by_id(str(result.id))

    async def start_conversation(
        self,
        token_jwt: Optional[TokenModel],
        conversation_request: ConversationRequest
    ) -> ConversationResponse:
        if token_jwt is not None:
            return await self._start_conversation_not_logged_in(request=conversation_request)
        else:
            return await self._start_conversation(token_jwt=token_jwt, request=conversation_request)


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

    async def _get_message(
        self,
        conversation_id: UUID,
        message_request: MessageRequest,
        token_jwt: TokenModel,
        repo: IEntityRepository,
        remove_last: bool = False
    ) -> Message:
        chat = await repo.get_chat_by_id(chat_id=str(conversation_id))
        if chat is None:
            raise Exception("Conversation with such Id doesnt exist!")
        if chat.user_id != token_jwt.sub:
            raise Exception("Conversation doesnt belong to the user!")

        api_key = await repo.get_llm_key_by_chat_id(chat_id=str(conversation_id))
        messages = [(message.message, message.response) for message in chat.messages]
        if remove_last:
            messages = messages[:-1]
        start = time.monotonic()
        result = await self._get_llm_response_and_validate(
            user_input=message_request.message,
            conversation_history=messages,
            api_key=api_key
        )
        end = time.monotonic()
        message = Message(
            conversation_id=conversation_id,
            response=result,
            message=message_request.message,
            response_secondary=result,
            generation_millis=int((end - start) * 1000)
        )
        return message

    async def _get_llm_response_and_validate(
        self,
        user_input: str,
        conversation_history: List[Tuple[str, str]],
        api_key: str,
    ) -> str:
        """
        Generate code based on user input, validate it, and regenerate if necessary.
        user_input: The user's input prompt.
        conversation_history: chat of user with LLM.
        Returns the valid generated code as a string.
        """
        prompt_manager = await BusinessFactory.get_prompt_manager()
        validator = await PersistenceFactory.get_code_validator()
        aiclient = await PersistenceFactory.get_ai_client()

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