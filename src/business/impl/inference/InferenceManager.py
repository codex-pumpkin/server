import datetime
import logging
import time
import uuid
from pydantic import Field
import re
import json
from typing import Optional

from src.core.dtos import (
    TokenModel,
    MessageRequest,
    ConversationRequest,
    ConversationResponse,
    UpdateConversationRequest,
    MessageResponse,
    Message
)

from src.core.exceptions import (
    QuotaExceededError,
    NotFoundError,
    AccessError,
    LLMRemovedError
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
        """
        Retrieve all conversations belonging to the authenticated user.

        @param token_jwt (TokenModel): Decoded JWT payload containing user id in `sub`.

        @return List[ConversationResponse]: User conversation list with metadata and messages.
        """
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
        """
        Append a new generated response to an existing conversation.

        @param conversation_id (UUID): Identifier of the target conversation.
        @param message_request (MessageRequest): Payload containing the user message text.
        @param token_jwt (TokenModel): Decoded JWT payload for access validation.

        @return MessageResponse: Newly persisted message/response pair.
        """
        repo = await PersistenceFactory.get_entity_repository()
        is_quota_exceeded = await repo.is_quota_exceeded(str(token_jwt.sub))
        if is_quota_exceeded:
            raise QuotaExceededError()

        conversation = await repo.get_chat_by_id(str(conversation_id))
        if conversation.llm_model_config_id is None:
            raise LLMRemovedError()


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
        name = await self._generate_conversation_name(message.response)
        if not message.response.startswith("Failed"):
            chat = await repo.get_chat_by_id(str(conversation_id))
            await repo.update_chat(chat_id=str(conversation_id), name=name, is_pinned=chat.pinned)
        return (await repo.get_messages(str(conversation_id)))[-1]

    async def message_regeneration(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="Id of the target conversation")
        ],
        message_request: MessageRequest,
        token_jwt: TokenModel
    ) -> MessageResponse:
        """
        Regenerate the most recent assistant response for a conversation.

        @param conversation_id (UUID): Identifier of the target conversation.
        @param message_request (MessageRequest): User prompt used for regeneration.
        @param token_jwt (TokenModel): Decoded JWT payload for access validation.

        @return MessageResponse: Replacement message generated and stored for the conversation.
        """
        repo = await PersistenceFactory.get_entity_repository()
        is_quota_exceeded = await repo.is_quota_exceeded(str(token_jwt.sub))
        if is_quota_exceeded:
            raise QuotaExceededError()

        conversation = await repo.get_chat_by_id(str(conversation_id))
        if conversation.llm_model_config_id is None:
            raise LLMRemovedError()

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
        return (await repo.get_messages(str(conversation_id)))[-1]

    async def remove_conversation(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="Id of the conversation to delete")
        ],
        token_jwt: TokenModel
    ):
        """
        Delete a conversation owned by the authenticated user.

        @param conversation_id (UUID): Identifier of the conversation to delete.
        @param token_jwt (TokenModel): Decoded JWT payload for ownership validation.

        @return None: Removes the conversation when ownership and existence checks pass.
        """
        repo = await PersistenceFactory.get_entity_repository()
        chat = await repo.get_chat_by_id(chat_id=str(conversation_id))

        if chat is None:
            raise NotFoundError(
                type_of="conversation",
                id_of=str(conversation_id)
            )

        if chat.user_id != token_jwt.sub:
            raise AccessError(
                type_of="conversation",
                id_of=str(chat.user_id)
            )

        await repo.delete_chat(str(conversation_id))


    async def _start_conversation_not_logged_in(
        self,
        request: ConversationRequest
    ) -> ConversationResponse:
        """
        Generate a one-off conversation result for unauthenticated users.

        @param request (ConversationRequest): Conversation payload including model id,
        @param target language, optional name, and first message.

        @return ConversationResponse: In-memory conversation object with a single generated message.
        """
        repo = await PersistenceFactory.get_entity_repository()
        api_key = await repo.get_key_of_model(request.llm_model_config_id)
        model = await repo.get_model(request.llm_model_config_id)

        start = time.monotonic()
        result, simulation_result = await self._get_llm_response_and_validate(
            user_input=request.message,
            conversation_history=[],
            api_key=api_key,
            model=model.model_name,
            llm_url=model.api_url
        )
        end = time.monotonic()
        chat_id = uuid.uuid4()

        graph_gen = await PersistenceFactory.get_graph_generator()
        graph = await graph_gen.gen_graph(code=result)
        name = await self._generate_conversation_name(result)

        message = MessageResponse(
            id=str(uuid.uuid4()),
            created_at=datetime.datetime.now(datetime.UTC).replace(tzinfo=None).timestamp(),
            message=request.message,
            response=result,
            graph=graph,
            simulation_result=self._parse_ngspice_output(simulation_result) if simulation_result else None,
            generation_millis=int((end - start) * 1000)
        )
        res = ConversationResponse(
            id=chat_id,
            name=name,
            target_language=request.target_language,
            llm_model_config_id=request.llm_model_config_id,
            created_at=datetime.datetime.now(datetime.UTC).replace(tzinfo=None).timestamp(),
            updated_at=datetime.datetime.now(datetime.UTC).replace(tzinfo=None).timestamp(),
            user_id=uuid.uuid4(),
            messages=[message]
        )
        return res


    async def _start_conversation(
        self,
        token_jwt: TokenModel,
        request:ConversationRequest
    ) -> ConversationResponse:
        """
        Create a persisted conversation for an authenticated user and add first message.

        @param token_jwt (TokenModel): Decoded JWT payload containing user identifier.
        @param request (ConversationRequest): Conversation creation payload.

        @return ConversationResponse: Persisted conversation with the initial generated reply.
        """
        repo = await PersistenceFactory.get_entity_repository()
        is_quota_exceeded = await repo.is_quota_exceeded(str(token_jwt.sub))
        if is_quota_exceeded:
            raise QuotaExceededError()

        result = await repo.create_chat(str(token_jwt.sub), request)
        await self.post_message_to_conversation(
            conversation_id=uuid.UUID(result),
            message_request=MessageRequest(message=request.message),
            token_jwt=token_jwt
        )
        return await repo.get_chat_by_id(result)

    async def start_conversation(
        self,
        token_jwt: Optional[TokenModel],
        conversation_request: ConversationRequest
    ) -> ConversationResponse:
        """
        Start a conversation in authenticated or unauthenticated mode.

        @param token_jwt (Optional[TokenModel]): Auth token payload when user is logged in,
            or `None` for guest flow.
        @param conversation_request (ConversationRequest): Conversation start request.

        @return ConversationResponse: Conversation object returned from the selected flow.
        """
        if token_jwt is None:
            return await self._start_conversation_not_logged_in(
                request=conversation_request
            )
        else:
            return await self._start_conversation(
                token_jwt=token_jwt,
                request=conversation_request
            )


    async def update_conversation(
        self,
        conversation_id: Annotated[
            UUID,
            Field(description="ID of the conversation to update")
        ],
        update_conversation_request: UpdateConversationRequest,
        token_jwt: TokenModel
    ) -> None:
        """
        Update mutable conversation fields such as name and pin state.

        @param conversation_id (UUID): Identifier of the conversation to update.
        @param update_conversation_request (UpdateConversationRequest): New editable values.
        @param token_jwt (TokenModel): Decoded JWT payload for ownership validation.

        @return None: Persists the requested conversation updates.
        """
        repo = await PersistenceFactory.get_entity_repository()
        chat = await repo.get_chat_by_id(chat_id=str(conversation_id))

        if chat is None:
            raise NotFoundError(
                type_of="conversation",
                id_of=str(conversation_id)
            )
        if chat.user_id != token_jwt.sub:
            raise AccessError(
                type_of="conversation",
                id_of=str(chat.user_id)
            )

        await repo.update_chat(
            chat_id=str(conversation_id),
            is_pinned=update_conversation_request.pinned,
            name=update_conversation_request.name
        )

    async def _get_message(
        self,
        conversation_id: UUID,
        message_request: MessageRequest,
        token_jwt: TokenModel,
        repo: IEntityRepository,
        remove_last: bool = False
    ) -> Message:
        """
        Generate a message payload by invoking the LLM and graph generator.

        @param conversation_id (UUID): Conversation identifier used for lookup and access checks.
        @param message_request (MessageRequest): User message used as LLM input.
        @param token_jwt (TokenModel): Decoded JWT payload for access control.
        @param repo (IEntityRepository): Repository instance used for data loading.
        @param remove_last (bool, optional): Whether to drop the last turn from history,
        @param primarily used for regeneration. Defaults to False.

        @return Message: Message entity ready for persistence.
        """
        chat = await repo.get_chat_by_id(chat_id=str(conversation_id))
        if chat is None:
            raise NotFoundError(
                type_of="conversation",
                id_of=str(conversation_id)
            )

        if chat.user_id != token_jwt.sub:
            raise AccessError(
                type_of="conversation",
                id_of=str(chat.user_id)
            )

        model = await repo.get_llm_by_chat_id(chat_id=str(conversation_id))
        messages = [(message.message, message.response) for message in chat.messages]
        if remove_last:
            messages = messages[:-1]
        start = time.monotonic()
        result, simulation_result = await self._get_llm_response_and_validate(
            user_input=message_request.message,
            conversation_history=messages,
            api_key=model.api_key,
            model=model.model_name,
            llm_url=model.api_url
        )
        graph = await self._get_graph_representation(result)
        
        end = time.monotonic()
        message = Message(
            conversation_id=str(conversation_id),
            response=result,
            message=message_request.message,
            graph=graph,
            simulation_result=self._parse_ngspice_output(simulation_result) if simulation_result else "No simulation result",
            generation_millis=int((end - start) * 1000)
        )
        return message

    async def _get_graph_representation(self, llm_response: str) -> str:
        """
        Convert generated code into graph representation.

        @param llm_response (str): Generated code text returned by the language model.

        @return str: Graph serialization produced by the graph generator backend.
        """
        graph_generator = await PersistenceFactory.get_graph_generator()
        graph = await graph_generator.gen_graph(llm_response)
        return graph

    async def _get_llm_response_and_validate(
        self,
        user_input: str,
        conversation_history: List[Tuple[str, str]],
        api_key: str,
        model: str,
        llm_url: str
    ) -> Tuple[str, str]:
        """
        Generate code, validate it, and regenerate when validation fails.

        @param user_input (str): Current user prompt sent to the model.
        @param conversation_history (List[Tuple[str, str]]): Prior conversation turns.
        @param api_key (str): API key for the configured LLM provider.
        @param model (str): Provider-specific model identifier.
        @param llm_url (str): Base URL for the LLM API endpoint.

        @return str: Valid generated code or a fallback failure string if retries are exhausted.
        """
        prompt_manager = await BusinessFactory.get_prompt_manager()
        validator = await PersistenceFactory.get_code_validator()
        aiclient = await PersistenceFactory.get_ai_client()

        doc_context = await prompt_manager.retrieve_context(user_input)
        print(doc_context)
        conversation_history = prompt_manager.get_conversation_context(conversation_history)
    
        code = await aiclient.get_response(user_input, doc_context, conversation_history, api_key, model, llm_url)
        code = await self._clean_markdown(code)

        validation_result = await validator.validate_code(code)

        if not validation_result.isValid:
            for i in range(settings.llm_settings.num_of_regenerations):
                context = prompt_manager.make_regeneration_context(
                    validation_result.exitCode, validation_result.rawOutput)
                
                code = await aiclient.regenerate(user_input, context, code, api_key, model, llm_url)
                code = await self._clean_markdown(code)
                
                validation_result = await validator.validate_code(code) 
                if validation_result.isValid:
                    return code, validation_result.rawOutput
        else:
            return code, validation_result.rawOutput

        return "Failed to generate valid code after multiple attempts.", None
    
    
    async def _clean_markdown(self, code: str) -> str:
        """
        Remove fenced markdown wrappers from generated code blocks.

        @param code (str): Raw LLM output that may include triple-backtick fences.

        @return str: Cleaned code content without markdown fencing.
        """
        if code.startswith("```") and code.endswith("```"):
            code = "\n".join(code.split("\n")[1:-1])
        return code
    
    async def _generate_conversation_name(self, llm_response: str) -> str:
        """
        Generate a conversation name based on the initial LLM response.

        @param llm_response (str): The first generated response in the conversation.

        @return str: A concise title for the conversation derived from the response.
        """

        return llm_response.strip().splitlines()[0][2:]

    def _parse_ngspice_output(self, raw: str) -> Optional[str]:
        """
        Parse raw ngspice text output into a compact JSON string suitable for the frontend.
    
        Keeps the raw text untouched for LLM regeneration context — this is only called
        when constructing the DTO to send to the client.
    
        @param raw (str): Raw stdout from ngspice.
    
        @return Optional[str]: JSON string with structured simulation data, or None if parsing fails.
        """
        try:
            analysis_match = re.search(r'\b(Transient Analysis|AC Analysis|DC Transfer Curve)\b', raw, re.IGNORECASE)
            analysis_type = "transient"
            if analysis_match:
                t = analysis_match.group(1).lower()
                if "ac" in t:
                    analysis_type = "ac"
                elif "dc" in t:
                    analysis_type = "dc"
    
            header_match = re.search(r'^(Index(?:\s+[\w().#]+)+)\s*$', raw, re.MULTILINE)
            if not header_match:
                return None
    
            all_cols = header_match.group(0).strip().split()
            x_name = all_cols[1]
            var_names = all_cols[2:]
    
            data_row_re = re.compile(r'^\d+\t([\d.e+\-]+)(\t[\d.e+\-]+)+', re.MULTILINE)
    
            x_values = []
            var_values = [[] for _ in var_names]
    
            for match in data_row_re.finditer(raw):
                cols = match.group(0).strip().split('\t')
                try:
                    x_values.append(float(cols[1]))
                except (IndexError, ValueError):
                    continue
                for i, _ in enumerate(var_names):
                    try:
                        var_values[i].append(float(cols[2 + i]))
                    except (IndexError, ValueError):
                        var_values[i].append(0.0)
    
            if not x_values:
                return None
    
            max_points = 300
            total = len(x_values)
            if total > max_points:
                step = total / max_points
                indices = [int(i * step) for i in range(max_points)]
                indices[-1] = total - 1 
                x_values = [x_values[i] for i in indices]
                var_values = [[col[i] for i in indices] for col in var_values]
    
            result = {
                "type": analysis_type,
                "x_axis": {
                    "name": x_name,
                    "values": x_values
                },
                "variables": [
                    {"name": name, "values": var_values[i]}
                    for i, name in enumerate(var_names)
                ]
            }
    
            return json.dumps(result, separators=(',', ':'))
    
        except Exception:
            logging.error("Returning null inside InferenceManager.py for _parse_ngspice_output")
            return None