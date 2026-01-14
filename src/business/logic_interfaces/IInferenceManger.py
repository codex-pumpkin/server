from abc import ABC, abstractmethod
#TODO add imports for datatyps

class IInferenceManager(ABC):

    @abstractmethod
    async def getConversationsByUser(token_JWT: TokenModel):
        pass

    @abstractmethod
    async def post_message_to_conversation(id: Annotated[StrictInt, Field(
        description="Id of the target conversation")], message_request: MessageRequest, token_JWT: TokenModel):
        pass

    @abstractmethod
    async def message_regeneration(id: Annotated[StrictInt, Field(
        description="Id of the target conversation")], message_request: MessageRequest, token_JWT: TokenModel):
        pass

    @abstractmethod
    async def removeConversation(id: Annotated[
        StrictStr, Field(description="Id of the conversation to delete")], token_JWT: TokenModel):
        pass

    @abstractmethod
    async def startConversation(token_JWT: TokenModel, conversation_request: ConversationRequest):
        pass

    @abstractmethod
    async def update_conversation(id: Annotated[StrictStr, Field(
        description="ID of the conversation to update")], update_conversation_request: UpdateConversationRequest, token_JWT: TokenModel):
        pass